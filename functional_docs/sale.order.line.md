# BugFix-Sales — `sale.order.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `sale.order.line` — Sales Order Line

*Extends a model created by `sale`.* Python: `models/sale_order_line.py`.

Other repos that use this model: `access right BugFix-Analytics.access_6247_inv___administrator` (BugFix-Analytics)<br>`access right BugFix-Analytics.access_7003_sales_order_lines` (BugFix-Analytics)<br>`helpdesk.ticket._compute_x_studio_task_status()` (Fix-repair)<br>`helpdesk.ticket._compute_x_studio_valid_delivered_so()` (Fix-repair)<br>`record rule BugFix-Analytics.rule_158_sales_order_line_multi_company` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_163_portal_sales_orders_line` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_168_personal_order_lines` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_169_all_orders_lines` (BugFix-Analytics)<details><summary>+13 more</summary>`record rule BugFix-Analytics.rule_419_sale_planning_planning_admin_can_see_every_service_sol` (BugFix-Analytics)<br>`report BugFix-Studio-Misc.action_report_1596_sales_order_lines` (BugFix-Studio-Misc)<br>`sale.order._fix_repair_apply_track_lock_status()` (Fix-repair)<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_production_purchase_report` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1763_srm_rpt_sales_production_purchase_report` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin` (BugFix-Accounting)<br>`server action BugFix-Studio-Misc.server_action_2268_sample_server_action_2` (BugFix-Studio-Misc)<br>`x_purchase_request_lin.x_studio_sales_line_id` (BugFix-Purchase)<br>`x_sales_report_model.x_studio_related_field_DqBBB` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_sales_lines_id` (Jinasena_Masterdata_Reporting)<br>`x_temp_estimated.x_studio_sales_order_line_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:sale.order.line -->
This repo adds about 40 fields to order lines, including Quotation Type, commission %, margin and over-commission flags, project and production links, cost and stock-shortage figures, RUG and re-estimate flags and Sales Report Type. Active automations reject discounts above the product's Maximum Discount, flag over-commission, apply pricelist discounts, update Price Confirmed and cost and stock details on Project lines, apply guarantee pricing to RUG-confirmed Repair lines, mark lines re-estimated on unlocked Repair orders, set the analytic Account Mandatory flag and fill the Sales Report Type. It also adds the Sales Order Lines, Line Items and Sales - Production Request Status lists and a project manager record rule.
<!-- /SUMMARY -->

