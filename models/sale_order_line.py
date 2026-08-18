# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # ---- Studio-ported x_studio_* fields ----
    x_studio_category = fields.Many2one('x_project_category', string='Category')
    x_studio_category_name = fields.Char(string='Category Name', readonly=True)
    x_studio_clear_free_items = fields.Boolean(string='Clear Free Items')
    x_studio_commission = fields.Float(string='Commission %')
    x_studio_cost_amount_inventory_shortage = fields.Float(string='Cost Amount (Inventory Shortage)')
    x_studio_cost_amount_req_qty = fields.Float(string='Cost Amount (Req. Qty)')
    x_studio_cost_value = fields.Float(string='Cost Value')
    x_studio_count_2 = fields.Integer(string='Count 2')
    x_studio_current_onhand = fields.Float(string='Current Onhand')
    x_studio_inventory_shortage = fields.Float(string='Inventory Shortage')
    x_studio_invt_status = fields.Boolean(string='Invt. Status')
    x_studio_main_project_2 = fields.Many2one('project.project', string='Main Project 2', readonly=True)
    x_studio_main_project_no = fields.Many2one('project.project', string='Main Project No', readonly=True, store=False)
    x_studio_many2one_field_btM1W = fields.Many2one('mrp.production', string='Production Order')
    x_studio_margin_exceed = fields.Boolean(string='Margin Exceed', readonly=True, store=False)
    x_studio_over_commission = fields.Boolean(string='Over Commission')
    x_studio_pr_created = fields.Boolean(string='PR Created')
    x_studio_price_confirmed = fields.Boolean(string='Price Confirmed')
    x_studio_pricelist_id = fields.Many2one('product.pricelist', string='Pricelist Id', readonly=True)
    x_studio_product_status = fields.Selection([], string='Product Status', readonly=True, store=False)
    x_studio_production_completed = fields.Boolean(string='Production Completed')
    x_studio_project_no = fields.Many2one('project.project', string='Project No', readonly=True)
    x_studio_project_no_1 = fields.Many2one('project.project', string='Project No', readonly=True)
    x_studio_purch_type = fields.Selection([], string='Purch. Type')
    x_studio_quotation_type = fields.Selection([], string='Quotation Type', readonly=True)
    x_studio_re_estimate_count = fields.Integer(string='Re-estimate Count', readonly=True)
    x_studio_re_estimate_request_sent = fields.Boolean(string='Re-estimate Request Sent', readonly=True)
    x_studio_req_for_production = fields.Boolean(string='Req. for Production')
    x_studio_req_qty = fields.Integer(string='Req. Qty')
    x_studio_rug_confirmed = fields.Boolean(string='RUG Confirmed', readonly=True)
    x_studio_sales_report_type = fields.Many2one('x_sales_report_type', string='Sales Report Type')
    x_studio_sub_contract = fields.Boolean(string='Sub-Contract', readonly=True, store=False)
    x_studio_total = fields.Char(string='Total', store=False)
    x_studio_trans_type = fields.Char(string='Trans Type', readonly=True, store=False)
    x_studio_unlocked = fields.Boolean(string='Unlocked', readonly=True)
    x_studio_warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
    # ---- End Studio-ported ----

    # Ported from Studio (v33). Consumed by BugFix-Sales' account-mandatory
    # gate on the parent sale.order (mirrored per-line).
    x_studio_account_mandatory = fields.Boolean(
        string='Account Mandatory',
    )
    # v43: original line price captured by Fix-repair's RUG-repricing
    # logic (sale_order_line.py's create/write override on Fix-repair
    # v279+). Studio also uses this field to restore the customer-facing
    # price if RUG is later rejected. Declared here so BugFix-Sales
    # owns the schema (single home for sale.order.line Studio fields);
    # Fix-repair reads/writes via the same field name.
    x_studio_price_unit_original = fields.Float(
        string='Price Unit Original',
    )
    # v44: per-line re-estimation marker + instance counter.
    # Written by Fix-repair v283's port of Studio automation 204
    # (RR - Track Lock Status - 3): when a Repair SO is currently
    # unlocked (parent x_studio_unlocked=True) and the user edits a
    # line in the form, x_studio_re_estimated flips to True and
    # x_studio_count_1 is set to (parent.x_studio_re_estimate_count + 1).
    # sale.order-side automations 202/203 read the max x_studio_count_1
    # of re-estimated lines to know the target re-estimate count for
    # the header. Declared here (BugFix-Sales owns line-level Studio
    # schema) so Fix-repair only carries the automation logic.
    x_studio_re_estimated = fields.Boolean(
        string='Re-estimated',
    )
    x_studio_count_1 = fields.Integer(
        string='Re-estimate Instance',
    )
