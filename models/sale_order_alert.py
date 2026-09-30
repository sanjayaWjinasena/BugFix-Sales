# -*- coding: utf-8 -*-
"""Studio fields on sale.order.alert (sale_subscription addon).

CDB Studio added 4 fields to the sale.order.alert model from the
sale_subscription addon. Two are text (Char), two are Selection with
empty option lists on CDB (Studio-created but never populated with
options — kept portable for schema parity).
"""
from odoo import fields, models


class SaleOrderAlert(models.Model):
    _inherit = 'sale.order.alert'

    x_studio_char_field_dpQHc = fields.Char(string='New Text', copy=True)
    x_studio_comments = fields.Char(string='Comments', copy=True)
    x_studio_selection_field_ogQSe = fields.Selection(
        selection=[],
        string='New Selection',
        copy=True,
    )
    x_studio_status = fields.Selection(
        selection=[],
        string='Status',
        copy=True,
    )
