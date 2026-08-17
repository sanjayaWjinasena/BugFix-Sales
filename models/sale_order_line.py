# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Ported from Studio (v33). Consumed by BugFix-Sales' account-mandatory
    # gate on the parent sale.order (mirrored per-line).
    x_studio_account_mandatory = fields.Boolean(
        string='Account Mandatory',
    )
    # v43: original line price captured by Fix-repair's RUG-repricing
    # logic (sale_order_line.py's create/write override on Fix-repair
    # v279+). Studio also uses this field to restore the customer-facing
    # price if RUG is later rejected. Declared here so BugFix-Sales
    # owns the schema (single home for sale.order.line Studio fields);
    # Fix-repair reads/writes via the same field name.
    x_studio_price_unit_original = fields.Float(
        string='Price Unit Original',
    )
