# BugFix-Sales — `sale.report`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `sale.report` — Sales Analysis Report

*Extends a model created by `sale`.*

**Summary:**

<!-- SUMMARY:model:sale.report -->
This repo adds a Sales Analysis By Salespersons window action and a form view listing the report fields for the Sales Analysis report. It adds no fields or logic.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Analysis By Salespersons | `act_window_3170_sales_analysis_by_salespersons` | Opens **Sales Analysis Report** records (graph,pivot,form). | `model sale.report` (sale) |  |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for ir.model(600,) | `ported_default_form_view_fo_e0d2cf85_360c_4576_b7f6_9020babe12f0` | form | full form layout with 41 fields | Form view for the Sales Analysis report, listing all report fields (customer, product, quantities, amounts, team, dates, etc.) in two columns. | `sale.report.analytic_account_id` (sale)<br>`sale.report.campaign_id` (sale)<br>`sale.report.categ_id` (sale)<br>`sale.report.commercial_partner_id` (sale)<br>`sale.report.company_id` (sale)<details><summary>+36 more</summary>`sale.report.country_id` (sale)<br>`sale.report.currency_id` (sale)<br>`sale.report.date` (sale)<br>`sale.report.discount_amount` (sale)<br>`sale.report.discount` (sale)<br>`sale.report.industry_id` (sale)<br>`sale.report.invoice_status` (sale)<br>`sale.report.is_abandoned_cart` (website_sale)<br>`sale.report.medium_id` (sale)<br>`sale.report.name` (sale)<br>`sale.report.nbr` (sale)<br>`sale.report.order_reference` (sale)<br>`sale.report.partner_id` (sale)<br>`sale.report.partner_zip` (sale)<br>`sale.report.price_subtotal` (sale)<br>`sale.report.price_total` (sale)<br>`sale.report.pricelist_id` (sale)<br>`sale.report.product_id` (sale)<br>`sale.report.product_tmpl_id` (sale)<br>`sale.report.product_uom_qty` (sale)<br>`sale.report.product_uom` (sale)<br>`sale.report.qty_delivered` (sale)<br>`sale.report.qty_invoiced` (sale)<br>`sale.report.qty_to_deliver` (sale)<br>`sale.report.qty_to_invoice` (sale)<br>`sale.report.source_id` (sale)<br>`sale.report.state_id` (sale)<br>`sale.report.state` (sale)<br>`sale.report.team_id` (sale)<br>`sale.report.untaxed_amount_invoiced` (sale)<br>`sale.report.untaxed_amount_to_invoice` (sale)<br>`sale.report.user_id` (sale)<br>`sale.report.volume` (sale)<br>`sale.report.warehouse_id` (sale_stock)<br>`sale.report.website_id` (website_sale)<br>`sale.report.weight` (sale)</details> |  |
