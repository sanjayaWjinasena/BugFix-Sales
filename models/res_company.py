# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):
    """Per-company Sales config, stored in ir.config_parameter.

    The four Sales-workflow configuration values (minimum sales margin,
    advance payment %, SO validity, last-purchase-price validity) live
    in ir.config_parameter under company-scoped keys:

        bugfix_sales.minimum_sales_margin.<company_id>
        bugfix_sales.sales_order_validity.<company_id>
        bugfix_sales.advance_payment_pct.<company_id>
        bugfix_sales.last_purchase_price_validity_days.<company_id>

    Storage rationale
    -----------------
    Before v21, these values lived on the Studio-manual catalogue model
    x_minimum_sales_margin (one row per company). That worked but felt
    off — configuration values are conceptually a res.config.settings
    concern, not a business-data model. The Studio catalogue also
    complicated menu UX (list-view editing, automation 146's
    single-row-per-company guard) and pinned itself to Studio's
    lifecycle.

    ir.config_parameter is Odoo's standard config store. Making these
    values per-company just means encoding company_id in the key. No
    new columns on res_company, no dependence on Studio.

    Access surface
    --------------
    Callers still read via the familiar
        self.env.company.x_studio_minimum_sales_margin_
    pattern — the fields on this class are computed/inverse proxies
    that transparently proxy to ir.config_parameter. Same field names
    as the Studio catalogue so any Python or view expression that
    already references either place keeps working. Compute is
    non-stored (no columns added to res_company); Odoo's per-txn
    cache handles read amortisation.

    Transitional dual-storage
    -------------------------
    The old x_minimum_sales_margin rows are preserved (per the
    "never delete x_ data" rule). Studio server actions that read
    env['x_minimum_sales_margin'].search([], limit=1) continue to see
    the seeded row values — they'll go stale relative to the
    ir.config_parameter source-of-truth after the first Settings edit,
    but that's the accepted cutover point. Each remaining consumer
    gets migrated to env.company.x_studio_* in follow-up commits.
    """
    _inherit = 'res.company'

    # Ordering — key_base, python_type, default when missing.
    # Kept as a class-level constant so _migrate_to_config_parameter in
    # minimum_sales_margin_seed can reuse the exact same mapping.
    _BUGFIX_SALES_CONFIG = {
        'x_studio_minimum_sales_margin_':
            ('bugfix_sales.minimum_sales_margin', float, 0.0),
        'x_studio_sales_order_validity':
            ('bugfix_sales.sales_order_validity', int, 0),
        'x_studio_advance_payment_':
            ('bugfix_sales.advance_payment_pct', float, 0.0),
        'x_studio_last_purchase_price_validity_days':
            ('bugfix_sales.last_purchase_price_validity_days', int, 0),
    }

    x_studio_minimum_sales_margin_ = fields.Float(
        string='Minimum Sales Margin %',
        compute='_compute_bugfix_sales_config',
        inverse='_inverse_bugfix_sales_config',
        store=False,
        help='Minimum margin percentage enforced on Sales / Project '
             'quotations at the Confirm gate.',
    )
    x_studio_sales_order_validity = fields.Integer(
        string='Sales Order Validity (Days)',
        compute='_compute_bugfix_sales_config',
        inverse='_inverse_bugfix_sales_config',
        store=False,
        help='How many days a quotation remains valid before it is '
             'flagged expired on the Confirm gate.',
    )
    x_studio_advance_payment_ = fields.Float(
        string='Advance Payment %',
        compute='_compute_bugfix_sales_config',
        inverse='_inverse_bugfix_sales_config',
        store=False,
        help='Minimum advance-payment percentage required before '
             'deliveries can be validated on non-RUG repair sale '
             'orders.',
    )
    x_studio_last_purchase_price_validity_days = fields.Integer(
        string='Last Purchase Price Validity (Days)',
        compute='_compute_bugfix_sales_config',
        inverse='_inverse_bugfix_sales_config',
        store=False,
        help="Age limit (days) before a product's last purchase price "
             "is considered stale.",
    )

    def _compute_bugfix_sales_config(self):
        """Read all four values from ir.config_parameter for each company.

        Single method covering four fields — Odoo will call it once
        per recordset when any of the four is accessed, then cache
        every value for the rest of the transaction. Fields with no
        stored key fall back to the type-default (0 / 0.0).
        """
        Icp = self.env['ir.config_parameter'].sudo()
        for company in self:
            for fname, (key_base, ttype, default) in self._BUGFIX_SALES_CONFIG.items():
                raw = Icp.get_param('%s.%s' % (key_base, company.id))
                if raw:
                    try:
                        company[fname] = ttype(raw)
                    except (TypeError, ValueError):
                        company[fname] = default
                else:
                    company[fname] = default

    def _inverse_bugfix_sales_config(self):
        """Persist all four values back to ir.config_parameter.

        Odoo calls the inverse after the write() has populated the
        cache — including any fields the caller didn't touch (those
        return their current computed value, so writing them back is
        a no-op). Storing everything unconditionally keeps this simple;
        the cost is four set_param calls per config write, which are
        negligible at Settings-page edit frequency.
        """
        Icp = self.env['ir.config_parameter'].sudo()
        for company in self:
            for fname, (key_base, _ttype, _default) in self._BUGFIX_SALES_CONFIG.items():
                Icp.set_param(
                    '%s.%s' % (key_base, company.id),
                    str(company[fname]),
                )
