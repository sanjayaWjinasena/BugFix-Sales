# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    # v46: Studio fields ported from Clear-DB. Read by customer-group
    # -> pricelist resolution logic on sale.order line creation. The
    # values (General/Distributor/Dealer, Cash/Credit) mirror
    # sale.order.x_studio_quotation_type / customer_group.x_studio_group_type
    # so the accounts team can filter pricelists by segment when
    # setting the SO pricelist manually.
    x_studio_group_type = fields.Selection(
        selection=[
            ('General', 'General'),
            ('Distributor', 'Distributor'),
            ('Dealer', 'Dealer'),
        ],
        string='Group Type',
    )
    x_studio_order_payment_method = fields.Selection(
        selection=[
            ('Cash', 'Cash'),
            ('Credit', 'Credit'),
        ],
        string='Order Payment Method',
    )
    x_studio_project_price_list = fields.Boolean(
        string='Project Price List',
    )
    # x_studio_zzzz: legacy Studio field, kept for schema parity so
    # seeded pricelist rows from Clear-DB write cleanly.
    x_studio_zzzz = fields.Selection(
        selection=[
            ('0', 'Normal'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Very High'),
        ],
        string='zzzz',
    )
