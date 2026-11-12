# BugFix-Sales — `product.product`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.product` — Product Variant

*Extends a model created by `product`.* Python: `models/product_product.py`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_product_product_group_system` (BugFix-Studio-Misc)<br>`account.move.line.x_studio_related_field_CQ41C` (BugFix-Accounting)<br>`helpdesk.ticket.x_studio_items` (Fix-repair)<br>`helpdesk.ticket.x_studio_materials_used` (Fix-repair)<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_production_purchase_report` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_slow_moving_items` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1370_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1374_imp_testing` (BugFix-Accounting)<details><summary>+39 more</summary>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1762_srm_rpt_slow_moving_items` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1763_srm_rpt_sales_production_purchase_report` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Purchase.server_action_991_update_pr_status_in_po` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice` (BugFix-Stock)<br>`x_bve.salesreport.x_bve_t2_product_id` (BugFix-Studio-Misc)<br>`x_consignment_charge_l.x_studio_product` (BugFix-Stock)<br>`x_consignment_line.x_studio_product_id` (BugFix-Stock)<br>`x_customer_posting_pro.x_studio_many2one_field_eYVbe` (BugFix-Accounting)<br>`x_import_rfq_charge_li.x_studio_product` (BugFix-Purchase)<br>`x_mass_produce_serial.x_studio_product_id` (BugFix-MRP)<br>`x_mass_produce_serial_.x_studio_product_id` (BugFix-MRP)<br>`x_mr_config.x_studio_many2one_field_02S0w` (BugFix-Stock)<br>`x_mr_config.x_studio_many2one_field_2LV9q` (BugFix-Stock)<br>`x_mr_config.x_studio_product` (BugFix-Stock)<br>`x_mrp_bom_material_cos.x_studio_product_id` (BugFix-MRP)<br>`x_pr_line_cash.x_studio_many2one_field_2Xthk` (BugFix-Purchase)<br>`x_product_test.x_studio_many2many_field_R1u9s` (BugFix-Studio-Misc)<br>`x_product_test.x_studio_many2one_field_cmfRx` (BugFix-Studio-Misc)<br>`x_pump_price_costing.x_studio_product_id` (BugFix-Accounting)<br>`x_purchase.request.line.make.purchase.order.item.x_cp_product_id` (BugFix-Purchase)<br>`x_purchase.request.line.make.purchase.order.item.x_product_id` (BugFix-Purchase)<br>`x_purchase_request_lin.x_studio_many2one_field_WAqP4` (BugFix-Purchase)<br>`x_rm_cust_invoice_s1.x_studio_product_id` (BugFix-Accounting)<br>`x_rm_daily_s1.x_studio_product_id` (BugFix-Accounting)<br>`x_rm_daily_s2.x_studio_product_id` (BugFix-Accounting)<br>`x_rm_daily_s3.x_studio_product_id` (BugFix-Accounting)<br>`x_rm_gross_margin_comp.x_studio_many2one_field_7fcuw` (BugFix-Accounting)<br>`x_rm_none_moving.x_studio_description` (BugFix-Accounting)<br>`x_rm_prod_summary_spli.x_studio_description` (BugFix-Accounting)<br>`x_rm_production_orders.x_studio_product_code` (BugFix-Accounting)<br>`x_rm_production_varian.x_studio_description_1` (BugFix-Accounting)<br>`x_rm_production_varian.x_studio_description` (BugFix-Accounting)<br>`x_rm_sales_order_line.x_studio_product_1` (BugFix-Accounting)<br>`x_rm_sales_prod_purch.x_studio_description` (BugFix-Accounting)<br>`x_temp_consignment_lin.x_studio_product_id` (BugFix-Stock)<br>`x_temp_estimated.x_studio_product_id` (BugFix-Accounting)<br>`x_test_layout.x_studio_product_id` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:product.product -->
This repo adds 43 Studio fields to product variants, most of them unused placeholders kept so migrated data loads (charge, duty, tax, melt, tariff code, maximum discount, internal product type and similar flags). The working part is the project item approval flow: the PROJ Request Item Approval and PROJ Item Approval multi-step actions mark the variant as requested or approved, check that it has an Internal Reference and schedule activities to notify the approver or project user. It also adds an Expense Account and ID column to the variant list and an Internal Reference column to the stock list.
<!-- /SUMMARY -->

