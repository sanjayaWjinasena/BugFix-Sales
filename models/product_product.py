# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # ---- Studio-ported x_studio_* fields (v0.1.0.58) ----
    # v17.0.1.0.171: template fields (Tariff Code, Internal Product Type, Maximum Discount %,
    # Sub-Contract, Melt Item, Clean, ...) are no longer redeclared here. On Clear-DB the variant
    # reads them from its template (_inherits); a separate stored copy left them empty on variants
    # (Imports row 14: 'No Valid Date Range for the Tariff Codes'). The fields below are not
    # template fields on Clear-DB.
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
    x_studio_char_field_2ug_1iullp7gr = fields.Char(string='New Text')
    x_studio_charge = fields.Boolean(string='Charge')
    x_studio_duty = fields.Boolean(string='Duty')
    x_studio_float_field_KIV5v = fields.Float(string='New Decimal')
    x_studio_item_approval_request_sent = fields.Boolean(
        string='Item Approval Request Sent')
    x_studio_item_approval_request_sent_2 = fields.Boolean(
        string='Item Approval Request Sent 2')
    x_studio_item_approval_request_sent_temp = fields.Boolean(
        string='Item Approval Request Sent Temp')
    x_studio_item_approved = fields.Boolean(string='Item Approved')
    x_studio_item_approved_temp = fields.Boolean(string='Item Approved Temp')
    x_studio_many2one_field_AS0wC = fields.Many2one(
        'x_tariffmaster', string='TariffMaster', ondelete='set null')
    x_studio_maximum_discount_ = fields.Float(string='Maximum  Discount %')
    x_studio_melt = fields.Boolean(string='Melt')
    x_studio_related_field_59m_1iv4fum1u = fields.Boolean(string='New Related Field')
    x_studio_related_field_850_1iv4flunc = fields.Boolean(string='New Related Field')
    x_studio_related_field_YoMQf = fields.Integer(string='New Related Field')
    x_studio_selection_field_Coru2 = fields.Selection([], string='New Selection')
    x_studio_selection_field_MSMlW = fields.Selection([], string='New Selection')
    x_studio_serial = fields.Char(string='Serial Number')
    x_studio_tax = fields.Boolean(string='Tax')
