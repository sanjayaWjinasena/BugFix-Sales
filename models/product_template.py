# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # ---- Studio-ported x_studio_* fields (v0.1.0.58) ----
    x_studio_binary_field_lN2B8 = fields.Binary(string='New File')
    x_studio_binary_field_lN2B8_filename = fields.Char(
        string='Filename for x_studio_binary_field_lN2B8')
    x_studio_category_id = fields.Integer(string='Category ID')
    x_studio_char_field_zSfyl = fields.Char(string='New Text')
    x_studio_clean = fields.Boolean(string='Clean')
    x_studio_item_approval_request_sent = fields.Boolean(
        string='Item Approval Request Sent')
    x_studio_item_approval_request_sent_prod = fields.Boolean(
        string='Item Approval Request Sent Prod')
    x_studio_item_approved = fields.Boolean(string='Item Approved')
    x_studio_item_approved_prod = fields.Boolean(string='Item Approved Prod')
    x_studio_many2one_field_8eWzY = fields.Many2one(
        'product.pricelist', string='Pricelist', ondelete='set null')
    x_studio_maximum_discount = fields.Float(string='Maximum  Discount %')
    x_studio_melt_item = fields.Boolean(string='Melt Item')
    x_studio_product_type = fields.Selection(
        [('Motor', 'Motor'), ('Other Products', 'Other Products'),
         ('Vehicles', 'Vehicles'), ('Pumps', 'Pumps')],
        string='Internal Product Type')
    x_studio_sub_contract = fields.Boolean(string='Sub-Contract')
    x_studio_tariff_code = fields.Many2one(
        'x_tariffmaster', string='Tariff Code', ondelete='set null')
