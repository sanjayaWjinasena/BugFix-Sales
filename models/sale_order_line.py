# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Ported from Studio (v33). Consumed by BugFix-Sales' account-mandatory
    # gate on the parent sale.order (mirrored per-line).
    x_studio_account_mandatory = fields.Boolean(
        string='Account Mandatory',
    )
