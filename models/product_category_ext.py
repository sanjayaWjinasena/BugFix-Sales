# -*- coding: utf-8 -*-
"""Studio field ports for product.category (auto-ported from CDB)."""
from odoo import fields, models


class XProductCategoryExt(models.Model):
    _inherit = 'product.category'

    x_studio_company_id = fields.Many2one('res.company', string='Company', ondelete='set null', domain='[]')
    x_studio_description = fields.Char(string='Description')