**Fields (43):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_binary_field_lN2B8` | New File | binary | Generic Studio file attachment on the product variant ('New File'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_binary_field_lN2B8_filename` | Filename for x_studio_binary_field_lN2B8 | char | Stores the file name of the variant's 'New File' attachment. | stored |  |  |
| `x_studio_boolean_field_FFbpV` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_FxQqp` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_IsrsH` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_JKe77` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_JpVfJ` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_NjgGv` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_OA6o4` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_OmpWA` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_Q23qt` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_XrNz2` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_boolean_field_qKrKh` | New Checkbox | boolean | Unnamed Studio checkbox on the product variant ('New Checkbox'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_category_id` | Category ID | integer | Integer category ID stored on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_char_field_2ug_1iullp7gr` | New Text | char | Unnamed Studio text field on the product variant ('New Text'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_char_field_zSfyl` | New Text | char | Unnamed Studio text field on the product variant ('New Text'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_charge` | Charge | boolean | Flags the product variant as a Charge item. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_clean` | Clean | boolean | 'Clean' checkbox on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_duty` | Duty | boolean | Flags the product variant as a Duty item. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_float_field_KIV5v` | New Decimal | float | Unnamed Studio decimal field on the product variant ('New Decimal'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_item_approval_request_sent` | Item Approval Request Sent | boolean | Marks that an item approval request was sent for this product variant; set by the 'PROJ Item Approval Request Sent' server action. | stored |  | `server action BugFix-Sales.server_action_2163_proj_item_approval_request_sent` |
| `x_studio_item_approval_request_sent_2` | Item Approval Request Sent 2 | boolean | Secondary 'item approval request sent' flag on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_item_approval_request_sent_prod` | Item Approval Request Sent Prod | boolean | Production-variant 'item approval request sent' flag on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_item_approval_request_sent_temp` | Item Approval Request Sent Temp | boolean | Temporary 'item approval request sent' flag on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_item_approved` | Item Approved | boolean | Marks the product variant as approved as a project item; set by the 'PROJ Item Approval' server action. | stored |  | `server action BugFix-Sales.server_action_2169_proj_item_approval` |
| `x_studio_item_approved_prod` | Item Approved Prod | boolean | Production-variant 'item approved' flag on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_item_approved_temp` | Item Approved Temp | boolean | Temporary 'item approved' flag on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_many2one_field_8eWzY` | Pricelist | many2one → `product.pricelist` | Pricelist linked to the product variant; read by three related fields on journal items (account.move.line). | stored | `model product.pricelist` (product) | `account.move.line.x_studio_related_field_CvPMn` (BugFix-Accounting)<br>`account.move.line.x_studio_related_field_X2pdt` (BugFix-Accounting)<br>`account.move.line.x_studio_related_field_aD9tj` (BugFix-Accounting) |
| `x_studio_many2one_field_AS0wC` | TariffMaster | many2one → `x_tariffmaster` | Link from the product variant to a Tariff Master record. Not used by any view or logic in this repo. | stored | `model x_tariffmaster` (BugFix-Stock) |  |
| `x_studio_maximum_discount` | Maximum  Discount % | float | Maximum discount percentage allowed for the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_maximum_discount_` | Maximum  Discount % | float | Duplicate 'Maximum Discount %' field on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_melt` | Melt | boolean | 'Melt' checkbox on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_melt_item` | Melt Item | boolean | Flags the product variant as a Melt Item. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_product_type` | Internal Product Type | selection: Motor=Motor; Other Products=Other Products; Vehicles=Vehicles; Pumps=Pumps; None=None | Internal product classification on the variant: Motor, Other Products, Vehicles, Pumps or None. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_related_field_59m_1iv4fum1u` | New Related Field | boolean | Studio 'New Related Field' checkbox on the variant, ported as a plain boolean (no related path kept). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_related_field_850_1iv4flunc` | New Related Field | boolean | Studio 'New Related Field' checkbox on the variant, ported as a plain boolean (no related path kept). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_related_field_YoMQf` | New Related Field | integer | Studio 'New Related Field' integer on the variant, ported as a plain integer (no related path kept). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_selection_field_Coru2` | New Selection | selection | Unnamed Studio selection on the variant with no options declared in code. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_selection_field_MSMlW` | New Selection | selection | Unnamed Studio selection on the variant ('New Selection'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_serial` | Serial Number | char | Free-text serial number stored on the product variant. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_sub_contract` | Sub-Contract | boolean | Flags the product variant as a sub-contract item. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_tariff_code` | Tariff Code | many2one → `x_tariffmaster` | Customs tariff code of the product variant (link to Tariff Master). Not used by any view or logic in this repo. | stored | `model x_tariffmaster` (BugFix-Stock) |  |
| `x_studio_tax` | Tax | boolean | Flags the product variant as a Tax item. Not used by any view or logic in this repo. | stored |  |  |

**Server actions (7):**

- **PROJ - Item Approval** (`server_action_2169_proj_item_approval`, type `object_write`)
  - Function: Sets Item Approved to 'Yes' on the product variant; step of 'PROJ - Item Approval - Final'.
  - Depends on: `model product.product` (product), `product.product.x_studio_item_approved`
  - Used by: `server action BugFix-Sales.server_action_2173_proj_item_approval_final`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **PROJ - Item Approval - Final** (`server_action_2173_proj_item_approval_final`, type `multi`)
  - Function: Multi-step action on product variants that approves a project item, notifies the project user and validates the approval via three child actions. Not referenced by any active view or rule in this repo.
  - Depends on: `model product.product` (product), `server action BugFix-Sales.server_action_2169_proj_item_approval`, `server action BugFix-Sales.server_action_2171_proj_item_approval_validate`, `server action BugFix-Sales.server_action_2196_proj_item_approval_notify_project_user`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **PROJ - Item Approval - Notify  Project User** (`server_action_2196_proj_item_approval_notify_project_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the product variant to notify the project user that the item was approved; step of 'PROJ - Item Approval - Final'.
  - Depends on: `model product.product` (product)
  - Used by: `server action BugFix-Sales.server_action_2173_proj_item_approval_final`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **PROJ - Item Approval - Validate** (`server_action_2171_proj_item_approval_validate`, type `code`)
  - Function: Raises an error if the product variant has no Internal Reference; step of 'PROJ - Item Approval - Final'.
  - Depends on: `model product.product` (product), `product.product.default_code` (product)
  - Used by: `server action BugFix-Sales.server_action_2173_proj_item_approval_final`
  <details><summary>code (3 lines)</summary>

```python
if record.default_code == False:

  raise UserError("Internal Reference should be filled in to proceed!")
```
  </details>
- **PROJ - Item Approval Request  Sent** (`server_action_2163_proj_item_approval_request_sent`, type `object_write`)
  - Function: Sets Item Approval Request Sent to 'Yes' on the product variant; step of 'PROJ - Request Item Approval'.
  - Depends on: `model product.product` (product), `product.product.x_studio_item_approval_request_sent`
  - Used by: `server action BugFix-Sales.server_action_2167_proj_request_item_approval`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **PROJ - Item Approval Request - Notify User** (`server_action_2165_proj_item_approval_request_notify_user`, type `next_activity`)
  - Function: Schedules an activity on the product variant to notify the approver of an item approval request; step of 'PROJ - Request Item Approval'.
  - Depends on: `model product.product` (product)
  - Used by: `server action BugFix-Sales.server_action_2167_proj_request_item_approval`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **PROJ - Request Item Approval** (`server_action_2167_proj_request_item_approval`, type `multi`)
  - Function: Multi-step action on product variants that marks a project item approval request as sent and notifies the approver via two child actions. Not referenced by any active view in this repo (its product form button was stripped).
  - Depends on: `model product.product` (product), `server action BugFix-Sales.server_action_2163_proj_item_approval_request_sent`, `server action BugFix-Sales.server_action_2165_proj_item_approval_request_notify_user`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
**Window actions (6):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Expense Products | `act_window_1273_expense_products` | Opens **Product Variant** records (tree,kanban,form), filtered to `[('can_be_expensed', '=', True)]`. | `model product.product` (product)<br>`product.product.can_be_expensed` (hr_expense) |  |
| Product.product | `aw_f4_product_product_product_product_1` | Opens **Product Variant** records (kanban,tree,form,graph,activity). | `model product.product` (product) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_product_product` (BugFix-Studio-Misc) |
| Product.product | `act_window_1373_product_product` | Opens **Product Variant** records (kanban,tree,form,graph,activity). | `model product.product` (product) |  |
| product.product | `aw_f4_product_product_product_product` | Opens **Product Variant** records (kanban,tree,form,graph,activity). | `model product.product` (product) |  |
| product.product | `act_window_2588_product_product` | Opens **Product Variant** records (kanban,tree,form,graph,activity). | `model product.product` (product) | `menu BugFix-Studio-Misc.menu_f6f_product_product` (BugFix-Studio-Misc) |
| product.product | `act_window_2881_product_product` | Opens **Product Variant** records (kanban,tree,form,graph,activity). | `model product.product` (product) |  |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: product.product.form customization | `view_4936_odoo_studio_product_product_form_customization_e` | form |  | Inactive, empty view: its only change was stripped during migration, so it has no effect. | `view product.product_normal_form_view` (product) |  |
| Odoo Studio: product.product.product.form_button | `view_4935_odoo_studio_product_product_product_form_button_e` | form | before `//button[@name='action_open_label_layout']`: add | Inactive view with no effect: the project item approval buttons it added to the product variant form were stripped as unresolvable. | `view product.product_normal_form_view` (product) |  |
| Odoo Studio: product.product.stock.tree customization | `view_8329_odoo_studio_product_product_stock_tree_customization_e` | tree | after `//field[@name='id']`: add field default_code; after `//field[@name='incoming_qty']`: add | Product stock list: adds an optional Internal Reference column after ID (other Studio changes were stripped). | `product.product.default_code` (product)<br>`view stock.product_product_stock_tree` (stock) |  |
| Odoo Studio: product.product.tree customization | `ported_view_3030_odoo_studio_product_product_tree_customi` | tree | after `//field[@name='virtual_available']`: add field property_account_expense_id; after `//field[@name='uom_id']`: add field id | Product variant list: adds an Expense Account column and the ID. | `product.product.property_account_expense_id` (account)<br>`view product.product_product_tree_view` (product) |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| product.product group_system | `access_1218_product_product_group_system` | Gives **Administration / Settings** read/write/create/delete access to Product Variant records. | `group base.group_system` (base)<br>`model product.product` (product) |  |
| product.product group_user | `access_1219_product_product_group_user` | Gives **User types / Internal User** read access to Product Variant records. | `group base.group_user` (base)<br>`model product.product` (product) |  |
