# BugFix-Sales — `product.template`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.template` — Product

*Extends a model created by `product`.* Python: `models/product_template.py`.

Other repos that use this model: `automation BugFix-Accounting.base_automation_1_avoid_product_duplicate` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_270_test_access_rights` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_39_product_multi_company` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_445_public_product_template` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1387_imp_service_item_charge_duty_tax` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2587_jin_company_id_in_product` (BugFix-Accounting)<details><summary>+11 more</summary>`server action BugFix-Purchase.sa_f5_x_imports_ledger_setup_imp_update_cost_allocation_method_in_items` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1453_imp_update_cost_allocation_method_in_items` (BugFix-Purchase)<br>`server action BugFix-Studio-Misc.server_action_1743_sample_server_action` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2586_sample_server_action_to_get_company_id` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2831_mst_odoo_data_clean_up_001` (BugFix-Studio-Misc)<br>`window action BugFix-Accounting.act_window_2288_product_template` (BugFix-Accounting)<br>`window action BugFix-Accounting.act_window_2622_product_template` (BugFix-Accounting)<br>`window action BugFix-Accounting.aw_f4_product_template_product_template_1` (BugFix-Accounting)<br>`window action BugFix-Accounting.aw_f4_product_template_product_template` (BugFix-Accounting)<br>`x_product_test.x_studio_product_1` (BugFix-Studio-Misc)<br>`x_pump_price_costing.x_studio_product_id_1` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:product.template -->
This repo adds product fields such as Internal Product Type, Sub-Contract, Maximum Discount %, Melt Item, Tariff Code and item approval flags, shown on the product form and list. Request Item Approval and Approve Item buttons run the PLM item approval actions, which require an Internal Reference, set the approval flags on the product and its variant and notify users by activity. Automations set the product's Company, ensure only one service product per company for each Charge, Duty or Tax type, and copy or check the landed-cost split method against the Imports Ledger Setup; an unattached action blocks duplicate Internal References.
<!-- /SUMMARY -->

