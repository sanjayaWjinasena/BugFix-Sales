# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # ---- Studio-ported x_studio_* fields (v0.1.0.58) ----
    x_studio_binary_field_lN2B8 = fields.Binary(string='New File')
    x_studio_binary_field_lN2B8_filename = fields.Char(
        string='Filename for x_studio_binary_field_lN2B8')
    x_studio_boolean_field_FFbpV = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_FxQqp = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_IsrsH = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_JKe77 = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_JpVfJ = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_NjgGv = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_OA6o4 = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_OmpWA = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_Q23qt = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_XrNz2 = fields.Boolean(string='New Checkbox')
    x_studio_boolean_field_qKrKh = fields.Boolean(string='New Checkbox')
    x_studio_category_id = fields.Integer(string='Category ID')
    x_studio_char_field_2ug_1iullp7gr = fields.Char(string='New Text')
    x_studio_char_field_zSfyl = fields.Char(string='New Text')
    x_studio_charge = fields.Boolean(string='Charge')
    x_studio_clean = fields.Boolean(string='Clean')
    x_studio_duty = fields.Boolean(string='Duty')
    x_studio_float_field_KIV5v = fields.Float(string='New Decimal')
    x_studio_item_approval_request_sent = fields.Boolean(
        string='Item Approval Request Sent')
    x_studio_item_approval_request_sent_2 = fields.Boolean(
        string='Item Approval Request Sent 2')
    x_studio_item_approval_request_sent_prod = fields.Boolean(
        string='Item Approval Request Sent Prod')
    x_studio_item_approval_request_sent_temp = fields.Boolean(
        string='Item Approval Request Sent Temp')
    x_studio_item_approved = fields.Boolean(string='Item Approved')
    x_studio_item_approved_prod = fields.Boolean(string='Item Approved Prod')
    x_studio_item_approved_temp = fields.Boolean(string='Item Approved Temp')
    x_studio_many2one_field_8eWzY = fields.Many2one(
        'product.pricelist', string='Pricelist', ondelete='set null')
    x_studio_many2one_field_AS0wC = fields.Many2one(
        'x_tariffmaster', string='TariffMaster', ondelete='set null')
    x_studio_maximum_discount = fields.Float(string='Maximum  Discount %')
    x_studio_maximum_discount_ = fields.Float(string='Maximum  Discount %')
    x_studio_melt = fields.Boolean(string='Melt')
    x_studio_melt_item = fields.Boolean(string='Melt Item')
    # Selection with empty options on Clear-DB (Studio user hadn't
    # configured values yet). Preserved verbatim.
    x_studio_product_type = fields.Selection([], string='Internal Product Type')
    x_studio_related_field_59m_1iv4fum1u = fields.Boolean(string='New Related Field')
    x_studio_related_field_850_1iv4flunc = fields.Boolean(string='New Related Field')
    x_studio_related_field_YoMQf = fields.Integer(string='New Related Field')
    x_studio_selection_field_Coru2 = fields.Selection([], string='New Selection')
    x_studio_selection_field_MSMlW = fields.Selection([], string='New Selection')
    x_studio_serial = fields.Char(string='Serial Number')
    x_studio_sub_contract = fields.Boolean(string='Sub-Contract')
    x_studio_tariff_code = fields.Many2one(
        'x_tariffmaster', string='Tariff Code', ondelete='set null')
    x_studio_tax = fields.Boolean(string='Tax')