**Fields (40):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_account_mandatory` | Account Mandatory | boolean | Flags that analytic account is mandatory on the line; set by the update-analytic-tag-parameters (sales line product) action. | stored |  | `server action BugFix-Sales.server_action_2416_update_analytic_tag_parameters_sales_line_product` |
| `x_studio_category` | Category | many2one → `x_project_category` | Project category of the order line; shown in the order line list. | stored | `model x_project_category` (BugFix-Project) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`<br>`view BugFix-Sales.ported_view_3259_odoo_studio_sale_order_line_tree_customi` |
| `x_studio_category_name` | Category Name | char | Text category name on the order line. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_clear_free_items` | Clear Free Items | boolean | Flags a line as a free item to clear; used by the 'SLS Clear Free Items SO Lines' action. | stored |  | `server action BugFix-Sales.server_action_2332_sls_clear_free_items_so_lines` |
| `x_studio_commission` | Commission % | float | Commission % on the line; validated by an automation/server action that flags over-commission, and also read by the margin validation. | stored |  | `automation BugFix-Sales.base_automation_90_sls_validate_commission_in_so_line`<br>`server action BugFix-Sales.server_action_1498_sls_validate_commission_in_so_line`<br>`server action BugFix-Sales.server_action_1508_sls_validate_margin_in_so_line` |
| `x_studio_cost_amount_inventory_shortage` | Cost Amount (Inventory Shortage) | float | Cost of the short quantity on a project line; filled by 'PROJ Item Related Details in Project SO'. | stored |  | `server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_cost_amount_req_qty` | Cost Amount (Req. Qty) | float | Cost of the required quantity on a project line; filled by 'PROJ Item Related Details in Project SO'. | stored |  | `server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_cost_value` | Cost Value | float | Unit cost value of the line's product; filled by 'PROJ Item Related Details in Project SO'. | stored |  | `server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_count_1` | Re-estimate Instance | integer | Re-estimate instance number of the line (default via a default record); maintained by the 'RR Track Lock Status 3' actions. | stored |  | `default BugFix-Sales.default_366_sale_order_line_x_studio_count_1`<br>`server action BugFix-Sales.sa_f5_sale_order_line_rr_track_lock_status_3`<br>`server action BugFix-Sales.server_action_2252_rr_track_lock_status_3` |
| `x_studio_count_2` | Count 2 | integer | Integer counter on the line with a default value record. Not used by any view or logic in this repo. | stored |  | `default BugFix-Sales.default_367_sale_order_line_x_studio_count_2` |
| `x_studio_current_onhand` | Current Onhand | float | On-hand stock of the product at the time of the project details update; filled by 'PROJ Item Related Details in Project SO'. | stored |  | `server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_inventory_shortage` | Inventory Shortage | float | Quantity short of stock on a project line; filled by 'PROJ Item Related Details in Project SO'. | stored |  | `server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_invt_status` | Invt. Status | boolean | Inventory status flag of a project line; set by 'PROJ Item Related Details in Project SO'. | stored |  | `server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_main_project_2` | Main Project 2 | many2one → `project.project` | Main project of the line; used by the 'Line Items' window action. | stored | `model project.project` (project) | `window action BugFix-Sales.act_window_2195_line_items` |
| `x_studio_main_project_no` | Main Project No | many2one → `project.project` | Main project link on the line. Not used by any view or logic in this repo. | not stored | `model project.project` (project) |  |
| `x_studio_many2one_field_btM1W` | Production Order | many2one → `mrp.production` | Manufacturing order linked to the line; shown in the order line list. | stored | `model mrp.production` (mrp) | `view BugFix-Sales.ported_view_3259_odoo_studio_sale_order_line_tree_customi` |
| `x_studio_margin_exceed` | Margin Exceed | boolean | True when the line breaches the margin rule; set by 'SLS Validate Margin in SO Line'. | not stored |  | `server action BugFix-Sales.server_action_1508_sls_validate_margin_in_so_line` |
| `x_studio_over_commission` | Over Commission | boolean | True when the line's commission exceeds the allowed level; set by 'SLS Validate Commission in SO Line'. | stored |  | `server action BugFix-Sales.server_action_1498_sls_validate_commission_in_so_line` |
| `x_studio_pr_created` | PR Created | boolean | Marks that a purchase request was created for this line. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_price_confirmed` | Price Confirmed | boolean | Marks the line's price as confirmed; updated by the 'PROJ Update Price Confirmed Status' actions. | stored |  | `server action BugFix-Sales.sa_f5_sale_order_line_proj_update_price_confirmed_status`<br>`server action BugFix-Sales.server_action_2898_proj_update_price_confirmed_status` |
| `x_studio_price_unit_original` | Price Unit Original | float | Original unit price saved before RUG pricing is applied; set by 'RR Sales Price for RUG Items' and shown in the line list. | stored |  | `server action BugFix-Sales.sa_f5_sale_order_line_rr_sales_price_for_rug_items`<br>`server action BugFix-Sales.server_action_2144_rr_sales_price_for_rug_items`<br>`view BugFix-Sales.ported_view_3259_odoo_studio_sale_order_line_tree_customi` |
| `x_studio_pricelist_id` | Pricelist Id | many2one → `product.pricelist` | Pricelist applied to the line; used by the 'SLS Apply Pricelist in SO Lines' and 'PROJ Update Price Confirmed Status' actions. | stored | `model product.pricelist` (product) | `server action BugFix-Sales.sa_f5_sale_order_line_proj_update_price_confirmed_status`<br>`server action BugFix-Sales.server_action_2314_sls_apply_pricelist_in_so_lines`<br>`server action BugFix-Sales.server_action_2315_sls_apply_pricelist_in_so_lines`<br>`server action BugFix-Sales.server_action_2898_proj_update_price_confirmed_status` |
| `x_studio_product_status` | Product Status | selection: Blank=Blank; New Item=New Item; Existing Item=Existing Item | Whether the line item is Blank, a New Item or an Existing Item (default via a default record); set by 'PROJ Item Related Details in Project SO'. | not stored |  | `default BugFix-Sales.default_325_sale_order_line_x_studio_product_status`<br>`server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so` |
| `x_studio_production_completed` | Production Completed | boolean | Marks production for the line as completed; shown in the order line list. | stored |  | `view BugFix-Sales.ported_view_3259_odoo_studio_sale_order_line_tree_customi` |
| `x_studio_project_no` | Project No | many2one → `project.project` | Project of the line; shown in the order line list and used by the 'Line Items' window action. | stored | `model project.project` (project) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`<br>`view BugFix-Sales.ported_view_3259_odoo_studio_sale_order_line_tree_customi`<br>`window action BugFix-Sales.act_window_2194_line_items` |
| `x_studio_project_no_1` | Project No | many2one → `project.project` | Second project link on the line. Not used by any view or logic in this repo. | stored | `model project.project` (project) |  |
| `x_studio_purch_type` | Purch. Type | selection: Local=Local; Import=Import | Purchase type for the line: Local or Import. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_quotation_type` | Quotation Type | selection: Sales=Sales; Project=Project; Repair=Repair | Quotation type of the line (Sales, Project, Repair); used by lock tracking, RUG pricing, margin validation, price-confirmed and project item details actions. | stored |  | `automation BugFix-Sales.base_automation_204_rr_track_lock_status_3`<br>`server action BugFix-Sales.sa_f5_sale_order_line_proj_update_price_confirmed_status`<br>`server action BugFix-Sales.sa_f5_sale_order_line_rr_sales_price_for_rug_items`<br>`server action BugFix-Sales.sa_f5_sale_order_line_rr_track_lock_status_3`<br>`server action BugFix-Sales.server_action_1508_sls_validate_margin_in_so_line`<details><summary>+4 more</summary>`server action BugFix-Sales.server_action_2144_rr_sales_price_for_rug_items`<br>`server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so`<br>`server action BugFix-Sales.server_action_2252_rr_track_lock_status_3`<br>`server action BugFix-Sales.server_action_2898_proj_update_price_confirmed_status`</details> |
| `x_studio_re_estimate_count` | Re-estimate Count | integer | Re-estimate counter on the line; used by the 'RR Track Lock Status 3' actions. | stored |  | `server action BugFix-Sales.sa_f5_sale_order_line_rr_track_lock_status_3`<br>`server action BugFix-Sales.server_action_2252_rr_track_lock_status_3` |
| `x_studio_re_estimate_request_sent` | Re-estimate Request Sent | boolean | Marks that a re-estimate request was sent for the line. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_re_estimated` | Re-estimated | boolean | Marks the line as re-estimated; maintained by the 'RR Track Lock Status 3' actions. | stored |  | `server action BugFix-Sales.sa_f5_sale_order_line_rr_track_lock_status_3`<br>`server action BugFix-Sales.server_action_2252_rr_track_lock_status_3` |
| `x_studio_req_for_production` | Req. for Production | boolean | Flags that the line requires production. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_req_qty` | Req. Qty | integer | Required quantity for the line (default via a default record); shown in the order line list. | stored |  | `default BugFix-Sales.default_244_sale_order_line_x_studio_req_qty`<br>`view BugFix-Sales.ported_view_3259_odoo_studio_sale_order_line_tree_customi` |
| `x_studio_rug_confirmed` | RUG Confirmed | boolean | Repair-Under-Guarantee confirmed flag on the line; used by 'RR Sales Price for RUG Items' to adjust prices. | stored |  | `server action BugFix-Sales.sa_f5_sale_order_line_rr_sales_price_for_rug_items`<br>`server action BugFix-Sales.server_action_2144_rr_sales_price_for_rug_items` |
| `x_studio_sales_report_type` | Sales Report Type | many2one → `x_sales_report_type` | Sales report category of the order line (link to Sales Report Type); filled automatically by the 'SRM auto populate report type in SO lines' server action. | stored | `model x_sales_report_type` (Jinasena_Masterdata_Reporting) | `server action BugFix-Sales.server_action_1729_srm_auto_populate_report_type_in_so_lines` |
| `x_studio_sub_contract` | Sub-Contract | boolean | Flags the line as sub-contract. Not used by any view or logic in this repo. | not stored |  |  |
| `x_studio_total` | Total | char | Free-text 'Total' field on the line. Not used by any view or logic in this repo. | not stored |  |  |
| `x_studio_trans_type` | Trans Type | char | Free-text transaction type on the line. Not used by any view or logic in this repo. | not stored |  |  |
| `x_studio_unlocked` | Unlocked | boolean | Unlock flag on the line, maintained by the 'RR Track Lock Status 3' actions. | stored |  | `server action BugFix-Sales.sa_f5_sale_order_line_rr_track_lock_status_3`<br>`server action BugFix-Sales.server_action_2252_rr_track_lock_status_3` |
| `x_studio_warehouse_id` | Warehouse | many2one → `stock.warehouse` | Warehouse used for the line's stock checks; used by 'PROJ Item Related Details in Project SO'. | stored | `model stock.warehouse` (stock) | `server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |

