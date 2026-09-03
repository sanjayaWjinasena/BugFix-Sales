# -*- coding: utf-8 -*-
"""x_delivery_terms - also declared in BugFix-Purchase (canonical owner).
Both modules use _name (not _inherit); Odoo merges declarations at runtime.

v0.1.0.57: removed x_studio_delivery_terms_id O2M from this declaration.
The O2M points to x_delivery_term_charge which is only declared in
BugFix-Purchase. Declaring the O2M here would force BugFix-Sales to
depend on BugFix-Purchase to resolve the comodel at setup, which
created the 3-way cycle Sales -> Purchase -> Accounting -> Sales.

BugFix-Purchase's declaration keeps the O2M and loads AFTER Sales.
Since Purchase loads last for this model, its class definition wins
and the O2M is present on the merged x_delivery_terms model at
runtime. Field sets don't need to match for _name-mirror models."""
from odoo import fields, models


class XDeliveryTerms(models.Model):
    _name = 'x_delivery_terms'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Delivery Terms'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Delivery Term')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_copied = fields.Boolean(string='Copied')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_vendor_despatch = fields.Boolean(string='Vendor Dispatch Voucher')
