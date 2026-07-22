# -*- coding: utf-8 -*-
from odoo import api, models


class MinimumSalesMarginSeed(models.AbstractModel):
    """Seed a default row on the Studio-manual x_minimum_sales_margin
    catalogue for every active res.company that doesn't already have
    one.

    Why this is needed
    ------------------
    x_minimum_sales_margin is a Studio catalogue holding one row per
    company with fields that other Studio logic reads at runtime:

      - x_studio_advance_payment_ (float, %) — minimum advance
        payment required on Repair sale orders
      - x_studio_minimum_sales_margin_ (float, %)
      - x_studio_sales_order_validity (int, days)
      - x_studio_last_purchase_price_validity_days (int, days)

    Three consumer sites read the row with
    `env['x_minimum_sales_margin'].search([], limit=1)` (no company
    filter — they rely on the model's record rule 638 to scope
    per-company at read time):

      - compute on account.payment.x_studio_payment_validation
      - server action 2427 'RR - Validate Payment %'
      - server action 2341 'SLS - Create Customer Payment'

    If a company has no row, all three degrade silently: the compute
    stays False (no warning banner), the validation action never
    raises, and the SO 'Create Customer Payment' button pre-fills
    Rs. 0.00. See MIGRATION notes for the full downstream trace.

    Why raw SQL, not create()
    -------------------------
    A Studio base.automation (id 146, server action 1776) runs on
    every ORM create() of this model and raises
        UserError('Only one Minimum Sales Margin % can exist.')
    whenever ANY x_studio_active=True row exists — regardless of
    company. That guard predates the multi-company setup and blocks
    any second row from being created via the ORM.

    Raw SQL INSERT bypasses ir.actions.server / base_automation
    entirely, so we can seed without touching the automation. The
    same idempotence-by-existence-check pattern used elsewhere in
    Fix-repair / BugFix-Sales applies: skip companies that already
    carry a row.
    """
    _name = 'bugfix_sales.minimum_sales_margin.seed'
    _description = 'Seed Minimum Sales Margin config per company'

    _DEFAULT_NAME = 'Sales Configurations'
    _DEFAULT_ADVANCE_PCT = 50.0
    _DEFAULT_MARGIN_PCT = 35.0
    _DEFAULT_SO_VALIDITY_DAYS = 1
    _DEFAULT_PURCHASE_VALIDITY_DAYS = 30

    @api.model
    def _seed_minimum_sales_margin_per_company(self):
        """Insert one x_minimum_sales_margin row for every active
        company that doesn't already have one. Idempotent — re-runs
        no-op when every company is already seeded.

        Defaults mirror the existing production row on company 1
        (Jinasena (Pvt) Ltd.) so the enforcement thresholds are
        consistent across the multi-company install. Individual
        companies can override their values later via the config
        form; the seed only touches rows it creates.
        """
        companies = self.env['res.company'].sudo().search([])
        if not companies:
            return

        self.env.cr.execute(
            "SELECT DISTINCT x_studio_company_id "
            "FROM x_minimum_sales_margin "
            "WHERE x_studio_company_id IS NOT NULL"
        )
        already = {row[0] for row in self.env.cr.fetchall()}
        missing = companies.filtered(lambda c: c.id not in already)
        if not missing:
            return

        uid = self.env.uid
        for company in missing:
            self.env.cr.execute(
                """
                INSERT INTO x_minimum_sales_margin (
                    x_name,
                    x_studio_advance_payment_,
                    x_studio_minimum_sales_margin_,
                    x_studio_sales_order_validity,
                    x_studio_last_purchase_price_validity_days,
                    x_studio_company_id,
                    x_active,
                    x_studio_active,
                    create_uid,
                    create_date,
                    write_uid,
                    write_date
                )
                VALUES (%s, %s, %s, %s, %s, %s, TRUE, TRUE, %s, NOW(), %s, NOW())
                """,
                (
                    self._DEFAULT_NAME,
                    self._DEFAULT_ADVANCE_PCT,
                    self._DEFAULT_MARGIN_PCT,
                    self._DEFAULT_SO_VALIDITY_DAYS,
                    self._DEFAULT_PURCHASE_VALIDITY_DAYS,
                    company.id,
                    uid,
                    uid,
                ),
            )

    @api.model
    def _migrate_to_config_parameter(self):
        """One-shot copy of each x_minimum_sales_margin row into
        ir.config_parameter under company-scoped keys.

        Purpose
        -------
        v21 moves the four Sales config values from the Studio
        catalogue model x_minimum_sales_margin (one row per company)
        to ir.config_parameter (per-company keys). res.company exposes
        computed proxy fields backed by those keys; res.config.settings
        binds them via `related`.

        This function preserves the current per-company values across
        the storage change:

          - For each x_minimum_sales_margin row, derive the four keys
            from res.company._BUGFIX_SALES_CONFIG.
          - For each key that does NOT yet exist in ir.config_parameter,
            copy the value across.
          - Existing keys are left alone — subsequent upgrades never
            overwrite a value the user has edited via Settings.

        The old catalogue rows are NOT touched. Studio server actions
        that still read env['x_minimum_sales_margin'].search(...) keep
        seeing the values they saw before the upgrade; those readers
        get migrated to env.company.x_studio_* in follow-up commits
        (they'll go stale relative to ir.config_parameter after the
        first Settings edit, per the accepted cutover plan).

        Idempotent — reruns find every key already present and no-op.
        """
        Icp = self.env['ir.config_parameter'].sudo()
        IcpModel = self.env['ir.config_parameter'].sudo()
        rows = self.env['x_minimum_sales_margin'].sudo().search([])
        if not rows:
            return
        # Import the mapping from res.company so field-name / key-base
        # pairs stay in lockstep with the reader side. Model may not
        # have been registered yet on the very first install pass; the
        # data XML calls this AFTER models are loaded, so the lookup
        # is safe here.
        keymap = self.env['res.company']._BUGFIX_SALES_CONFIG
        for row in rows:
            company = row.x_studio_company_id
            if not company:
                continue
            for fname, (key_base, _ttype, _default) in keymap.items():
                param_key = '%s.%s' % (key_base, company.id)
                # Use a direct search so we can distinguish "key
                # exists with value 0" from "key missing". get_param
                # returns False for both cases.
                existing = IcpModel.search(
                    [('key', '=', param_key)], limit=1,
                )
                if existing:
                    continue
                Icp.set_param(param_key, str(row[fname]))

    _C01_REPORT_NAME = 'C01 Sales Quotation'
    _C01_INHERIT_XMLID = 'bugfix_sales_c01_quotation_intro_conclusion'
    _C01_INHERIT_ARCH = (
        '<data>'
        '<xpath expr="//table[hasclass(\'table-sm\')][1]" position="before">'
        '<div t-if="doc.bugfix_sales_intro_text" class="mt-3 mb-3" '
        'style="white-space: pre-wrap; font-size: 10pt;">'
        '<strong>Notes:</strong><br/>'
        '<t t-out="doc.bugfix_sales_intro_text"/>'
        '</div>'
        '</xpath>'
        '<xpath expr="//table[hasclass(\'table-sm\')][2]" position="after">'
        '<div t-if="doc.bugfix_sales_conclusion_text" class="mt-3 mb-3" '
        'style="white-space: pre-wrap; font-size: 10pt;">'
        '<t t-out="doc.bugfix_sales_conclusion_text"/>'
        '</div>'
        '</xpath>'
        '</data>'
    )

    @api.model
    def _attach_c01_intro_conclusion_view(self):
        """Attach the Document Introduction / Conclusion QWeb overlay to
        the Studio 'C01 Sales Quotation' report's _document sub-template.

        Prior to v20 this was a static <template inherit_id="..."> in
        report/c01_sales_quotation.xml. The inherit_id was Studio's
        per-database UUID xml_id — which exists only on the database
        where Studio generated it. Any other instance (v17-final,
        production, a fresh dev DB) would fail module install with:

          ValueError: External ID not found in the system:
              studio_customization.studio_customization_<uuid>

        Now the inheritance is resolved dynamically:

          1. Find ir.actions.report where name = 'C01 Sales Quotation'
             and model = 'sale.order'. If absent → skip silently.
          2. Take the report's `report_name` field (module-scoped key
             of the outer QWeb template) and derive the _document
             sub-template's key by inserting '_document' at the
             '_copy' boundary. Studio's naming convention:
                report_name: studio_customization.studio_report_docume_
                             <uuid>_copy_1_copy_4_...
                doc key:     studio_customization.studio_report_docume_
                             <uuid>_document_copy_1_copy_4_...
             When no '_copy' segments exist, append '_document'.
          3. Look up the ir.ui.view with that key. If not found →
             skip silently.
          4. Create or update our inherit view, keyed under
             bugfix_sales.<self._C01_INHERIT_XMLID>. Reversal path:
             if a prior run created the view but C01 has since been
             removed from this database, unlink the stale view.

        Idempotent — reruns with unchanged state no-op.
        """
        Report = self.env['ir.actions.report'].sudo()
        View = self.env['ir.ui.view'].sudo()
        Data = self.env['ir.model.data'].sudo()

        existing = View.search([
            ('key', '=', 'bugfix_sales.' + self._C01_INHERIT_XMLID),
        ], limit=1)

        report = Report.search([
            ('name', '=', self._C01_REPORT_NAME),
            ('model', '=', 'sale.order'),
        ], limit=1)
        if not report:
            if existing:
                existing.unlink()
            return

        rname = report.report_name or ''
        if '.' not in rname:
            if existing:
                existing.unlink()
            return

        module_prefix, tail = rname.split('.', 1)
        if '_copy' in tail:
            idx = tail.index('_copy')
            doc_tail = tail[:idx] + '_document' + tail[idx:]
        else:
            doc_tail = tail + '_document'
        doc_key = '%s.%s' % (module_prefix, doc_tail)

        target = View.search([
            ('key', '=', doc_key),
            ('type', '=', 'qweb'),
        ], limit=1)
        if not target:
            if existing:
                existing.unlink()
            return

        if existing:
            updates = {}
            if existing.inherit_id.id != target.id:
                updates['inherit_id'] = target.id
            if (existing.arch_db or '').strip() != self._C01_INHERIT_ARCH.strip():
                updates['arch'] = self._C01_INHERIT_ARCH
            if updates:
                existing.write(updates)
            return

        new_view = View.create({
            'name': 'BugFix-Sales: C01 Quotation Intro/Conclusion',
            'type': 'qweb',
            'inherit_id': target.id,
            'mode': 'extension',
            'arch': self._C01_INHERIT_ARCH,
            'key': 'bugfix_sales.' + self._C01_INHERIT_XMLID,
        })
        Data.create({
            'module': 'bugfix_sales',
            'name': self._C01_INHERIT_XMLID,
            'model': 'ir.ui.view',
            'res_id': new_view.id,
            'noupdate': True,
        })

    @api.model
    def _cleanup_orphan_studio_menu_pins(self):
        """Unlink ir.model.data rows owned by studio_customization
        whose target ir.ui.menu no longer exists.

        Context: when v18 flipped the two Studio-generated 'Sales
        Configurations' menus to active=False, something outside
        this module (most likely Studio's own on-upgrade housekeeping
        pass on the studio_customization module) hard-deleted the
        menu records shortly afterwards. Odoo normally cleans up an
        ir.model.data pin in the same transaction as its target's
        unlink, but that cascade missed here — leaving two dangling
        pins pointing at res_ids 904 and 1867 which no longer resolve
        to anything.

        These pins are harmless (env.ref() returns empty, no code
        reads them) but they clutter ir.model.data. Sweep them out.

        Scope kept deliberately narrow: only pins on ir.ui.menu owned
        by studio_customization. Doesn't touch pins on other models
        or from other modules, so unrelated Studio-owned records stay
        untouched.

        Idempotent: reruns find no orphans and no-op.
        """
        Data = self.env['ir.model.data'].sudo()
        Menu = self.env['ir.ui.menu'].sudo().with_context(active_test=False)
        pins = Data.search([
            ('module', '=', 'studio_customization'),
            ('model', '=', 'ir.ui.menu'),
        ])
        if not pins:
            return
        orphans = pins.filtered(
            lambda p: not Menu.browse(p.res_id).exists()
        )
        if orphans:
            orphans.unlink()

    @api.model
    def _hide_minimum_sales_margin_menus(self):
        """Deactivate every menu that opens the Studio-generated
        list/form view for x_minimum_sales_margin.

        Since v17 the four config values are edited from
        Settings → Sales via res.config.settings; the standalone
        Sales Configurations list view is redundant and confusing
        (users could accidentally create a second row and either
        hit automation 146's guard or bypass per-company scoping).

        Finds menus by walking `ir.actions.act_window` on
        res_model='x_minimum_sales_margin' — so any menu Studio may
        add in the future (e.g. from a duplicate app configuration)
        also gets caught on the next upgrade. Model / actions / views
        / rows are all preserved: only menu visibility changes, so
        the migration is reversible (chatter shows the flip; a user
        can set active=True from Developer Mode if ever needed).

        Idempotent: reruns find no still-active menus and no-op.
        """
        ActWindow = self.env['ir.actions.act_window'].sudo()
        actions = ActWindow.search(
            [('res_model', '=', 'x_minimum_sales_margin')]
        )
        if not actions:
            return
        Menu = self.env['ir.ui.menu'].sudo().with_context(active_test=False)
        refs = ['ir.actions.act_window,%s' % a.id for a in actions]
        menus = Menu.search([('action', 'in', refs)])
        active_menus = menus.filtered(lambda m: m.active)
        if active_menus:
            active_menus.write({'active': False})
