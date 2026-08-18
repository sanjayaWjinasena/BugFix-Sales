# -*- coding: utf-8 -*-
from odoo import fields, models


class XDeliveryTerms(models.Model):
    """Studio-ported custom model x_delivery_terms."""
    _name = 'x_delivery_terms'
    _description = 'Delivery Terms'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Delivery Term')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_copied = fields.Boolean(string='Copied')
    # TODO: x_studio_delivery_terms_id = fields.One2many(...) -- Studio inverse name unknown; port from Clear-DB manually.
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_vendor_despatch = fields.Boolean(string='Vendor Dispatch Voucher')
