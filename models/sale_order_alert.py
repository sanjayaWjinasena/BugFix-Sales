# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderAlert(models.Model):
    _inherit = 'sale.order.alert'

    x_studio_char_field_dpQHc = fields.Char(string='New Text', store=False)
    x_studio_comments = fields.Char(string='Comments', store=False)
    x_studio_selection_field_ogQSe = fields.Selection([], string='New Selection', store=False)
    x_studio_status = fields.Selection([], string='Status', store=False)