**Server actions (15):**

- **Execute Code** (`server_action_2144_rr_sales_price_for_rug_items`, type `code`)
  - Function: Run by its automation: on RUG-confirmed Repair order lines, saves the current price as Original Price and sets the unit price to the product cost.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.price_unit` (sale), `sale.order.line.product_template_id` (sale), `sale.order.line.x_studio_price_unit_original`, `sale.order.line.x_studio_quotation_type`<details><summary>+1 more</summary>`sale.order.line.x_studio_rug_confirmed`</details>
  - Used by: `automation BugFix-Sales.base_automation_193_rr_sales_price_for_rug_items`
  <details><summary>code (5 lines)</summary>

```python

if record.x_studio_quotation_type == 'Repair':
  original_price = record.price_unit
  if record.x_studio_rug_confirmed == True:
    record.write({'price_unit': record.product_template_id.standard_price,'x_studio_price_unit_original': original_price})
```
  </details>
- **Execute Code** (`server_action_2252_rr_track_lock_status_3`, type `code`)
  - Function: Run by its automation: on lines of Unlocked Repair orders, marks the line Re-estimated and sets its count to the order's re-estimate count plus one.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.x_studio_count_1`, `sale.order.line.x_studio_quotation_type`, `sale.order.line.x_studio_re_estimate_count`, `sale.order.line.x_studio_re_estimated`<details><summary>+1 more</summary>`sale.order.line.x_studio_unlocked`</details>
  - Used by: `automation BugFix-Sales.base_automation_204_rr_track_lock_status_3`
  <details><summary>code (5 lines)</summary>

