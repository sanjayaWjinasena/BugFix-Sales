# -*- coding: utf-8 -*-
from odoo import models, fields

class XMinimumSalesMarginGap(models.Model):
    _inherit = 'x_minimum_sales_margin'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
