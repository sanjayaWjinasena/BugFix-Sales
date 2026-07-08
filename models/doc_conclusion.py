# -*- coding: utf-8 -*-
from odoo import fields, models


class BugFixSalesDocConclusion(models.Model):
    """Library of reusable conclusion blocks (Availability, Terms of
    Payment, Delivery, Guarantee, closing salutation …) for the
    printed Quotation. Same shape as bugfix_sales.doc_intro; kept as a
    separate model so the two lookups on sale.order are unambiguous
    and the config menu labels stay clear.
    """
    _name = 'bugfix_sales.doc_conclusion'
    _description = 'Quotation Document Conclusion'
    _order = 'name'

    name = fields.Char(string='Title', required=True, index=True)
    description = fields.Text(
        string='Conclusion Text', required=True,
        help='Multi-line body printed after the totals on the quotation.',
    )
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company,
    )
    active = fields.Boolean(default=True)