```python

if record.x_studio_quotation_type == 'Repair': 
 if record.x_studio_unlocked == True:
    record['x_studio_re_estimated'] = True
    record['x_studio_count_1'] = record.x_studio_re_estimate_count + 1
```
  </details>
- **Execute Code** (`server_action_2898_proj_update_price_confirmed_status`, type `code`)
  - Function: Run by its automation: for Project lines copies Price Confirmed from the product's pricelist item (clears discount if none); non-Project lines get Price Confirmed cleared.
  - Depends on: `model product.pricelist.item` (product), `model sale.order.line` (sale), `sale.order.line.product_id` (sale), `sale.order.line.product_template_id` (sale), `sale.order.line.x_studio_price_confirmed`<details><summary>+2 more</summary>`sale.order.line.x_studio_pricelist_id`, `sale.order.line.x_studio_quotation_type`</details>
  - Used by: `automation BugFix-Sales.base_automation_342_proj_update_price_confirmed_status`
  <details><summary>code (18 lines)</summary>

```python

if record.x_studio_quotation_type == 'Project':

  if record.product_id.id  != False:

    pricelist = env['product.pricelist.item'].search([('pricelist_id', '=', record.x_studio_pricelist_id.id),('product_tmpl_id', '=', record.product_template_id.id)],limit=1)

    if pricelist:

      record['x_studio_price_confirmed'] = pricelist.x_studio_price_confirmed

    else:

      record['discount'] = False

else:

  record['x_studio_price_confirmed'] = False
```
  </details>
- **PROJ - Update Price Confirmed Status** (`sa_f5_sale_order_line_proj_update_price_confirmed_status`, type `code`)
  - Function: For Project order lines, copies Price Confirmed from the matching pricelist item for the product (clears the discount if none found); for non-Project lines, clears Price Confirmed.
  - Depends on: `model product.pricelist.item` (product), `model sale.order.line` (sale), `sale.order.line.product_id` (sale), `sale.order.line.product_template_id` (sale), `sale.order.line.x_studio_price_confirmed`<details><summary>+2 more</summary>`sale.order.line.x_studio_pricelist_id`, `sale.order.line.x_studio_quotation_type`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (17 lines)</summary>

```python
if record.x_studio_quotation_type == 'Project':

  if record.product_id.id  != False:

    pricelist = env['product.pricelist.item'].search([('pricelist_id', '=', record.x_studio_pricelist_id.id),('product_tmpl_id', '=', record.product_template_id.id)],limit=1)

    if pricelist:

      record['x_studio_price_confirmed'] = pricelist.x_studio_price_confirmed

    else:

      record['discount'] = False

else:

  record['x_studio_price_confirmed'] = False
```
  </details>
- **PROJ-Item Related Details In Project SO** (`server_action_2162_proj_item_related_details_in_project_so`, type `code`)
  - Function: On Project order lines, finds the resupply warehouse and its on-hand qty via product routes, then writes cost, on-hand, shortage qty, cost amounts and inventory status; resets these values on non-Project lines.
  - Depends on: `model sale.order.line` (sale), `model stock.quant` (stock), `model stock.warehouse` (stock), `sale.order.line.product_template_id` (sale), `sale.order.line.product_uom_qty` (sale)<details><summary>+10 more</summary>`sale.order.line.warehouse_id` (sale_stock), `sale.order.line.x_studio_cost_amount_inventory_shortage`, `sale.order.line.x_studio_cost_amount_req_qty`, `sale.order.line.x_studio_cost_value`, `sale.order.line.x_studio_current_onhand`, `sale.order.line.x_studio_inventory_shortage`, `sale.order.line.x_studio_invt_status`, `sale.order.line.x_studio_product_status`, `sale.order.line.x_studio_quotation_type`, `sale.order.line.x_studio_warehouse_id`</details>
  - Used by: `automation BugFix-Sales.base_automation_196_proj_item_related_details_in_project_so`
  <details><summary>code (27 lines)</summary>

```python
if record.x_studio_quotation_type == 'Project':
  onhand_qty = 0
  qty_short = 0
  re_wh = False
  status = True 
  if record.x_studio_product_status != 'Blank':
    so_loc = env['stock.warehouse'].search([('id', '=', record.warehouse_id.id)],limit=1)
    if so_loc:
      for sup_lines in so_loc.resupply_wh_ids:
        for routes in record.product_template_id.route_ids:
          if routes.supplier_wh_id:
            if routes.supplier_wh_id.id == sup_lines.id:
              if routes.supplied_wh_id.id == record.warehouse_id.id:
                onhand = env['stock.quant'].search([('product_tmpl_id', '=', record.product_template_id.id),('location_id', '=', routes.supplier_wh_id.lot_stock_id.id)], limit=1)
                if onhand:
                  onhand_qty = onhand.available_quantity
              re_wh = routes.supplier_wh_id.id
   
    if record.product_template_id.detailed_type == 'service':
      qty_short = 0
    else:
      if record.product_uom_qty > onhand_qty:
        qty_short = (record.product_uom_qty - onhand_qty)
        status = False
    record.write({'x_studio_cost_value': record.product_template_id.standard_price, 'x_studio_warehouse_id': re_wh, 'x_studio_current_onhand': onhand_qty, 'x_studio_inventory_shortage': qty_short, 'x_studio_cost_amount_req_qty': (record.product_uom_qty * record.product_template_id.standard_price), 'x_studio_cost_amount_inventory_shortage': (qty_short * record.product_template_id.standard_price), 'x_studio_invt_status': status})
else:
   record.write({'x_studio_cost_value': 0, 'x_studio_warehouse_id': False, 'x_studio_current_onhand': 0, 'x_studio_inventory_shortage': 0, 'x_studio_cost_amount_req_qty': 0, 'x_studio_cost_amount_inventory_shortage': 0, 'x_studio_invt_status': False})
```
  </details>
