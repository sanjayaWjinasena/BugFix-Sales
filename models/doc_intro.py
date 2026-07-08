# -*- coding: utf-8 -*-
from odoo import fields, models


class BugFixSalesDocIntro(models.Model):
    """Library of reusable introduction blocks for the printed
    Quotation. Salespeople pick one on the SO header; the block's
    description is copied into an editable text field on the SO so any
    per-order tweaks don't mutate the library entry.
    """
    _name = 'bugfix_sales.doc_intro'
    _description = 'Quotation Document Introduction'
    _order = 'name'

    name = fields.Char(string='Title', required=True, index=True)
    description = fields.Text(
        string='Introduction Text', required=True,
        help='Multi-line body printed at the top of the quotation.',
    )
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company,
    )
    active = fields.Boolean(default=True)
