# -*- coding: utf-8 -*-
from odoo import fields, models


class XCustomerGroup(models.Model):
    """Studio-ported custom model x_customer_group."""
    _name = 'x_customer_group'
    _description = 'Customer Group'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Code')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_group_type = fields.Selection([], string='Group Type')
    x_studio_one2many_field_hfDGm = fields.One2many('res.partner', 'TODO_inverse', string='Customers')
    x_studio_payment_term = fields.Many2one('account.payment.term', string='Payment Term')
    x_studio_receivable_account = fields.Many2one('account.account', string='Receivable Account')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_x_studio_customer_group__res_partner_count = fields.Integer(string='Customer Group count', store=False)
