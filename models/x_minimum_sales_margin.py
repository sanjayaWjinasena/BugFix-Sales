# -*- coding: utf-8 -*-
from odoo import models, fields

class X_minimum_sales_margin(models.Model):
    _name = 'x_minimum_sales_margin'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Minimum Sales Margin %'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_active = fields.Boolean(string='Active')
    x_studio_advance_payment_ = fields.Float(string='Advance Payment %')
    x_studio_company_id = fields.Many2one(comodel_name='res.company', string='Company')
    x_studio_last_purchase_price_validity_days = fields.Integer(string='Last Purchase Price Validity (Days)')
    x_studio_minimum_sales_margin_ = fields.Float(string='Minimum Sales Margin %')
    x_studio_sales_order_validity = fields.Integer(string='Sales Order Validity (Days)')
    x_studio_sequence = fields.Integer(string='Sequence')
