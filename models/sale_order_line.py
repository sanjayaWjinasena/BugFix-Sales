from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # ---- Studio-ported x_studio_* fields ----
    category = fields.Many2one("project_category", string="Category")
    category_name = fields.Char(string="Category Name", readonly=True)
    clear_free_items = fields.Boolean(string="Clear Free Items")
    commission = fields.Float(string="Commission %")
    cost_amount_inventory_shortage = fields.Float(
        string="Cost Amount (Inventory Shortage)"
    )
    cost_amount_req_qty = fields.Float(string="Cost Amount (Req. Qty)")
    cost_value = fields.Float(string="Cost Value")
    count_2 = fields.Integer(string="Count 2")
    current_onhand = fields.Float(string="Current Onhand")
    inventory_shortage = fields.Float(string="Inventory Shortage")
    invt_status = fields.Boolean(string="Invt. Status")
    main_project_2 = fields.Many2one(
        "project.project", string="Main Project 2", readonly=True
    )
    main_project_no = fields.Many2one(
        "project.project", string="Main Project No", readonly=True, store=False
    )
    many2one_field_btM1W = fields.Many2one(
        "mrp.production", string="Production Order"
    )
    margin_exceed = fields.Boolean(
        string="Margin Exceed", readonly=True, store=False
    )
    over_commission = fields.Boolean(string="Over Commission")
    pr_created = fields.Boolean(string="PR Created")
    price_confirmed = fields.Boolean(string="Price Confirmed")
    pricelist_id = fields.Many2one(
        "product.pricelist", string="Pricelist Id", readonly=True
    )
    product_status = fields.Selection(
        [
            ("Blank", "Blank"),
            ("New Item", "New Item"),
            ("Existing Item", "Existing Item"),
        ],
        string="Product Status",
        readonly=True,
        store=False,
    )
    production_completed = fields.Boolean(string="Production Completed")
    project_no = fields.Many2one(
        "project.project", string="Project No", readonly=True
    )
    project_no_1 = fields.Many2one(
        "project.project", string="Project No", readonly=True
    )
    purch_type = fields.Selection(
        [("Local", "Local"), ("Import", "Import")], string="Purch. Type"
    )
    quotation_type = fields.Selection(
        [("Sales", "Sales"), ("Project", "Project"), ("Repair", "Repair")],
        string="Quotation Type",
        readonly=True,
    )
    re_estimate_count = fields.Integer(string="Re-estimate Count", readonly=True)
    re_estimate_request_sent = fields.Boolean(
        string="Re-estimate Request Sent", readonly=True
    )
    req_for_production = fields.Boolean(string="Req. for Production")
    req_qty = fields.Integer(string="Req. Qty")
    rug_confirmed = fields.Boolean(string="RUG Confirmed", readonly=True)
    sales_report_type = fields.Many2one(
        "sales_report_type", string="Sales Report Type"
    )
    sub_contract = fields.Boolean(
        string="Sub-Contract", readonly=True, store=False
    )
    total = fields.Char(string="Total", store=False)
    trans_type = fields.Char(string="Trans Type", readonly=True, store=False)
    unlocked = fields.Boolean(string="Unlocked", readonly=True)
    sales_warehouse_id = fields.Many2one("stock.warehouse", string="Warehouse")
    # ---- End Studio-ported ----

    # Ported from Studio (v33). Consumed by BugFix-Sales' account-mandatory
    # gate on the parent sale.order (mirrored per-line).
    account_mandatory = fields.Boolean(
        string="Account Mandatory",
    )
    # v43: original line price captured by Fix-repair's RUG-repricing
    # logic (sale_order_line.py's create/write override on Fix-repair
    # v279+). Studio also uses this field to restore the customer-facing
    # price if RUG is later rejected. Declared here so BugFix-Sales
    # owns the schema (single home for sale.order.line Studio fields);
    # Fix-repair reads/writes via the same field name.
    price_unit_original = fields.Float(
        string="Price Unit Original",
    )
    # v44: per-line re-estimation marker + instance counter.
    # Written by Fix-repair v283's port of Studio automation 204
    # (RR - Track Lock Status - 3): when a Repair SO is currently
    # unlocked (parent unlocked=True) and the user edits a
    # line in the form, re_estimated flips to True and
    # count_1 is set to (parent.re_estimate_count + 1).
    # sale.order-side automations 202/203 read the max count_1
    # of re-estimated lines to know the target re-estimate count for
    # the header. Declared here (BugFix-Sales owns line-level Studio
    # schema) so Fix-repair only carries the automation logic.
    re_estimated = fields.Boolean(
        string="Re-estimated",
    )
    count_1 = fields.Integer(
        string="Re-estimate Instance",
    )