- **RR - Sales Price For RUG Items** (`sa_f5_sale_order_line_rr_sales_price_for_rug_items`, type `code`)
  - Function: On Repair orders, when the line is RUG-confirmed, saves the current unit price as Original Price and replaces the unit price with the product's cost.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.price_unit` (sale), `sale.order.line.product_template_id` (sale), `sale.order.line.x_studio_price_unit_original`, `sale.order.line.x_studio_quotation_type`<details><summary>+1 more</summary>`sale.order.line.x_studio_rug_confirmed`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
if record.x_studio_quotation_type == 'Repair':
  original_price = record.price_unit
  if record.x_studio_rug_confirmed == True:
    record.write({'price_unit': record.product_template_id.standard_price,'x_studio_price_unit_original': original_price})
```
  </details>
- **RR - Track Lock Status - 3** (`sa_f5_sale_order_line_rr_track_lock_status_3`, type `code`)
  - Function: On Repair order lines edited while the order is Unlocked, marks the line Re-estimated and sets its count to the order's re-estimate count plus one.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.x_studio_count_1`, `sale.order.line.x_studio_quotation_type`, `sale.order.line.x_studio_re_estimate_count`, `sale.order.line.x_studio_re_estimated`<details><summary>+1 more</summary>`sale.order.line.x_studio_unlocked`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
if record.x_studio_quotation_type == 'Repair': 
 if record.x_studio_unlocked == True:
    record['x_studio_re_estimated'] = True
    record['x_studio_count_1'] = record.x_studio_re_estimate_count + 1
```
  </details>
- **SLS - Apply Pricelist in SO Lines** (`server_action_2315_sls_apply_pricelist_in_so_lines`, type `code`)
  - Function: Finds the pricelist item for the line's product and quantity; if found, grosses up the unit price and applies the item's discount %, otherwise sets the discount to 0.
  - Depends on: `model product.pricelist.item` (product), `model sale.order.line` (sale), `sale.order.line.price_unit` (sale), `sale.order.line.product_id` (sale), `sale.order.line.product_template_id` (sale)<details><summary>+2 more</summary>`sale.order.line.product_uom_qty` (sale), `sale.order.line.x_studio_pricelist_id`</details>
  - Used by: `automation BugFix-Sales.base_automation_212_sls_apply_pricelist_in_so_lines`
  <details><summary>code (13 lines)</summary>

```python
if record.product_id.id  != False:

  pricelist = env['product.pricelist.item'].search([('pricelist_id', '=', record.x_studio_pricelist_id.id),('product_tmpl_id', '=', record.product_template_id.id),('min_quantity', '<=', record.product_uom_qty)], limit=1)

  if pricelist:

    record['price_unit'] = record.price_unit/(1-pricelist.price_discount/100)

    record['discount'] = pricelist.price_discount

  else:

    record['discount'] = 0
```
  </details>
- **SLS - Apply Pricelist in SO Lines** (`server_action_2314_sls_apply_pricelist_in_so_lines`, type `code`)
  - Function: Sets the line discount to the matching pricelist item's discount % for the product and quantity (no price gross-up). Not referenced by any automation in this repo.
  - Depends on: `model product.pricelist.item` (product), `model sale.order.line` (sale), `sale.order.line.product_id` (sale), `sale.order.line.product_template_id` (sale), `sale.order.line.product_uom_qty` (sale)<details><summary>+1 more</summary>`sale.order.line.x_studio_pricelist_id`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (7 lines)</summary>

```python
if record.product_id.id  != False:

  pricelist = env['product.pricelist.item'].search([('pricelist_id', '=', record.x_studio_pricelist_id.id),('product_tmpl_id', '=', record.product_template_id.id),('min_quantity', '<=', record.product_uom_qty)], limit=1)

  if pricelist:

    record['discount'] = pricelist.price_discount
```
  </details>
- **SLS - Clear Free Items SO Lines** (`server_action_2332_sls_clear_free_items_so_lines`, type `code`)
  - Function: When a product line is added to an order that has reward (free) lines, sets Clear Free Items on the line, which surfaces the 'Validate Sales Lines' button.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.order_id` (sale), `sale.order.line.product_id` (sale), `sale.order.line.x_studio_clear_free_items`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (9 lines)</summary>