**Fields (15):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_binary_field_lN2B8` | New File | binary | Generic Studio file attachment on the product ('New File'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_binary_field_lN2B8_filename` | Filename for x_studio_binary_field_lN2B8 | char | Stores the file name of the product's 'New File' attachment. | stored |  |  |
| `x_studio_category_id` | Category ID | integer | Integer category ID stored on the product; shown in the product list view. | stored |  | `view BugFix-Sales.ported_view_3029_odoo_studio_product_template_product_tre` |
| `x_studio_char_field_zSfyl` | New Text | char | Unnamed Studio text field on the product ('New Text'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_clean` | Clean | boolean | 'Clean' checkbox on the product. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_item_approval_request_sent` | Item Approval Request Sent | boolean | Marks that an item approval request was sent for the product; set by the 'PLM Item Approval Request Sent' server action and used on the product form. | stored |  | `server action BugFix-Sales.server_action_2289_plm_item_approval_request_sent`<br>`view BugFix-Sales.ported_product_template_studio_2551` |
| `x_studio_item_approval_request_sent_prod` | Item Approval Request Sent Prod | boolean | Production 'item approval request sent' flag used on the product form. | stored |  | `view BugFix-Sales.ported_product_template_studio_2551` |
| `x_studio_item_approved` | Item Approved | boolean | Marks the product as approved; set by the 'PLM Item Approval' server action and used on the product form. | stored |  | `server action BugFix-Sales.server_action_2295_plm_item_approval`<br>`view BugFix-Sales.ported_product_template_studio_2551` |
| `x_studio_item_approved_prod` | Item Approved Prod | boolean | Production 'item approved' flag used on the product form. | stored |  | `view BugFix-Sales.ported_product_template_studio_2551` |
| `x_studio_many2one_field_8eWzY` | Pricelist | many2one → `product.pricelist` | Pricelist linked to the product. Not used by any view or logic in this repo. | stored | `model product.pricelist` (product) |  |
| `x_studio_maximum_discount` | Maximum  Discount % | float | Maximum discount percentage allowed for the product; entered on the product form. | stored |  | `view BugFix-Sales.ported_view_2551_odoo_studio_product_template_product_for` |
| `x_studio_melt_item` | Melt Item | boolean | Flags the product as a Melt Item; entered on the product form. | stored |  | `view BugFix-Sales.ported_view_2551_odoo_studio_product_template_product_for` |
| `x_studio_product_type` | Internal Product Type | selection: Motor=Motor; Other Products=Other Products; Vehicles=Vehicles; Pumps=Pumps; None=None | Internal product classification: Motor, Other Products, Vehicles, Pumps or None; has a default value record and appears on the product form and list. | stored |  | `default BugFix-Sales.default_586_product_template_x_studio_product_type`<br>`view BugFix-Sales.ported_view_2551_odoo_studio_product_template_product_for`<br>`view BugFix-Sales.ported_view_3029_odoo_studio_product_template_product_tre` |
| `x_studio_sub_contract` | Sub-Contract | boolean | Flags the product as a sub-contract item; entered on the product form. | stored |  | `view BugFix-Sales.ported_view_2551_odoo_studio_product_template_product_for` |
| `x_studio_tariff_code` | Tariff Code | many2one → `x_tariffmaster` | Customs tariff code of the product (link to Tariff Master), shown on the product form. | stored | `model x_tariffmaster` (BugFix-Stock) | `view BugFix-Sales.ported_product_template_studio_2551` |

**Server actions (13):**

- **Avoid Product Duplicate** (`server_action_808_avoid_product_duplicate`, type `code`)
  - Function: Raises 'Duplicate Found Try Another Code!' when another product in the current company already uses the same Internal Reference (case-insensitive). Not referenced by any automation in this repo.
  - Depends on: `model product.template` (product), `model res.company` (base), `product.template.default_code` (product)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (11 lines)</summary>

```python
if record.default_code:
  
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  product = env['product.template'].search([('default_code', '=ilike', record.default_code),('company_id', '=', company.id)], limit=1)
  
  if product:
    for p in product:
      if p.id != record.id:
        raise UserError("Duplicate Found Try Another Code!")
```
  </details>
- **IMP - Pass Split Method in Item Master** (`server_action_1452_imp_pass_split_method_in_item_master`, type `code`)
  - Function: For landed-cost products, copies the cost allocation method from the Imports Ledger Setup (record id 1) into the product's default split method.
  - Depends on: `model product.template` (product), `model x_imports_ledger_setup` (BugFix-Purchase), `product.template.landed_cost_ok` (stock_landed_costs)
  - Used by: `automation BugFix-Sales.base_automation_84_imp_pass_split_method_in_item_master`
  <details><summary>code (4 lines)</summary>

```python
if record.landed_cost_ok == True:
  def_split = env['x_imports_ledger_setup'].search([('id', '=', 1)], limit=1)
  if def_split:
    record['split_method_landed_cost'] = def_split.x_studio_cost_allocation_method
```
  </details>
- **IMP - Service Item - Charge-Duty-Tax** (`server_action_1387_imp_service_item_charge_duty_tax`, type `code`)
  - Function: For service products, ensures only one product per company is set up for each Charge/Duty/Tax type and billable/non-billable combination, raising an error on duplicates (Tax non-billable check is commented out).
  - Depends on: `model product.template` (product), `model res.company` (base), `product.template.type` (product), `product.template.x_studio_charge_type` (BugFix-Accounting), `product.template.x_studio_non_billable` (BugFix-Accounting)
  - Used by: `automation BugFix-Sales.base_automation_66_imp_service_item_charge_duty_tax`
  <details><summary>code (47 lines)</summary>

```python
if record.type == 'service':
  
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  if record.x_studio_charge_type == 'Charge' and record.x_studio_non_billable == False:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Charge'), ('x_studio_non_billable', '=', False),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Only One Service Item can be Setup as Charge/ Not Non Billable Item!")

  if record.x_studio_charge_type == 'Duty' and record.x_studio_non_billable == False:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Duty'), ('x_studio_non_billable', '=', False),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Duty/ Not Non Billable Item!")

  if record.x_studio_charge_type == 'Tax' and record.x_studio_non_billable == False:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Tax'), ('x_studio_non_billable', '=', False),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Tax/ Not Non Billable Item!")
          
          
  if record.x_studio_charge_type == 'Charge' and record.x_studio_non_billable == True:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Charge'), ('x_studio_non_billable', '=', True),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Charge/ Non Billable Item!")

  if record.x_studio_charge_type == 'Duty' and record.x_studio_non_billable == True:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Duty'), ('x_studio_non_billable', '=', True),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Duty/ Non Billable Item!")

  """if record.x_studio_charge_type == 'Tax' and record.x_studio_non_billable == True:
    product = env['product.template'].search([('x_studio_charge_type', '=', 'Tax'), ('x_studio_non_billable', '=', True),('company_id', '=', company.id)], limit=1)
    if product:
      for p in product:
        if p.id != record.id:
          raise UserError("Ony One Service Item can be Setup as Tax/ Non Billable Item!")"""
```
  </details>
- **IMP - Validate Default Split Method in Item Master** (`server_action_1451_imp_validate_default_split_method_in_item_master`, type `code`)
  - Function: For landed-cost products, raises an error if the product's default split method differs from the cost allocation method in the Imports Ledger Setup (record id 1).
  - Depends on: `model product.template` (product), `model x_imports_ledger_setup` (BugFix-Purchase), `product.template.landed_cost_ok` (stock_landed_costs), `product.template.split_method_landed_cost` (stock_landed_costs)
  - Used by: `automation BugFix-Sales.base_automation_83_imp_validate_default_split_method_in_item_master`
  <details><summary>code (5 lines)</summary>

```python
if record.landed_cost_ok == True:
  def_split = env['x_imports_ledger_setup'].search([('id', '=', 1)], limit=1)
  if def_split:
    if record.split_method_landed_cost != def_split.x_studio_cost_allocation_method:
      raise UserError('Default Split Method Should be Equal to Cost Allocation Method in Imports Ledger Setup')
```
  </details>
- **JIN - Company Id in Product** (`server_action_2587_jin_company_id_in_product`, type `code`)
  - Function: Sets the product's Company to the user's currently selected company.
  - Depends on: `model product.template` (product), `model res.company` (base)
  - Used by: `automation BugFix-Sales.base_automation_268_jin_company_id_in_product`
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['company_id'] = company.id
```
  </details>
- **PLM - Item Approval** (`server_action_2295_plm_item_approval`, type `code`)
  - Function: Marks the product template Item Approved and sets Item Approved (and its temp copy) on its variant; step of 'PLM - Item Approval - Final'.
  - Depends on: `model product.product` (product), `model product.template` (product), `product.template.product_variant_id` (product), `product.template.x_studio_item_approved`
  - Used by: `server action BugFix-Sales.server_action_2301_plm_item_approval_final`
  <details><summary>code (5 lines)</summary>

```python
record['x_studio_item_approved'] = True

product_product = env['product.product'].search([('id', '=', record.product_variant_id.id)],limit=1)
if product_product:
  product_product.write({'x_studio_item_approved':True,'x_studio_item_approved_temp':True})
```
  </details>
- **PLM - Item Approval - Final** (`server_action_2301_plm_item_approval_final`, type `multi`)
  - Function: Multi-step action behind the Approve Item button on the product form: runs child actions that approve the item, notify the project user and validate the approval.
  - Depends on: `model product.template` (product), `server action BugFix-Sales.server_action_2295_plm_item_approval`, `server action BugFix-Sales.server_action_2297_plm_item_approval_notify_project_user`, `server action BugFix-Sales.server_action_2299_plm_item_approval_validate`
  - Used by: `view BugFix-Sales.ported_product_template_studio_2551`
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
- **PLM - Item Approval - Notify  Project User** (`server_action_2297_plm_item_approval_notify_project_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the product to notify the project user that the item was approved; step of 'PLM - Item Approval - Final'.
  - Depends on: `model product.template` (product)
  - Used by: `server action BugFix-Sales.server_action_2301_plm_item_approval_final`
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
- **PLM - Item Approval - Validate** (`server_action_2299_plm_item_approval_validate`, type `code`)
  - Function: Raises an error if the product has no Internal Reference; step of 'PLM - Item Approval - Final'.
  - Depends on: `model product.template` (product), `product.template.default_code` (product)
  - Used by: `server action BugFix-Sales.server_action_2301_plm_item_approval_final`
  <details><summary>code (3 lines)</summary>

```python
if record.default_code == False:

  raise UserError("Internal Reference should be filled in to proceed!")
```
  </details>
- **PLM - Item Approval Request  Sent** (`server_action_2289_plm_item_approval_request_sent`, type `code`)
  - Function: Marks the product template Item Approval Request Sent and sets the same flag (and temp copy) on its variant; step of 'PLM - Request Item Approval'.
  - Depends on: `model product.product` (product), `model product.template` (product), `product.template.product_variant_id` (product), `product.template.x_studio_item_approval_request_sent`
  - Used by: `server action BugFix-Sales.server_action_2293_plm_request_item_approval`
  <details><summary>code (5 lines)</summary>

```python
record['x_studio_item_approval_request_sent'] = True

product_product = env['product.product'].search([('id', '=', record.product_variant_id.id)],limit=1)
if product_product:
  product_product.write({'x_studio_item_approval_request_sent':True,'x_studio_item_approval_request_sent_temp':True})
```
  </details>
- **PLM - Item Approval Request - Notify User** (`server_action_2291_plm_item_approval_request_notify_user`, type `next_activity`)
  - Function: Schedules an activity on the product to notify the approver of an item approval request; step of 'PLM - Request Item Approval'. Its code field oddly holds a mobile-number check, which is ignored for activity-type actions.
  - Depends on: `model product.template` (product)
  - Used by: `server action BugFix-Sales.server_action_2293_plm_request_item_approval`
  <details><summary>code (9 lines)</summary>

```python
if record.mobile:
    stripped = ''.join(c for c in str(record.mobile) if c.isdigit())
    # Blank / all-non-digit strings are allowed through — either a
    # legitimate empty field or a data-cleanup task, not our concern
    # here. Only enforce when the user has typed actual digits.
    if stripped and len(stripped) not in (10, 11, 12):
        raise UserError(
            'Invalid mobile number. Enter a valid mobile '
            '(10 digits, optionally with country code).')
```
  </details>
- **PLM - Request Item Approval** (`server_action_2293_plm_request_item_approval`, type `multi`)
  - Function: Multi-step action behind the Request Item Approval button on the product form: marks the item approval request as sent and notifies the approver via two child actions.
  - Depends on: `model product.template` (product), `server action BugFix-Sales.server_action_2289_plm_item_approval_request_sent`, `server action BugFix-Sales.server_action_2291_plm_item_approval_request_notify_user`
  - Used by: `view BugFix-Sales.ported_product_template_studio_2551`
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
- **Update Product Cost - Work Center Cost - 2** (`server_action_1142_update_product_cost_work_center_cost_2`, type `code`)
  - Function: Empty server action on product templates (no code); does nothing.
  - Depends on: `model product.template` (product)
  - Used by: — (not linked to a button, menu or automation)
**Automations (4):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Pass Split Method in Item Master | `base_automation_84_imp_pass_split_method_in_item_master` |  | When a watched field changes in the form on Product, runs _IMP - Pass Split Method in Item Master_. | `model product.template` (product)<br>`product.template.landed_cost_ok` (stock_landed_costs)<br>`server action BugFix-Sales.server_action_1452_imp_pass_split_method_in_item_master` |  |
| IMP - Service Item - Charge-Duty-Tax | `base_automation_66_imp_service_item_charge_duty_tax` |  | When a record is created or updated on Product, runs _IMP - Service Item - Charge-Duty-Tax_. | `model product.template` (product)<br>`server action BugFix-Sales.server_action_1387_imp_service_item_charge_duty_tax` |  |
| IMP - Validate Default Split Method in Item Master | `base_automation_83_imp_validate_default_split_method_in_item_master` |  | When a watched field changes in the form on Product, runs _IMP - Validate Default Split Method in Item Master_. | `model product.template` (product)<br>`product.template.split_method_landed_cost` (stock_landed_costs)<br>`server action BugFix-Sales.server_action_1451_imp_validate_default_split_method_in_item_master` |  |
| JIN - Company Id in Product | `base_automation_268_jin_company_id_in_product` |  | When a record is created or updated on Product, runs _JIN - Company Id in Product_. | `model product.template` (product)<br>`product.template.create_date` (product)<br>`server action BugFix-Sales.server_action_2587_jin_company_id_in_product` |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Product.Template | `act_window_2288_product_template` | Opens **Product** records (kanban,tree,form,activity). | `model product.template` (product) |  |
| Products | `act_window_204_products` | Opens **Product** records (tree,kanban,form). | `model product.template` (product) |  |
| product.template | `act_window_2622_product_template` | Opens **Product** records (kanban,tree,form,activity). | `model product.template` (product) |  |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: product.template.form customization | `ported_product_template_studio_2551` | form | inside `//form/sheet`: add field x_studio_item_approval_request_sent_prod, field x_studio_item_approval_request_sent, field x_studio_item_approved, field x_studio_item_approved_prod; inside `//header`: add button 'Request Item Approval', button 'Approve Item'; inside `//form/sheet/notebook`: add page 'Sri Lanka Localization' | Product form: adds Request Item Approval and Approve Item header buttons (shown depending on hidden request-sent/approved flags) and a 'Sri Lanka Localization' tab with Tariff Code. | `product.template.x_studio_item_approval_request_sent_prod`<br>`product.template.x_studio_item_approval_request_sent`<br>`product.template.x_studio_item_approved_prod`<br>`product.template.x_studio_item_approved`<br>`product.template.x_studio_tariff_code`<details><summary>+3 more</summary>`server action BugFix-Sales.server_action_2293_plm_request_item_approval`<br>`server action BugFix-Sales.server_action_2301_plm_item_approval_final`<br>`view product.product_template_form_view` (product)</details> | `view BugFix-Accounting.product_template_form_bugfix_accounting_field_content` (BugFix-Accounting) |
| Odoo Studio: product.template.product.form customization | `ported_view_2551_odoo_studio_product_template_product_for` | form | inside `//sheet`: add field type; set groups=product.group_product_pricelist on `//button[@name='open_pricelist_rules']`; set groups= on `//field[@name='is_published']`; set groups= on `//button[@name='action_view_stock_move_lines']`; set groups= on `//button[@name='action_open_product_lot']`; set invisible=type == 'service', required=type == 'service' on `//field[@name='invoice_policy']`; after `//field[@name='product_tooltip']`: add field x_studio_sub_contract; after `//field[@name='uom_po_id']`: add field x_studio_maximum_discount … | Product form: adds Sub-Contract, Maximum Discount %, Internal Product Type and Melt Item fields, makes Internal Reference required, hides invoicing policy for services, restricts Cost to a warning group and adjusts several button/page group restrictions. | `group base.group_multi_company` (base)<br>`group base.group_multi_currency` (base)<br>`group product.group_product_variant` (product)<br>`group uom.group_uom` (uom)<br>`product.template.company_id` (product)<details><summary>+8 more</summary>`product.template.currency_id` (product)<br>`product.template.sequence` (product)<br>`product.template.type` (product)<br>`product.template.x_studio_maximum_discount`<br>`product.template.x_studio_melt_item`<br>`product.template.x_studio_product_type`<br>`product.template.x_studio_sub_contract`<br>`view product.product_template_only_form_view` (product)</details> |  |
| Odoo Studio: product.template.product.tree customization | `ported_view_3029_odoo_studio_product_template_product_tre` | tree | after `//field[@name='priority']`: add xpath, field bom_ids; after `//tree[1]/field[@name='name']`: add xpath, field x_studio_product_type, xpath; set column_invisible=1 on `//field[@name='responsible_id']`; after `//field[@name='responsible_id']`: add field invoice_policy; after `//field[@name='uom_id']`: add field weight, field volume, field x_studio_category_id, field landed_cost_ok, field split_method_landed_cost, field id; set optional=show on `//field[@name='categ_id']` | Product list: reorders reference/category/tags, adds Internal Product Type, BoMs, invoicing policy, weight, volume, Category ID, landed-cost flags and ID; hides Responsible. | `product.template.bom_ids` (mrp)<br>`product.template.invoice_policy` (sale)<br>`product.template.landed_cost_ok` (stock_landed_costs)<br>`product.template.split_method_landed_cost` (stock_landed_costs)<br>`product.template.volume` (product)<details><summary>+4 more</summary>`product.template.weight` (product)<br>`product.template.x_studio_category_id`<br>`product.template.x_studio_product_type`<br>`view product.product_template_tree_view` (product)</details> |  |
| Odoo Studio: product.template.view.tree.website_sale customization | `ported_view_5445_odoo_studio_product_template_view_tree` | tree | after `//tree/field[@name='public_categ_ids']`: add field weight, field volume, field landed_cost_ok, field split_method_landed_cost | Website product list: adds weight, volume and landed-cost fields after the eCommerce categories. | `product.template.landed_cost_ok` (stock_landed_costs)<br>`product.template.split_method_landed_cost` (stock_landed_costs)<br>`product.template.volume` (product)<br>`product.template.weight` (product)<br>`view website_sale.product_template_view_tree_website_sale` (website_sale) |  |
