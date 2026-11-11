from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    # ---- Studio-ported x_studio_* fields (v0.1.0.58) ---- v17.0.1.0.171: template
    # fields (Tariff Code, Internal Product Type, Maximum Discount %, Sub-Contract, Melt
    # Item, Clean, ...) are no longer redeclared here. On Clear-DB the variant reads
    # them from its template (_inherits); a separate stored copy left them empty on
    # variants (Imports row 14: 'No Valid Date Range for the Tariff Codes'). The fields
    # below are not template fields on Clear-DB.
    boolean_field_FFbpV = fields.Boolean(string="New Checkbox")
    boolean_field_FxQqp = fields.Boolean(string="New Checkbox")
    boolean_field_IsrsH = fields.Boolean(string="New Checkbox")
    boolean_field_JKe77 = fields.Boolean(string="New Checkbox")
    boolean_field_JpVfJ = fields.Boolean(string="New Checkbox")
    boolean_field_NjgGv = fields.Boolean(string="New Checkbox")
    boolean_field_OA6o4 = fields.Boolean(string="New Checkbox")
    boolean_field_OmpWA = fields.Boolean(string="New Checkbox")
    boolean_field_Q23qt = fields.Boolean(string="New Checkbox")
    boolean_field_XrNz2 = fields.Boolean(string="New Checkbox")
    boolean_field_qKrKh = fields.Boolean(string="New Checkbox")
    char_field_2ug_1iullp7gr = fields.Char(string="New Text")
    charge = fields.Boolean()
    duty = fields.Boolean()
    float_field_KIV5v = fields.Float(string="New Decimal")
    item_approval_request_sent = fields.Boolean()
    item_approval_request_sent_2 = fields.Boolean()
    item_approval_request_sent_temp = fields.Boolean()
    item_approved = fields.Boolean()
    item_approved_temp = fields.Boolean()
    many2one_field_AS0wC = fields.Many2one(
        "tariffmaster", string="TariffMaster", ondelete="set null"
    )
    maximum_discount_ = fields.Float(string="Maximum  Discount %")
    melt = fields.Boolean()
    related_field_59m_1iv4fum1u = fields.Boolean(string="New Related Field")
    related_field_850_1iv4flunc = fields.Boolean(string="New Related Field")
    related_field_YoMQf = fields.Integer(string="New Related Field")
    selection_field_Coru2 = fields.Selection([], string="New Selection")
    selection_field_MSMlW = fields.Selection([], string="New Selection")
    serial = fields.Char(string="Serial Number")
    tax = fields.Boolean()
