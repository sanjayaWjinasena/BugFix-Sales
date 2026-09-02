# -*- coding: utf-8 -*-
"""x_delivery_terms - also declared in BugFix-Purchase. Both modules use
_name (not _inherit); Odoo merges the two declarations but the later-loaded
one's field list REPLACES the earlier one's, so field sets MUST match to
avoid runtime shadowing. Purchase v0.1.0.33 shipped x_studio_delivery_terms_id
O2M pointing to x_delivery_term_charge; Sales v0.1.0.55 mirrors that
declaration + default=True on x_active."""
from odoo import fields, models


class XDeliveryTerms(models.Model):
    _name = 'x_delivery_terms'
    _description = 'Delivery Terms'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Delivery Term')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_copied = fields.Boolean(string='Copied')
    x_studio_delivery_terms_id = fields.One2many(
        'x_delivery_term_charge', 'x_studio_delivery_terms_id',
        string='Charges')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_vendor_despatch = fields.Boolean(string='Vendor Dispatch Voucher')
