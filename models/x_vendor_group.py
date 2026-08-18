# -*- coding: utf-8 -*-
from odoo import fields, models


class XVendorGroup(models.Model):
    """Studio-ported custom model x_vendor_group."""
    _name = 'x_vendor_group'
    _description = 'Vendor Group'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Code')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_one2many_field_5cEfV = fields.One2many('res.partner', 'TODO_inverse', string='Vendors')
    x_studio_payable_account = fields.Many2one('account.account', string='Payable Account')
    x_studio_payment_term = fields.Many2one('account.payment.term', string='Payment Term')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_x_studio_vendor_group__res_partner_count = fields.Integer(string='Vendor Group count', store=False)
