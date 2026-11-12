# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """Bind the four Sales-workflow config values into Settings → Sales.

    Storage lives in ir.config_parameter (per-company keys) — see
    res_company._BUGFIX_SALES_CONFIG for the key format. On this
    transient model each field is `related` to the same-name proxy
    field on res.company, so Odoo's standard settings pipeline
    (get_values / set_values) is automatic:

      * Opening Settings → Sales computes each proxy field on
        env.company (reads from ir.config_parameter).
      * Clicking Save writes back through the proxy's inverse, which
        writes to ir.config_parameter.

    No get_values / set_values override needed. Field names match the
    legacy x_studio_* names on both res.company and the old Studio
    catalogue model, so view arch and consumer code that already
    references either place keeps working with zero changes.

    Predecessor (v20) held stored fields on this transient and
    hand-rolled get_values / set_values to sync with rows on the
    x_minimum_sales_margin Studio catalogue (including raw-SQL
    INSERTs to bypass automation 146's cross-company single-row
    guard). All of that goes away — Odoo's related-field write path
    on res.company covers it cleanly.
    """
    _inherit = 'res.config.settings'

    x_studio_minimum_sales_margin_ = fields.Float(
        related='company_id.x_studio_minimum_sales_margin_',
        readonly=False,
    )
    x_studio_advance_payment_ = fields.Float(
        related='company_id.x_studio_advance_payment_',
        readonly=False,
    )
    x_studio_sales_order_validity = fields.Integer(
        related='company_id.x_studio_sales_order_validity',
        readonly=False,
    )
    x_studio_last_purchase_price_validity_days = fields.Integer(
        related='company_id.x_studio_last_purchase_price_validity_days',
        readonly=False,
    )