```python
if record.product_id.id  != False: 

  #free_items = env['sale.order.line'].search([('order_id', '=', record.order_id._origin.id),('is_reward_line', '=', True)]).unlink()

  free_items = env['sale.order.line'].search([('order_id', '=', record.order_id._origin.id),('is_reward_line', '=', True)])

  if free_items:

    record['x_studio_clear_free_items'] = True
```
  </details>
- **SLS - Validate Commission in SO Line** (`server_action_1498_sls_validate_commission_in_so_line`, type `code`)
  - Function: Sets Over Commission on the order line when the commission % exceeds the product's maximum discount minus the line discount; raises an error for negative commission.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.discount` (sale), `sale.order.line.product_id` (sale), `sale.order.line.x_studio_commission`, `sale.order.line.x_studio_over_commission`
  - Used by: `automation BugFix-Sales.base_automation_90_sls_validate_commission_in_so_line`
  <details><summary>code (35 lines)</summary>

```python
#if record.x_studio_commission > 0.00:

if record.x_studio_commission > record.product_id.x_studio_maximum_discount - record.discount:

  record['x_studio_over_commission'] = True

  """

  title = "Over Commission"

  message = "The Commission % Applied to the Line Exceeds the Authorised Limit and Require Approval to Further Process."

  

  action = {

            'type': 'ir.actions.client',

            'tag': 'display_notification',

            'params': {'title': title,'message': message,'sticky': True,}

            } 

  """

else:

  record['x_studio_over_commission'] = False



if record.x_studio_commission < 0.00:

  raise UserError('Commission Percentage Should not be a Negative.')
```
  </details>
- **SLS - Validate Discount in SO Line** (`server_action_1497_sls_validate_discount_in_so_line`, type `code`)
  - Function: Raises an error when a sales order line's discount exceeds the product's Maximum Discount.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.discount` (sale), `sale.order.line.product_id` (sale)
  - Used by: `automation BugFix-Sales.base_automation_89_sls_validate_discount_in_so_line`
  <details><summary>code (3 lines)</summary>

```python
if record.id:
  if record.product_id.x_studio_maximum_discount < record.discount:
    raise UserError('Line Discount Exceeds the Max. Discount Allowed for the Selected Item.')
```
  </details>
- **SLS - Validate Margin in SO Line** (`server_action_1508_sls_validate_margin_in_so_line`, type `code`)
  - Function: On non-Project lines, computes net margin after commission and cost and sets Margin Exceed when it is non-zero and below the company's Minimum Sales Margin %; otherwise clears it. Its automation is deactivated by the module.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.company_id` (sale), `sale.order.line.price_subtotal` (sale), `sale.order.line.product_id` (sale), `sale.order.line.product_uom_qty` (sale)<details><summary>+3 more</summary>`sale.order.line.x_studio_commission`, `sale.order.line.x_studio_margin_exceed`, `sale.order.line.x_studio_quotation_type`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (54 lines)</summary>

```python
# bugfix_sales:config-cutover-v22
if record.product_id.id:

  if record.x_studio_quotation_type != 'Project':

    value_1 = 0

    value_2 = 0

    

    min_magin = record.company_id

    

    

    if record.product_uom_qty > 0.00:

      value_1 = ((record.price_subtotal/record.product_uom_qty)-(record.price_subtotal*(record.x_studio_commission/100))-record.product_id.standard_price)

      value_2 = (record.price_subtotal/record.product_uom_qty)-(record.price_subtotal*(record.x_studio_commission/100))

    

    if value_2 > 0.00:

      net_margin = (value_1/value_2)*100

    else:

      net_margin = 0

      

    #if net_margin < 20:

    if net_margin != 0:

      if net_margin < min_magin.x_studio_minimum_sales_margin_:  

        record['x_studio_margin_exceed'] = True

      else:

        record['x_studio_margin_exceed'] = False

    else:

      record['x_studio_margin_exceed'] = False

  else:

    record['x_studio_margin_exceed'] = False
```
  </details>
- **SRM - Auto Populate Report Type in SO Lines** (`server_action_1729_srm_auto_populate_report_type_in_so_lines`, type `code`)
  - Function: Sets the sales order line's Sales Report Type to the record with hard-coded id 9.
  - Depends on: `model sale.order.line` (sale), `sale.order.line.x_studio_sales_report_type` (Jinasena_Masterdata_Reporting)
  - Used by: `automation BugFix-Sales.base_automation_118_srm_auto_populate_report_type_in_so_lines`
  <details><summary>code (2 lines)</summary>

```python
if record.id:
  record['x_studio_sales_report_type'] = 9
```
  </details>
