# -*- coding: utf-8 -*-
"""Studio field ports for sale.order.alert (auto-ported from CDB)."""
from odoo import fields, models


class XSaleOrderAlertExt(models.Model):
    _inherit = 'sale.order.alert'

    x_studio_char_field_dpQHc = fields.Char(string='New Text')
    x_studio_comments = fields.Char(string='Comments')
    x_studio_selection_field_ogQSe = fields.Selection([], string='New Selection')
    x_studio_status = fields.Selection([], string='Status')
