# -*- coding: utf-8 -*-
"""Studio field ports for product.pricelist.item (auto-ported from CDB)."""
from odoo import fields, models


class XProductPricelistItemExt(models.Model):
    _inherit = 'product.pricelist.item'

    x_studio_price_confirmed = fields.Boolean(string='Price Confirmed')