- **Update Analytic Tag Parameters - Sales Line - Product** (`server_action_2416_update_analytic_tag_parameters_sales_line_product`, type `code`)
  - Function: Sets the line's Account Mandatory flag from the analytic distribution model for the product (Product Mandatory), else from the current user's model (User Mandatory), else False.
  - Depends on: `model account.analytic.distribution.model` (analytic), `model sale.order.line` (sale), `sale.order.line.product_id` (sale), `sale.order.line.x_studio_account_mandatory`
  - Used by: `automation BugFix-Sales.base_automation_236_update_analytic_tag_parameters_sales_line_product`
  <details><summary>code (11 lines)</summary>

```python
if record.product_id:
  #record['x_studio_account_mandatory'] = True
  tag_rule= env['account.analytic.distribution.model'].search([('product_id', '=', record.product_id.id)],limit=1)
  if tag_rule:
    record['x_studio_account_mandatory'] = tag_rule.x_studio_product_mandatory
  else:
    tag_rule2= env['account.analytic.distribution.model'].search([('partner_id.user_id', '=', uid)],limit=1)
    if tag_rule2:
      record['x_studio_account_mandatory'] = tag_rule2.x_studio_user_mandatory
    else:
      record['x_studio_account_mandatory'] = False
```
  </details>
**Automations (11):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| PROJ - Update Price Confirmed Status | `base_automation_342_proj_update_price_confirmed_status` |  | When a watched field changes in the form on Sales Order Line, runs _Execute Code_. | `model sale.order.line` (sale)<br>`sale.order.line.product_id` (sale)<br>`server action BugFix-Sales.server_action_2898_proj_update_price_confirmed_status` |  |
| PROJ-Item Related Details In Project SO | `base_automation_196_proj_item_related_details_in_project_so` |  | When a record is created or updated on Sales Order Line, runs _PROJ-Item Related Details In Project SO_. | `model sale.order.line` (sale)<br>`sale.order.line.create_date` (sale)<br>`server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so` |  |
| RR - Sales Price For RUG Items | `base_automation_193_rr_sales_price_for_rug_items` |  | When a record is created or updated on Sales Order Line, runs _Execute Code_. | `model sale.order.line` (sale)<br>`sale.order.line.create_date` (sale)<br>`server action BugFix-Sales.server_action_2144_rr_sales_price_for_rug_items` |  |
| RR - Track Lock Status - 3 | `base_automation_204_rr_track_lock_status_3` |  | When a watched field changes in the form on Sales Order Line and `[["x_studio_quotation_type","=","Repair"]]`, runs _Execute Code_. | `model sale.order.line` (sale)<br>`sale.order.line.product_id` (sale)<br>`sale.order.line.x_studio_quotation_type`<br>`server action BugFix-Sales.server_action_2252_rr_track_lock_status_3` |  |
| SLS - Apply Pricelist in SO Lines | `base_automation_212_sls_apply_pricelist_in_so_lines` |  | When a watched field changes in the form on Sales Order Line, runs _SLS - Apply Pricelist in SO Lines_. | `model sale.order.line` (sale)<br>`sale.order.line.product_id` (sale)<br>`sale.order.line.product_uom_qty` (sale)<br>`server action BugFix-Sales.server_action_2315_sls_apply_pricelist_in_so_lines` |  |
| SLS - Clear Free Items SO Lines | `base_automation_216_sls_clear_free_items_so_lines` | archived | When a watched field changes in the form on Sales Order Line and `[]`, runs nothing (no action linked). **Archived — does not run.** | `model sale.order.line` (sale) |  |
| SLS - Validate Commission in SO Line | `base_automation_90_sls_validate_commission_in_so_line` |  | When a watched field changes in the form on Sales Order Line, runs _SLS - Validate Commission in SO Line_. | `model sale.order.line` (sale)<br>`sale.order.line.discount` (sale)<br>`sale.order.line.x_studio_commission`<br>`server action BugFix-Sales.server_action_1498_sls_validate_commission_in_so_line` |  |
| SLS - Validate Discount in SO Line | `base_automation_89_sls_validate_discount_in_so_line` |  | When a watched field changes in the form on Sales Order Line, runs _SLS - Validate Discount in SO Line_. | `model sale.order.line` (sale)<br>`sale.order.line.discount` (sale)<br>`server action BugFix-Sales.server_action_1497_sls_validate_discount_in_so_line` |  |
| SLS - Validate Margin in SO Line | `base_automation_91_sls_validate_margin_in_so_line` | archived | When a watched field changes in the form on Sales Order Line, runs nothing (no action linked). **Archived — does not run.** | `model sale.order.line` (sale) |  |
| SRM - Auto Populate Report Type in SO Lines | `base_automation_118_srm_auto_populate_report_type_in_so_lines` |  | When a record is created or updated on Sales Order Line, runs _SRM - Auto Populate Report Type in SO Lines_. | `model sale.order.line` (sale)<br>`sale.order.line.create_date` (sale)<br>`server action BugFix-Sales.server_action_1729_srm_auto_populate_report_type_in_so_lines` |  |
| Update Analytic Tag Parameters - Sales Line - Product | `base_automation_236_update_analytic_tag_parameters_sales_line_product` |  | When a watched field changes in the form on Sales Order Line, runs _Update Analytic Tag Parameters - Sales Line - Product_. | `model sale.order.line` (sale)<br>`sale.order.line.product_id` (sale)<br>`server action BugFix-Sales.server_action_2416_update_analytic_tag_parameters_sales_line_product` |  |

