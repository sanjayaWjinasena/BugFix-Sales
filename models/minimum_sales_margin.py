from odoo import fields, models


class X_minimum_sales_margin(models.Model):
    _name = "minimum_sales_margin"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Minimum Sales Margin %"

    active = fields.Boolean()
    name = fields.Char()
    accounting_active = fields.Boolean(string="Active")
    advance_payment_ = fields.Float(string="Advance Payment %")
    accounting_company_id = fields.Many2one(
        comodel_name="res.company", string="Company"
    )
    last_purchase_price_validity_days = fields.Integer(
        string="Last Purchase Price Validity (Days)"
    )
    minimum_sales_margin_ = fields.Float(string="Minimum Sales Margin %")
    sales_order_validity = fields.Integer(string="Sales Order Validity (Days)")
    sequence = fields.Integer()


class XMinimumSalesMarginGap(models.Model):
    _inherit = "minimum_sales_margin"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
