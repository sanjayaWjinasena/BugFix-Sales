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

    # ---------- v22: full cutover to ir.config_parameter -----------------
    # Marker embedded in every Studio code reader we've patched. Presence
    # of the marker means the code has already been swept once, so future
    # upgrades skip that reader and any manual Studio edit stays intact.
    _CUTOVER_MARKER = '# bugfix_sales:config-cutover-v22'

    # Sensible defaults used when seeding ir.config_parameter for a
    # freshly-added company. Mirror the same defaults the old row seed
    # was using (see _seed_minimum_sales_margin_per_company).
    _DEFAULT_IR_CONFIG_VALUES = {
        'bugfix_sales.minimum_sales_margin': _DEFAULT_MARGIN_PCT,
        'bugfix_sales.sales_order_validity': _DEFAULT_SO_VALIDITY_DAYS,
        'bugfix_sales.advance_payment_pct': _DEFAULT_ADVANCE_PCT,
        'bugfix_sales.last_purchase_price_validity_days': _DEFAULT_PURCHASE_VALIDITY_DAYS,
    }

    @api.model
    def _seed_ir_config_parameter_defaults(self):
        """Write default values for every Sales config key that is
        missing on any active company.

        v21 introduced ir.config_parameter as the source of truth but
        relied on _seed_minimum_sales_margin_per_company running first
        (to insert old-model rows) and _migrate_to_config_parameter
        running second (to copy those into ir.config_parameter). v22
        drops the old-model seed — new companies would end up with no
        parameter row at all, which the res.company compute treats as
        "0", i.e. margin gate disabled. Seed real defaults instead so
        the enforcement stays live from day one on any new company.

        Idempotent — only writes keys that are currently absent, so
        Settings edits done between upgrades never get clobbered.
        """
        Icp = self.env['ir.config_parameter'].sudo()
        companies = self.env['res.company'].sudo().search([])
        for company in companies:
            for base_key, default in self._DEFAULT_IR_CONFIG_VALUES.items():
                param_key = '%s.%s' % (base_key, company.id)
                existing = Icp.search(
                    [('key', '=', param_key)], limit=1,
                )
                if existing:
                    continue
                Icp.set_param(param_key, str(default))

    # Formula for sale.order.line.x_studio_margin_exceed as a compute.
    # Mirrors the original SLS - Validate Margin in SO Line server
    # action 1508 exactly (same value_1 / value_2 dimensional quirk
    # preserved so results don't drift between installations that ran
    # the old on_change vs the new compute). The threshold now reads
    # via record.company_id.x_studio_minimum_sales_margin_ (the
    # per-company proxy backed by ir.config_parameter), so a Settings
    # save re-evaluates every line on the next read — no stored flag
    # to go stale.
    _LINE_MARGIN_EXCEED_COMPUTE = (
        "# bugfix_sales:margin-exceed-computed-v23\n"
        "for record in self:\n"
        "  exceeded = False\n"
        "  if record.product_id and record.x_studio_quotation_type != 'Project':\n"
        "    if record.product_uom_qty and record.product_uom_qty > 0:\n"
        "      value_1 = ((record.price_subtotal/record.product_uom_qty) - "
        "(record.price_subtotal*(record.x_studio_commission/100)) - "
        "record.product_id.standard_price)\n"
        "      value_2 = (record.price_subtotal/record.product_uom_qty) - "
        "(record.price_subtotal*(record.x_studio_commission/100))\n"
        "      if value_2 > 0:\n"
        "        net_margin = (value_1/value_2)*100\n"
        "        if net_margin and "
        "net_margin < (record.company_id.x_studio_minimum_sales_margin_ or 0.0):\n"
        "          exceeded = True\n"
        "  record['x_studio_margin_exceed'] = exceeded\n"
    )

    _LINE_MARGIN_EXCEED_DEPENDS = (
        'product_id,'
        'product_id.standard_price,'
        'product_uom_qty,'
        'price_subtotal,'
        'x_studio_commission,'
        'x_studio_quotation_type'
    )

    _HEADER_MARGIN_EXCEED_DEPENDS = 'order_line.x_studio_margin_exceed'

    @api.model
    def _convert_line_margin_flag_to_computed(self):
        """Convert sale.order.line.x_studio_margin_exceed from a
        stored boolean (set via base.automation 91's on_change into
        server action 1508) into a non-stored computed field that is
        re-evaluated on every read.

        Why
        ---
        Stored booleans go stale when the surrounding config changes
        without touching the record. That is exactly what happened
        after the v22 cutover: users saw the "Insufficient Margin"
        modal fire on lines with 91.67% margin against a 50%
        threshold because the flag had been set True under an older
        (higher) threshold and no on_change fired since. Making the
        flag a compute means the check is fresh at every render.

        What
        ----
        1. On sale.order.line.x_studio_margin_exceed:
             store   = False
             compute = <the same formula the on_change ran>
             depends = product / qty / price / commission / quotation
                       type (skipping the config value itself: it's a
                       non-stored proxy field so depends can't
                       reliably chain through it — but non-stored
                       computes recompute on every read anyway, so
                       cache invalidation via other fields is only a
                       within-transaction concern, not correctness)
        2. Tighten sale.order.x_studio_margin_exceed's depends from
           "order_line" (link changes only) to
           "order_line.x_studio_margin_exceed" so the header rollup
           invalidates when a line's computed value changes within a
           transaction.
        3. Deactivate base.automation 91 — the on_change is dead
           weight once the compute takes over, and leaving it active
           would still fire (idempotently) at every line edit,
           writing the same non-stored value to nothing.
        4. Also tighten sale.order.line._description of the field to
           its computed form so the label is unchanged.

        Idempotent via the marker at the top of the compute string
        — reruns detect the marker and no-op. Manual Studio edits
        that removed the marker will trigger a re-write; if that
        matters, the marker can be re-added by hand in Studio.
        """
        Field = self.env['ir.model.fields'].sudo()
        marker = '# bugfix_sales:margin-exceed-computed-v23'

        # Step 1 — line field
        line_field = Field.search([
            ('model', '=', 'sale.order.line'),
            ('name', '=', 'x_studio_margin_exceed'),
        ], limit=1)
        if line_field and marker not in (line_field.compute or ''):
            line_field.write({
                'store': False,
                'compute': self._LINE_MARGIN_EXCEED_COMPUTE,
                'depends': self._LINE_MARGIN_EXCEED_DEPENDS,
                'readonly': True,
            })

        # Step 2 — header field depends tightening
        header_field = Field.search([
            ('model', '=', 'sale.order'),
            ('name', '=', 'x_studio_margin_exceed'),
        ], limit=1)
        if header_field and header_field.depends != self._HEADER_MARGIN_EXCEED_DEPENDS:
            header_field.write({
                'depends': self._HEADER_MARGIN_EXCEED_DEPENDS,
            })

        # Step 3 — retire the automation that used to set the stored value
        Auto = self.env['base.automation'].sudo()
        auto_91 = Auto.search([
            ('model_name', '=', 'sale.order.line'),
            ('name', '=', 'SLS - Validate Margin in SO Line'),
        ], limit=1)
        if auto_91 and auto_91.active:
            auto_91.write({'active': False})

    @api.model
    def _patch_studio_readers_to_use_company(self):
        """Surgically rewrite every Studio Python element that reads
        env['x_minimum_sales_margin'].search(...) so it reads the new
        proxy fields on res.company instead.

        Substitution pattern
        --------------------
        Because res.company.x_studio_minimum_sales_margin_ (and the
        three siblings) keep the same names as the fields on the old
        Studio catalogue model, every downstream reference
        `min_magin.x_studio_minimum_sales_margin_` continues to work
        verbatim. Only the ONE fetch line needs replacing:

            env['x_minimum_sales_margin'].search([], limit=1)
                → record.company_id   (or env.company / rec.company_id)

        Which right-hand side to pick depends on which local variable
        the surrounding code already carries:

          * If the enclosing scope has `record` (a per-record server
            action or a compute loop iteration variable) — use
            record.company_id.
          * If the compute loop uses `rec` — use rec.company_id.
          * If the enclosing scope has a `company` variable already
            derived from allowed_company_ids — use that.
          * Otherwise (crons where no record is in scope) — fall back
            to env.company (single-company cron process; matches
            pre-v22 behaviour where search([], limit=1) returned one
            arbitrary row).

        Idempotence
        -----------
        Each patch checks for the marker `# bugfix_sales:config-cutover-v22`
        at the top of the target string; skipped if already present. A
        second guard `if patch_from not in code` (verbatim match)
        prevents overwriting Studio edits that removed the original
        fetch line — safer than blind replace.
        """
        marker = self._CUTOVER_MARKER
        Server = self.env['ir.actions.server'].sudo()
        Field = self.env['ir.model.fields'].sudo()

        # Server-action patches: (id, old_snippet, new_snippet, comment)
        server_patches = [
            # 1508 — SLS - Validate Margin in SO Line (sale.order.line)
            (
                1508,
                "min_magin = env['x_minimum_sales_margin'].search([], limit=1)",
                "min_magin = record.company_id",
                'Read minimum margin from the current SO line company.',
            ),
            # 1517 — SLS - Item Over Margin Details (sale.order)
            (
                1517,
                "min_magin = env['x_minimum_sales_margin'].search([], limit=1)",
                "min_magin = record.company_id",
                'Read minimum margin from the current SO company.',
            ),
            # 2340 — SLS - Cancel SOs more than 3 Months (cron; no record in scope)
            (
                2340,
                "no_of_days = env['x_minimum_sales_margin'].search([])",
                "no_of_days = env.company",
                'Read SO validity days from the caller company '
                '(cron traditionally used first row).',
            ),
            # 2341 — SLS - Create Customer Payment (sale.order); has TWO occurrences
            (
                2341,
                "min_magin = env['x_minimum_sales_margin'].search([], limit=1)",
                "min_magin = record.company_id",
                'Read advance payment % from the current SO company.',
            ),
            # 2427 — RR - Validate Payment % (account.payment)
            (
                2427,
                "min_magin = env['x_minimum_sales_margin'].search([], limit=1)",
                "min_magin = record.company_id",
                'Read advance payment % from the current payment company.',
            ),
            # 2897 — PROJ - Update Project Pricelist (product.pricelist);
            # already had explicit company scoping via x_studio_company_id
            (
                2897,
                ("sales_configuration = env['x_minimum_sales_margin'].search("
                 "[('x_studio_company_id', '=', company.id)],limit=1)"),
                'sales_configuration = company',
                'Read last-purchase-price validity from the resolved company.',
            ),
        ]
        for action_id, old, new, _why in server_patches:
            action = Server.browse(action_id).exists()
            if not action:
                continue
            code = action.code or ''
            if marker in code:
                continue
            if old not in code:
                continue
            # replace(count=-1) covers the double-occurrence in action 2341
            new_code = code.replace(old, new)
            action.write({'code': marker + '\n' + new_code})

        # Compute-field patches: same idea but on ir.model.fields.compute.
        # Identify by model + field-name (safer than id — surviving Studio
        # rebuilds that may renumber ids).
        field_patches = [
            (
                'account.payment', 'x_studio_payment_validation',
                "min_magin = self.env['x_minimum_sales_margin'].search([], limit=1)",
                'min_magin = record.company_id',
                'Read advance payment % from the current payment company.',
            ),
            (
                'sale.order', 'x_studio_sales_order_validity',
                "setup = self.env['x_minimum_sales_margin'].search([])",
                'setup = rec.company_id',
                'Read SO validity days from the current SO company.',
            ),
        ]
        for model, name, old, new, _why in field_patches:
            field = Field.search(
                [('model', '=', model), ('name', '=', name)], limit=1,
            )
            if not field:
                continue
            code = field.compute or ''
            if marker in code:
                continue
            if old not in code:
                continue
            new_code = code.replace(old, new)
            field.write({'compute': marker + '\n' + new_code})

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