**Window actions (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Line Items | `aw_f4_sale_order_line_line_items` | Opens **Sales Order Line** records (tree,form), filtered to `[('project_id', '=', active_id)]`. | `model sale.order.line` (sale)<br>`sale.order.line.project_id` (sale_project) |  |
| Line Items | `act_window_2193_line_items` | Opens **Sales Order Line** records (tree,form), filtered to `[('project_id', '=', active_id)]`. | `model sale.order.line` (sale)<br>`sale.order.line.project_id` (sale_project) |  |
| Line Items | `act_window_2194_line_items` | Opens **Sales Order Line** records (tree,form), filtered to `[('x_studio_project_no', '=', active_id)]`. | `model sale.order.line` (sale)<br>`sale.order.line.x_studio_project_no` |  |
| Line Items | `act_window_2195_line_items` | Opens **Sales Order Line** records (tree,form), filtered to `[('x_studio_main_project_2', '=', active_id)]`. | `model sale.order.line` (sale)<br>`sale.order.line.x_studio_main_project_2` |  |
| Sales - Production Request Status | `aw_f4_sale_order_line_sales_production_request_status` | Opens **Sales Order Line** records (tree,kanban,form,pivot). | `model sale.order.line` (sale) | `menu BugFix-Sales.menu_f6_sales_production_request_status` |
| Sales - Production Request Status | `act_window_2200_sales_production_request_status` | Opens **Sales Order Line** records (tree,kanban,form,pivot). | `model sale.order.line` (sale) | `menu BugFix-Sales.menu_1060_sales_production_request_status` |
| Sales Order Lines | `aw_f4_sale_order_line_sales_order_lines` | Opens **Sales Order Line** records (tree,form,pivot). | `model sale.order.line` (sale) |  |
| Sales Order Lines | `act_window_1568_sales_order_lines` | Opens **Sales Order Line** records (tree,form,pivot). | `model sale.order.line` (sale) | `menu BugFix-Sales.menu_832_sales_order_lines`<br>`menu BugFix-Sales.menu_f6_sales_order_lines` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default pivot view for ir.model(599,) | `ported_default_pivot_view_f_b434dca2_4958_4f97_b58e_a253d775c63c` | pivot | full pivot layout with 0 fields | Empty default pivot view for Sales Order Lines. |  |  |
| Default pivot view for ir.model(599,) | `view_3260_default_pivot_view_for_ir_model_599_e` | pivot | full pivot layout with 0 fields | Empty default pivot view for Sales Order Lines (duplicate of another ported default pivot). |  |  |
| Odoo Studio: sale.order.line.tree customization | `ported_view_3259_odoo_studio_sale_order_line_tree_customi` | tree | set string=Sales Order Ref on `//field[@name='order_id']`; after `//field[@name='order_partner_id']`: add field invoice_status, field warehouse_id; after `//tree[1]/field[@name='name']`: add field x_studio_price_unit_original; set string=Order Qty on `//field[@name='product_uom_qty']`; after `//field[@name='product_uom_qty']`: add field price_unit; set string=Delivered Qty on `//field[@name='qty_delivered']`; after `//field[@name='qty_delivered']`: add field qty_to_deliver; set string=Invoiced Qty on `//field[@name='qty_invoiced']` … | Sales order line list: renames columns (Sales Order Ref, Order Qty, Delivered Qty, Invoiced Qty, Qty To Invoice, UOM) and adds invoice status, unit price, quantity to deliver, discount, required qty, production completed, creator/date, category and project number. | `sale.order.line.discount` (sale)<br>`sale.order.line.invoice_status` (sale)<br>`sale.order.line.price_unit` (sale)<br>`sale.order.line.qty_to_deliver` (sale_stock)<br>`sale.order.line.warehouse_id` (sale_stock)<details><summary>+7 more</summary>`sale.order.line.x_studio_category`<br>`sale.order.line.x_studio_many2one_field_btM1W`<br>`sale.order.line.x_studio_price_unit_original`<br>`sale.order.line.x_studio_production_completed`<br>`sale.order.line.x_studio_project_no`<br>`sale.order.line.x_studio_req_qty`<br>`view sale.view_order_line_tree` (sale)</details> |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Project Manager Sales Orders Line | `rule_190_project_manager_sales_orders_line` | For Project / Administrator: read on Sales Order Line only where `['&', '&', ('state', 'in', ['sale', 'sale']), ('is_service', '=', True), '|', ('project_id', '!=', False), ('task_id', '!=', False)]`. | `group project.group_project_manager` (project)<br>`model sale.order.line` (sale)<br>`sale.order.line.is_service` (sale_service)<br>`sale.order.line.project_id` (sale_project)<br>`sale.order.line.state` (sale)<details><summary>+1 more</summary>`sale.order.line.task_id` (sale_project)</details> |  |
