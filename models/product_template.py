from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # ---- Studio-ported x_studio_* fields (v0.1.0.58) ----
    binary_field_lN2B8 = fields.Binary(string="New File")
    binary_field_lN2B8_filename = fields.Char(string="Filename for binary_field_lN2B8")
    category_id = fields.Integer(string="Category ID")
    char_field_zSfyl = fields.Char(string="New Text")
    clean = fields.Boolean()
    item_approval_request_sent = fields.Boolean()
    item_approval_request_sent_prod = fields.Boolean()
    item_approved = fields.Boolean()
    item_approved_prod = fields.Boolean()
    many2one_field_8eWzY = fields.Many2one(
        "product.pricelist", string="Pricelist", ondelete="set null"
    )
    maximum_discount = fields.Float(string="Maximum  Discount %")
    melt_item = fields.Boolean()
    product_type = fields.Selection(
        [
            ("Motor", "Motor"),
            ("Other Products", "Other Products"),
            ("Vehicles", "Vehicles"),
            ("Pumps", "Pumps"),
            ("None", "None"),
        ],
        string="Internal Product Type",
    )
    sub_contract = fields.Boolean(string="Sub-Contract")
    tariff_code = fields.Many2one("tariffmaster", ondelete="set null")
