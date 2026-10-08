# BugFix-Sales — `res.partner`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `res.partner` — Contact

*Extends a model created by `base`.* Python: `models/res_partner.py`, `models/res_partner_gap.py`.

Other repos that use this model: `account.move.line.x_studio_partner` (BugFix-Accounting)<br>`res.partner.x_studio_vendor_account` (Fix-repair)<br>`res.users.x_studio_many2many_field_f1lwc` (studio_usermodel_migration)<br>`res.users.x_studio_many2one_field_3xHed` (studio_usermodel_migration)<br>`res.users.x_studio_many2one_field_jhSr4` (studio_usermodel_migration)<br>`res.users.x_studio_many2one_field_pbZO1` (studio_usermodel_migration)<br>`res.users.x_studio_vendor_account` (Fix-repair)<br>`sale.order.create()` (Fix-repair)<details><summary>+126 more</summary>`sale.order.write()` (Fix-repair)<br>`server action BugFix-Accounting.server_action_1680_rpt_customer_wise_invoices_generate` (BugFix-Accounting)<br>`server action BugFix-Studio-Misc.server_action_2578_sample_server_action_multi_company` (BugFix-Studio-Misc)<br>`x_bve.salesreport.x_bve_t1_partner_id` (BugFix-Studio-Misc)<br>`x_con_consolidated_hea.message_partner_ids` (BugFix-Stock)<br>`x_con_consolidated_lin.message_partner_ids` (BugFix-Stock)<br>`x_con_consolidated_lin.x_studio_supplier_id` (BugFix-Stock)<br>`x_conditions.message_partner_ids` (Fix-repair)<br>`x_consignment_charge_h.message_partner_ids` (BugFix-Accounting)<br>`x_consignment_charge_l.message_partner_ids` (BugFix-Stock)<br>`x_consignment_header.message_partner_ids` (BugFix-Stock)<br>`x_consignment_header.x_studio_supplier_id` (BugFix-Stock)<br>`x_consignment_line.message_partner_ids` (BugFix-Stock)<br>`x_custom_reports.x_studio_partner_id` (BugFix-Custom-Reports)<br>`x_customer_group._compute_res_partner_count()` (studio_usermodel_migration)<br>`x_customer_group.message_partner_ids` (studio_usermodel_migration)<br>`x_customer_group.x_studio_one2many_field_hfDGm` (studio_usermodel_migration)<br>`x_customer_groups.message_partner_ids` (BugFix-Studio-Misc)<br>`x_delivery_term_charge.message_partner_ids` (BugFix-Purchase)<br>`x_departments.message_partner_ids` (BugFix-Project)<br>`x_diagnosis_areas.message_partner_ids` (Fix-repair)<br>`x_diagnosis_codes.message_partner_ids` (Fix-repair)<br>`x_import_charges.message_partner_ids` (BugFix-Purchase)<br>`x_import_rfq_charge_he.message_partner_ids` (BugFix-Purchase)<br>`x_import_rfq_charge_li.message_partner_ids` (BugFix-Purchase)<br>`x_imports_ledger_setup.message_partner_ids` (BugFix-Purchase)<br>`x_journal_types.message_partner_ids` (BugFix-Accounting)<br>`x_lc_header.x_studio_vendor` (BugFix-Accounting)<br>`x_material_request.message_partner_ids` (BugFix-Stock)<br>`x_material_request_m.x_studio_partner_id` (BugFix-MRP)<br>`x_material_request_mt.message_partner_ids` (BugFix-Stock)<br>`x_material_request_mt.x_studio_partner_id` (BugFix-Stock)<br>`x_material_request_tes.message_partner_ids` (BugFix-Stock)<br>`x_material_request_tes.x_studio_partner_id` (BugFix-Stock)<br>`x_misc_charge_codes.message_partner_ids` (BugFix-Accounting)<br>`x_mr_config.message_partner_ids` (BugFix-Stock)<br>`x_non_inventory_produc.message_partner_ids` (BugFix-Purchase)<br>`x_paye_tax.message_partner_ids` (BugFix-HR)<br>`x_payment_methods.message_partner_ids` (BugFix-Purchase)<br>`x_po_line_non_inventor.message_partner_ids` (BugFix-Purchase)<br>`x_po_line_non_inventor.x_studio_vendor` (BugFix-Purchase)<br>`x_po_non_inventory.message_partner_ids` (BugFix-Purchase)<br>`x_po_non_inventory.x_studio_vendor` (BugFix-Purchase)<br>`x_pr_line_cash.message_partner_ids` (BugFix-Purchase)<br>`x_pr_line_non_inventor.message_partner_ids` (BugFix-Purchase)<br>`x_pr_line_non_inventor.x_studio_last_po_vendor` (BugFix-Purchase)<br>`x_pr_non_inventory.message_partner_ids` (BugFix-Purchase)<br>`x_project_category.message_partner_ids` (BugFix-Project)<br>`x_project_category_gro.message_partner_ids` (BugFix-Project)<br>`x_project_groups.message_partner_ids` (BugFix-Project)<br>`x_pump_price_costing.message_partner_ids` (BugFix-Accounting)<br>`x_purchase.request.line.make.purchase.order.x_supplier_id` (BugFix-Purchase)<br>`x_purchase_request.message_partner_ids` (BugFix-Purchase)<br>`x_purchase_request_cas.message_partner_ids` (BugFix-Purchase)<br>`x_purchase_request_cas.x_studio_vendor` (BugFix-Purchase)<br>`x_purchase_request_lin.message_partner_ids` (BugFix-Purchase)<br>`x_purchase_request_lin.x_studio_last_po_vendor` (BugFix-Purchase)<br>`x_purchase_request_lin.x_studio_vendor_account` (BugFix-Purchase)<br>`x_purchase_request_mt.message_partner_ids` (BugFix-Purchase)<br>`x_purchase_request_mt.x_studio_partner_id` (BugFix-Purchase)<br>`x_purchase_request_t.message_partner_ids` (BugFix-Purchase)<br>`x_purchase_request_t.x_studio_partner_id` (BugFix-Purchase)<br>`x_repair_accounts.message_partner_ids` (Fix-repair)<br>`x_repair_reason.message_partner_ids` (Fix-repair)<br>`x_repair_reason_custom.message_partner_ids` (Fix-repair)<br>`x_repair_stages.message_partner_ids` (Fix-repair)<br>`x_repair_sub_reason.message_partner_ids` (Fix-repair)<br>`x_resolutions.message_partner_ids` (Fix-repair)<br>`x_rm_cust_invoice_s1.x_studio_partner` (BugFix-Accounting)<br>`x_rm_customer_wise_inv.x_studio_customer` (BugFix-Accounting)<br>`x_rm_daily_s1.message_partner_ids` (BugFix-Accounting)<br>`x_rm_daily_s1.x_studio_partner` (BugFix-Accounting)<br>`x_rm_daily_s2.message_partner_ids` (BugFix-Accounting)<br>`x_rm_daily_s2.x_studio_partner` (BugFix-Accounting)<br>`x_rm_daily_s3.message_partner_ids` (BugFix-Accounting)<br>`x_rm_daily_s3.x_studio_many2one_field_CiZHF` (BugFix-Accounting)<br>`x_rm_daily_sales_repor.message_partner_ids` (BugFix-Accounting)<br>`x_rm_date_test.message_partner_ids` (BugFix-Accounting)<br>`x_rm_gross_margin_esti.message_partner_ids` (BugFix-Accounting)<br>`x_rm_gross_margin_invo.message_partner_ids` (BugFix-Accounting)<br>`x_rm_none_moving.message_partner_ids` (BugFix-Accounting)<br>`x_rm_prod_summary_spli.message_partner_ids` (BugFix-Accounting)<br>`x_rm_production_orders.message_partner_ids` (BugFix-Accounting)<br>`x_rm_production_varian.message_partner_ids` (BugFix-Accounting)<br>`x_rm_sales_order_line.message_partner_ids` (BugFix-Accounting)<br>`x_rm_sales_order_line.x_studio_customer_acc` (BugFix-Accounting)<br>`x_rm_sales_prod_purch.message_partner_ids` (BugFix-Accounting)<br>`x_sales_model_debug.message_partner_ids` (BugFix-Studio-Misc)<br>`x_sales_report_model.message_partner_ids` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_customer` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.message_partner_ids` (Jinasena_Masterdata_Reporting)<br>`x_structure_details.message_partner_ids` (BugFix-Purchase)<br>`x_structure_master.message_partner_ids` (BugFix-Purchase)<br>`x_symptom_areas.message_partner_ids` (Fix-repair)<br>`x_symptom_codes.message_partner_ids` (Fix-repair)<br>`x_tariff_date.message_partner_ids` (BugFix-Purchase)<br>`x_tariff_rates.message_partner_ids` (BugFix-Purchase)<br>`x_tariffmaster.message_partner_ids` (BugFix-Stock)<br>`x_task_diagnosis.message_partner_ids` (Fix-repair)<br>`x_temp_con_conso_line.message_partner_ids` (BugFix-Stock)<br>`x_temp_con_conso_line.x_studio_supplier_id` (BugFix-Stock)<br>`x_temp_con_consolidate.message_partner_ids` (BugFix-Stock)<br>`x_temp_consignment_hea.message_partner_ids` (BugFix-Stock)<br>`x_temp_consignment_lin.message_partner_ids` (BugFix-Stock)<br>`x_temp_consignment_lin.x_studio_supplier_id` (BugFix-Stock)<br>`x_temp_estimated.message_partner_ids` (BugFix-Accounting)<br>`x_temp_estimated.x_studio_customer` (BugFix-Accounting)<br>`x_temp_structure_detai.message_partner_ids` (BugFix-Stock)<br>`x_temp_structure_maste.message_partner_ids` (BugFix-Stock)<br>`x_temp_tp_invoice_head.x_studio_supplier_id` (BugFix-Accounting)<br>`x_test_form.message_partner_ids` (BugFix-Studio-Misc)<br>`x_test_model_link.message_partner_ids` (BugFix-Studio-Misc)<br>`x_test_model_link_2.message_partner_ids` (BugFix-Studio-Misc)<br>`x_test_model_primary.message_partner_ids` (BugFix-Studio-Misc)<br>`x_tp_invoice_header.x_studio_vendor` (BugFix-Accounting)<br>`x_tp_invoice_line.message_partner_ids` (BugFix-Accounting)<br>`x_trf_charges.message_partner_ids` (BugFix-Purchase)<br>`x_trf_duty.message_partner_ids` (BugFix-Purchase)<br>`x_trf_taxes.message_partner_ids` (BugFix-Purchase)<br>`x_update_ot.message_partner_ids` (BugFix-HR)<br>`x_vendor_group._compute_res_partner_count()` (studio_usermodel_migration)<br>`x_vendor_group.message_partner_ids` (studio_usermodel_migration)<br>`x_vendor_group.x_studio_one2many_field_5cEfV` (studio_usermodel_migration)<br>`x_website_faq.message_partner_ids` (BugFix-Studio-Misc)<br>`x_website_faqs.message_partner_ids` (BugFix-Studio-Misc)<br>`x_work_center_costing.message_partner_ids` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:res.partner -->
This repo adds customer credit fields to contacts: Payment Type (Cash or Credit), Bank Guarantee Amount, Bank Guarantee Expiration Date, Valid Bank Guarantee and a Purchase Agreements count with smart button. Active automations set the contact's company and default pricelist, copy payment terms and accounts from the customer or vendor group, require a bank guarantee for Distributor customers, reset the credit limit for Cash customers, check the mobile number length and post chatter notes when name, address, tax and VAT numbers, group, payment term, pricelist, credit limit or bank guarantee details change. The contact form and list are reworked to show these fields, and record rules control which sales users may edit Cash and non-Cash customers.
<!-- /SUMMARY -->

**Fields (5):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_bank_guarantee_amount` | Bank Guarantee Amount | float | Bank guarantee amount held for the customer; used by the sales order over-bank-guarantee computes and the credit limit / customer group validation server actions. | stored |  | `res.users.x_studio_bank_guarantee_amount`<br>`sale.order._jin_compute_over_bank_guarantee()` (Fix-repair)<br>`sale.order._jin_compute_over_bank_guarantee_amount()` (Fix-repair)<br>`server action BugFix-Sales.sa_f5_res_partner_sls_validate_credit_limit_bank_guarantee_amount_1`<br>`server action BugFix-Sales.sa_f5_res_partner_sls_validate_credit_limit`<details><summary>+6 more</summary>`server action BugFix-Sales.server_action_1427_sls_validate_credit_limit`<br>`server action BugFix-Sales.server_action_1480_sls_validate_customer_group`<br>`server action BugFix-Sales.server_action_1768_sls_customer_group_not_in_general_validation`<br>`server action BugFix-Sales.server_action_1771_sls_validate_credit_limit_bank_guarantee_amount_1`<br>`server action BugFix-Sales.server_action_1772_sls_111111111`<br>`view BugFix-Sales.ported_view_2299_odoo_studio_res_partner_form_customizati`</details> |
| `x_studio_expiry_date` | Bank Guarantee Expiration Date | date | Expiry date of the customer's bank guarantee; tracked by an automation, mirrored to the sales order and used for the order's guarantee status and customer group validation. | stored |  | `automation BugFix-Sales.base_automation_167_sls_track_bank_guarantee_expiration_date_in_customer`<br>`res.users.x_studio_expiry_date`<br>`sale.order._fix_repair_compute_guarantee_status()` (Fix-repair)<br>`sale.order.x_studio_expiry_date`<br>`server action BugFix-Sales.server_action_1768_sls_customer_group_not_in_general_validation`<details><summary>+2 more</summary>`server action BugFix-Sales.server_action_1838_sls_track_bank_guarantee_expiration_date_in_customer`<br>`view BugFix-Sales.ported_view_2299_odoo_studio_res_partner_form_customizati`</details> |
| `x_studio_payment_method` | Payment Type | selection: Cash=Cash; Credit=Credit | Customer's payment type (Cash or Credit), entered on the contact form; validated and tracked by automations and copied to sales orders as Customer Payment Method for credit-limit checks. | stored |  | `automation BugFix-Sales.base_automation_158_sls_track_payment_type_in_customer`<br>`automation BugFix-Sales.base_automation_78_sls_validate_payment_method`<br>`res.users.x_studio_payment_method`<br>`sale.order.x_studio_customer_payment_method`<br>`server action BugFix-Sales.sa_f5_res_partner_sls_validate_credit_limit`<details><summary>+5 more</summary>`server action BugFix-Sales.server_action_1427_sls_validate_credit_limit`<br>`server action BugFix-Sales.server_action_1428_sls_validate_payment_method`<br>`server action BugFix-Sales.server_action_1829_sls_track_payment_type_in_customer`<br>`view BugFix-Sales.ported_view_2299_odoo_studio_res_partner_form_customizati`<br>`view BugFix-Studio-Misc.view_x_customer_group_form_studio_ext` (BugFix-Studio-Misc)</details> |
| `x_studio_valid_bank_guarantee` | Valid Bank Guarantee | boolean | True when the customer has an active (unexpired) bank guarantee; mirrored onto sales orders for credit-limit gates and used by the Validate Credit Limit server actions. | stored |  | `res.users.x_studio_valid_bank_guarantee`<br>`sale.order.x_studio_valid_bank_guarantee`<br>`server action BugFix-Sales.sa_f5_res_partner_sls_validate_credit_limit`<br>`server action BugFix-Sales.server_action_1427_sls_validate_credit_limit`<br>`view BugFix-Sales.ported_view_2299_odoo_studio_res_partner_form_customizati` |
| `x_vendor_id__purchase_requisition_count` | Vendor count | integer | Count of purchase requisitions where this partner is the vendor, computed by `_compute_x_vendor_id_pr_count` and shown as a smart button on the contact form. | not stored |  | `res.partner._compute_x_vendor_id_pr_count()`<br>`res.users.x_vendor_id__purchase_requisition_count`<br>`view BugFix-Sales.ported_view_2299_odoo_studio_res_partner_form_customizati` |

**Python methods (1):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_x_vendor_id_pr_count` | Computes how many purchase requisitions (purchase agreements) have this partner as vendor; returns 0 if the purchase_requisition model is not installed. | api.depends() |  | `res.partner.x_vendor_id__purchase_requisition_count` |  | `models/res_partner.py:40` |

**Server actions (40):**

- **Execute Code** (`server_action_810_sls_update_payment_term_customer`, type `code`)
  - Function: Run by the 'SLS - Update Payment Term - Customer' automation: copies the Customer Group's payment term and receivable account onto the contact.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_customer_group` (studio_usermodel_migration)
  - Used by: `automation BugFix-Sales.base_automation_2_sls_update_payment_term_customer`
  <details><summary>code (4 lines)</summary>

```python

if record.x_studio_customer_group.id:
  record['property_payment_term_id'] = record.x_studio_customer_group.x_studio_payment_term.id
  record['property_account_receivable_id'] = record.x_studio_customer_group.x_studio_receivable_account.id
```
  </details>
- **Execute Code** (`server_action_1427_sls_validate_credit_limit`, type `code`)
  - Function: Run by the 'SLS - Validate Credit Limit' automation: requires a Bank Guarantee Amount for Distributor-group customers and sets Valid Bank Guarantee according to whether the amount is above zero.
  - Depends on: `model res.partner` (base), `res.partner.credit_limit` (account), `res.partner.customer_rank` (account), `res.partner.x_studio_bank_guarantee_amount`, `res.partner.x_studio_group_type` (studio_usermodel_migration)<details><summary>+2 more</summary>`res.partner.x_studio_payment_method`, `res.partner.x_studio_valid_bank_guarantee`</details>
  - Used by: `automation BugFix-Sales.base_automation_77_sls_validate_credit_limit`
  <details><summary>code (12 lines)</summary>

```python

if record.id:
  #if record.customer_rank > 0 and record.x_studio_payment_method == 'Credit' and record.credit_limit < 1:
    #raise UserError('Invalid Credit Limit.')
    
  if record.customer_rank > 0 and record.x_studio_group_type == 'Distributor' and record.x_studio_bank_guarantee_amount == 0:
    raise UserError('Bank Guarantee Amount must be Specified for Distributors.')

  if record.x_studio_bank_guarantee_amount > 0.00:
    record['x_studio_valid_bank_guarantee'] = True
  else:
    record['x_studio_valid_bank_guarantee'] = False
```
  </details>
- **Execute Code** (`server_action_1518_sls_track_credit_limit_in_customer`, type `code`)
  - Function: Run by the 'SLS - Track Credit Limit in Customer' automation: posts a chatter note with the new credit limit whenever one is set.
  - Depends on: `model res.partner` (base), `res.partner.credit_limit` (account), `res.partner.name` (base)
  - Used by: `automation BugFix-Sales.base_automation_92_sls_track_credit_limit_in_customer`
  <details><summary>code (4 lines)</summary>

```python

if record.credit_limit:
  #records.message_post(body="Credit Limit Modified. --> " + record.name + "-->" + str(record.credit_limit))  #... No need to include the customer name in to the log record since the log is already within the customer.
  records.message_post(body="Credit Limit Modified. --> " + str(record.credit_limit))
```
  </details>
- **Execute Code** (`server_action_2828_jin_company_id_in_respartner_inherit_model`, type `code`)
  - Function: Run by its automation: sets the contact's Company to the user's currently selected company.
  - Depends on: `model res.company` (base), `model res.partner` (base)
  - Used by: `automation BugFix-Sales.base_automation_336_jin_company_id_in_respartner_inherit_model`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['company_id'] = company.id
```
  </details>
- **Execute Code** (`server_action_2891_jin_pricelist_in_respartner_inherit_model`, type `code`)
  - Function: Run by its automation: sets the contact's default pricelist to the current company's pricelist matching the contact's Group Type.
  - Depends on: `model product.pricelist` (product), `model res.company` (base), `model res.partner` (base), `res.partner.x_studio_group_type` (studio_usermodel_migration)
  - Used by: `automation BugFix-Sales.base_automation_340_jin_pricelist_in_respartner_inherit_model`
  <details><summary>code (7 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

pricelist = env['product.pricelist'].search([('x_studio_group_type', '=', record.x_studio_group_type),('company_id', '=', company.id)], limit=1) 
if pricelist:
  record['property_product_pricelist'] = pricelist.id
```
  </details>
- **JIN - Company Id in ResPartner Inherit Model** (`sa_f5_res_partner_jin_company_id_in_respartner_inherit_model`, type `code`)
  - Function: Sets the contact's Company to the user's currently selected company.
  - Depends on: `model res.company` (base), `model res.partner` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['company_id'] = company.id
```
  </details>
- **JIN - Pricelist in ResPartner Inherit Model** (`sa_f5_res_partner_jin_pricelist_in_respartner_inherit_model`, type `code`)
  - Function: Sets the contact's default pricelist to the current company's pricelist whose Group Type matches the contact's Group Type, if one exists.
  - Depends on: `model product.pricelist` (product), `model res.company` (base), `model res.partner` (base), `res.partner.x_studio_group_type` (studio_usermodel_migration)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (6 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

pricelist = env['product.pricelist'].search([('x_studio_group_type', '=', record.x_studio_group_type),('company_id', '=', company.id)], limit=1) 
if pricelist:
  record['property_product_pricelist'] = pricelist.id
```
  </details>
- **SLS - 111111111** (`server_action_1772_sls_111111111`, type `code`)
  - Function: Test-named action that posts a chatter note when the contact's credit limit is lower than the bank guarantee amount. Not referenced by any automation in this repo.
  - Depends on: `model res.partner` (base), `res.partner.credit_limit` (account), `res.partner.x_studio_bank_guarantee_amount`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python
if record.credit_limit < record.x_studio_bank_guarantee_amount:

  records.message_post(body="The bank guarantee amount is less than the credit limit." + "\n" + "Credit Limit--> " + str(record.credit_limit) + "\n" + "Bank Guarantee Amount--> " + str(record.x_studio_bank_guarantee_amount))
```
  </details>
- **SLS - Customer Group - Distributor - Mandatory Bank Guarantee** (`server_action_1767_sls_customer_group_distributor_mandatory_bank_guarantee`, type `code`)
  - Function: Sets Mandatory Bank Guarantee on the contact to True when its Customer Group type is Distributor, otherwise False.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_customer_group` (studio_usermodel_migration), `res.partner.x_studio_mandatory_bank_guarantee` (Fix-repair)
  - Used by: `automation BugFix-Sales.base_automation_139_sls_customer_group_distributor_mandatory_bank_guarantee`
  <details><summary>code (4 lines)</summary>

```python
if record.x_studio_customer_group.x_studio_group_type == 'Distributor':
  record['x_studio_mandatory_bank_guarantee'] = True
else:
  record['x_studio_mandatory_bank_guarantee'] = False
```
  </details>
- **SLS - Customer Group - not in General - Validation** (`server_action_1768_sls_customer_group_not_in_general_validation`, type `code`)
  - Function: Intended to require a Bank Guarantee Amount and Expiry Date for active customers in a non-General group, but the check compares the Customer Group record to True, so it never raises.
  - Depends on: `model res.partner` (base), `res.partner.active` (base), `res.partner.customer_rank` (account), `res.partner.x_studio_bank_guarantee_amount`, `res.partner.x_studio_customer_group` (studio_usermodel_migration)<details><summary>+1 more</summary>`res.partner.x_studio_expiry_date`</details>
  - Used by: `automation BugFix-Sales.base_automation_140_sls_customer_group_not_in_general_validation`
  <details><summary>code (9 lines)</summary>

```python
if record.active == True:
  if record.customer_rank > 0:
    if record.x_studio_customer_group == True:
      if record.x_studio_customer_group.x_studio_group_type != 'General':
        if record.x_studio_bank_guarantee_amount <= 0.00:
          raise UserError('Bank Guarantee Amount for the Selected Customer must be Defined.')
          
        if record.x_studio_expiry_date == False:
          raise UserError('Expiry Date of the Bank Guarantee Amount must be Defined.')
```
  </details>
- **SLS - Track  Address1 in Customer** (`server_action_1822_sls_track_address1_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new street when it is set.
  - Depends on: `model res.partner` (base), `res.partner.street` (base)
  - Used by: `automation BugFix-Sales.base_automation_151_sls_track_address1_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.street:
  records.message_post(body="Customer Address Modified. --> " + record.street)
```
  </details>
- **SLS - Track  Address2 in Customer** (`server_action_1823_sls_track_address2_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new city when it is set.
  - Depends on: `model res.partner` (base), `res.partner.city` (base)
  - Used by: `automation BugFix-Sales.base_automation_152_sls_track_address2_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.city:
  records.message_post(body="Customer Address Modified. --> " + record.city)
```
  </details>
- **SLS - Track  Address3 in Customer** (`server_action_1824_sls_track_address3_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new ZIP code when it is set.
  - Depends on: `model res.partner` (base), `res.partner.zip` (base)
  - Used by: `automation BugFix-Sales.base_automation_153_sls_track_address3_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.zip:
  records.message_post(body="Customer Address Modified. --> " + record.zip)
```
  </details>
- **SLS - Track  Address4 in Customer** (`server_action_1830_sls_track_address4_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new Street 2 when it is set.
  - Depends on: `model res.partner` (base), `res.partner.street2` (base)
  - Used by: `automation BugFix-Sales.base_automation_159_sls_track_address4_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.street2:
  records.message_post(body="Customer Address Modified. --> " + record.street2)
```
  </details>
- **SLS - Track  Address5 in Customer** (`server_action_1831_sls_track_address5_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new country name when it is set.
  - Depends on: `model res.partner` (base), `res.partner.country_id` (base)
  - Used by: `automation BugFix-Sales.base_automation_160_sls_track_address5_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.country_id:
  records.message_post(body="Customer Address Modified. --> " + record.country_id.name)
```
  </details>
- **SLS - Track  Bank Guarantee Expiration Date in Customer** (`server_action_1838_sls_track_bank_guarantee_expiration_date_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new bank guarantee expiry date.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_expiry_date`
  - Used by: `automation BugFix-Sales.base_automation_167_sls_track_bank_guarantee_expiration_date_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_expiry_date:
  records.message_post(body="Customer Bank Guarantee Expiration Date Modified. --> " + str(record.x_studio_expiry_date))
```
  </details>
- **SLS - Track  Customer Group in Customer** (`server_action_1826_sls_track_customer_group_in_customer`, type `code`)
  - Function: Posts a chatter note with the name of the customer's new Customer Group.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_customer_group` (studio_usermodel_migration)
  - Used by: `automation BugFix-Sales.base_automation_155_sls_track_customer_group_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_customer_group.x_name:
  records.message_post(body="Customer Group Modified. --> " + record.x_studio_customer_group.x_name)
```
  </details>
- **SLS - Track  Mandatory Bank Guarantee in Customer** (`server_action_1839_sls_track_mandatory_bank_guarantee_in_customer`, type `code`)
  - Function: Always posts a chatter note with the customer's current Mandatory Bank Guarantee value (True/False).
  - Depends on: `model res.partner` (base), `res.partner.x_studio_mandatory_bank_guarantee` (Fix-repair)
  - Used by: `automation BugFix-Sales.base_automation_168_sls_track_mandatory_bank_guarantee_in_customer`
  <details><summary>code (2 lines)</summary>

```python
#if record.x_studio_mandatory_bank_guarantee:
records.message_post(body="Customer Mandatory Bank Guarantee Modified. --> " + str(record.x_studio_mandatory_bank_guarantee))
```
  </details>
- **SLS - Track  Mobile in Customer** (`server_action_1832_sls_track_mobile_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new mobile number when it is set.
  - Depends on: `model res.partner` (base), `res.partner.mobile` (base)
  - Used by: `automation BugFix-Sales.base_automation_161_sls_track_mobile_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.mobile:
  records.message_post(body="Customer Mobile Modified. --> " + record.mobile)
```
  </details>
- **SLS - Track  Payment Term in Customer** (`server_action_1828_sls_track_payment_term_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new payment term name.
  - Depends on: `model res.partner` (base), `res.partner.property_payment_term_id` (account)
  - Used by: `automation BugFix-Sales.base_automation_157_sls_track_payment_term_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.property_payment_term_id.id:
  records.message_post(body="Customer Payment Term Modified. --> " + record.property_payment_term_id.name)
```
  </details>
- **SLS - Track  Payment Type in Customer** (`server_action_1829_sls_track_payment_type_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new payment method (payment type).
  - Depends on: `model res.partner` (base), `res.partner.x_studio_payment_method`
  - Used by: `automation BugFix-Sales.base_automation_158_sls_track_payment_type_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_payment_method:
  records.message_post(body="Customer Payment Type Modified. --> " + str(record.x_studio_payment_method))
```
  </details>
- **SLS - Track  Phone in Customer** (`server_action_1827_sls_track_phone_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new phone number. Not referenced by any automation in this repo.
  - Depends on: `model res.partner` (base), `res.partner.phone` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.phone:
  records.message_post(body="Customer Phone No Modified. --> " + record.phone)
```
  </details>
- **SLS - Track  Price List in Customer** (`server_action_1833_sls_track_price_list_in_customer`, type `code`)
  - Function: Posts a chatter note with the name of the customer's new pricelist.
  - Depends on: `model res.partner` (base), `res.partner.property_product_pricelist` (product)
  - Used by: `automation BugFix-Sales.base_automation_162_sls_track_price_list_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.property_product_pricelist:
  records.message_post(body="Customer Price List Modified. --> " + record.property_product_pricelist.name)
```
  </details>
- **SLS - Track  SVAT Registration No in Customer** (`server_action_1837_sls_track_svat_registration_no_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new SVAT Registration Number.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_svat_registration_number` (Fix-repair)
  - Used by: `automation BugFix-Sales.base_automation_166_sls_track_svat_registration_no_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_svat_registration_number:
  records.message_post(body="Customer SVAT Registration No Modified. --> " + record.x_studio_svat_registration_number)
```
  </details>
- **SLS - Track  SVAT Registration Status in Customer** (`server_action_1836_sls_track_svat_registration_status_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new SVAT Registration Status.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_svat_registration_status` (Fix-repair)
  - Used by: `automation BugFix-Sales.base_automation_165_sls_track_svat_registration_status_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_svat_registration_status:
  records.message_post(body="Customer SVAT Registration Status Modified. --> " + str(record.x_studio_svat_registration_status))
```
  </details>
- **SLS - Track  Tax ID in Customer** (`server_action_1825_sls_track_tax_id_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new Tax ID when it is set.
  - Depends on: `model res.partner` (base), `res.partner.vat` (base)
  - Used by: `automation BugFix-Sales.base_automation_154_sls_track_tax_id_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.vat:
  records.message_post(body="Customer Tax ID Modified. --> " + record.vat)
```
  </details>
- **SLS - Track  VAT Exempted Number in Customer** (`server_action_2037_sls_track_vat_exempted_number_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new VAT Exempted Number; the message text wrongly says 'VAT Registration Status Modified'.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_vat_exempted_number` (Fix-repair)
  - Used by: `automation BugFix-Sales.base_automation_180_sls_track_vat_exempted_number_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_vat_exempted_number:
  records.message_post(body="Customer VAT Registration Status Modified. --> " + str(record.x_studio_vat_exempted_number))
```
  </details>
- **SLS - Track  VAT Registration No in Customer** (`server_action_1835_sls_track_vat_registration_no_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new VAT Registration Number.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_vat_registration_number` (Fix-repair)
  - Used by: `automation BugFix-Sales.base_automation_164_sls_track_vat_registration_no_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_vat_registration_number:
  records.message_post(body="Customer VAT Registration No Modified. --> " + record.x_studio_vat_registration_number)
```
  </details>
- **SLS - Track  VAT Registration Status in Customer** (`server_action_1834_sls_track_vat_registration_status_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new VAT Registration Status.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_vat_registration_status` (Fix-repair)
  - Used by: `automation BugFix-Sales.base_automation_163_sls_track_vat_registration_status_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_vat_registration_status:
  records.message_post(body="Customer VAT Registration Status Modified. --> " + str(record.x_studio_vat_registration_status))
```
  </details>
- **SLS - Track Credit Limit in Customer** (`sa_f5_res_partner_sls_track_credit_limit_in_customer`, type `code`)
  - Function: Posts a chatter note on the customer with the new credit limit whenever a credit limit is set.
  - Depends on: `model res.partner` (base), `res.partner.credit_limit` (account), `res.partner.name` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python
if record.credit_limit:
  #records.message_post(body="Credit Limit Modified. --> " + record.name + "-->" + str(record.credit_limit))  #... No need to include the customer name in to the log record since the log is already within the customer.
  records.message_post(body="Credit Limit Modified. --> " + str(record.credit_limit))
```
  </details>
- **SLS - Track Name in Customer** (`server_action_1821_sls_track_name_in_customer`, type `code`)
  - Function: Posts a chatter note with the customer's new name when it is set.
  - Depends on: `model res.partner` (base), `res.partner.name` (base)
  - Used by: `automation BugFix-Sales.base_automation_150_sls_track_name_in_customer`
  <details><summary>code (2 lines)</summary>

```python
if record.name:
  records.message_post(body="Customer Name Modified. --> " + record.name)
```
  </details>
- **SLS - Update Payment Term - Customer** (`sa_f5_res_partner_sls_update_payment_term_customer`, type `code`)
  - Function: When the contact has a Customer Group, copies the group's payment term and receivable account onto the contact.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_customer_group` (studio_usermodel_migration)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python
if record.x_studio_customer_group.id:
  record['property_payment_term_id'] = record.x_studio_customer_group.x_studio_payment_term.id
  record['property_account_receivable_id'] = record.x_studio_customer_group.x_studio_receivable_account.id
```
  </details>
- **SLS - Update Payment Term - Vendor** (`server_action_1445_sls_update_payment_term_vendor`, type `code`)
  - Function: When the contact has a Vendor Group, copies the group's payment term and payable account onto the contact's vendor settings.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_vendor_group` (studio_usermodel_migration)
  - Used by: `automation BugFix-Sales.base_automation_82_sls_update_payment_term_vendor`
  <details><summary>code (3 lines)</summary>

```python
if record.x_studio_vendor_group.id:
  record['property_supplier_payment_term_id'] = record.x_studio_vendor_group.x_studio_payment_term.id
  record['property_account_payable_id'] = record.x_studio_vendor_group.x_studio_payable_account.id
```
  </details>
- **SLS - Validate Credit Limit** (`sa_f5_res_partner_sls_validate_credit_limit`, type `code`)
  - Function: For customers in a Distributor group, raises an error if no Bank Guarantee Amount is given; sets Valid Bank Guarantee to True when the amount is above zero, else False.
  - Depends on: `model res.partner` (base), `res.partner.credit_limit` (account), `res.partner.customer_rank` (account), `res.partner.x_studio_bank_guarantee_amount`, `res.partner.x_studio_group_type` (studio_usermodel_migration)<details><summary>+2 more</summary>`res.partner.x_studio_payment_method`, `res.partner.x_studio_valid_bank_guarantee`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (11 lines)</summary>

```python
if record.id:
  #if record.customer_rank > 0 and record.x_studio_payment_method == 'Credit' and record.credit_limit < 1:
    #raise UserError('Invalid Credit Limit.')
    
  if record.customer_rank > 0 and record.x_studio_group_type == 'Distributor' and record.x_studio_bank_guarantee_amount == 0:
    raise UserError('Bank Guarantee Amount must be Specified for Distributors.')

  if record.x_studio_bank_guarantee_amount > 0.00:
    record['x_studio_valid_bank_guarantee'] = True
  else:
    record['x_studio_valid_bank_guarantee'] = False
```
  </details>
- **SLS - Validate Credit Limit & Bank Guarantee Amount - 1** (`sa_f5_res_partner_sls_validate_credit_limit_bank_guarantee_amount_1`, type `code`)
  - Function: Posts a chatter warning on the contact when its credit limit is higher than its bank guarantee amount, showing both values.
  - Depends on: `model res.partner` (base), `res.partner.credit_limit` (account), `res.partner.x_studio_bank_guarantee_amount`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python
if record.credit_limit > record.x_studio_bank_guarantee_amount:

  records.message_post(body="The credit limit is higher than the bank guarantee amount." + "\n" + "Credit Limit: " + str(record.credit_limit) + "\n" + "Bank Guarantee Amount: " + str(record.x_studio_bank_guarantee_amount))
```
  </details>
- **SLS - Validate Credit Limit & Bank Guarantee Amount - 1** (`server_action_1771_sls_validate_credit_limit_bank_guarantee_amount_1`, type `code`)
  - Function: Run by its automation: posts a chatter warning when the contact's credit limit exceeds its bank guarantee amount, showing both values.
  - Depends on: `model res.partner` (base), `res.partner.credit_limit` (account), `res.partner.x_studio_bank_guarantee_amount`
  - Used by: `automation BugFix-Sales.base_automation_141_sls_validate_credit_limit_bank_guarantee_amount_1`
  <details><summary>code (4 lines)</summary>

```python

if record.credit_limit > record.x_studio_bank_guarantee_amount:

  records.message_post(body="The credit limit is higher than the bank guarantee amount." + "\n" + "Credit Limit: " + str(record.credit_limit) + "\n" + "Bank Guarantee Amount: " + str(record.x_studio_bank_guarantee_amount))
```
  </details>
- **SLS - Validate Customer Group** (`server_action_1480_sls_validate_customer_group`, type `code`)
  - Function: Resets the contact's Bank Guarantee Amount to 0. Not referenced by any automation in this repo.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_bank_guarantee_amount`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
record['x_studio_bank_guarantee_amount'] = 0
```
  </details>
- **SLS - Validate Mobile** (`server_action_2336_sls_validate_mobile`, type `code`)
  - Function: Raises 'Invalid mobile number' when a contact's mobile is filled in but is not exactly 10 characters.
  - Depends on: `model res.partner` (base), `res.partner.mobile` (base)
  - Used by: `automation BugFix-Sales.base_automation_218_sls_validate_mobile`
  <details><summary>code (7 lines)</summary>

```python
if record.mobile != False:

  if len(record.mobile) != 0:

    if len(record.mobile) != 10:

      raise UserError('Invalid mobile number.')
```
  </details>
- **SLS - Validate Payment Method** (`server_action_1428_sls_validate_payment_method`, type `code`)
  - Function: Resets the contact's credit limit to 0 when its payment method is 'Cash'.
  - Depends on: `model res.partner` (base), `res.partner.x_studio_payment_method`
  - Used by: `automation BugFix-Sales.base_automation_78_sls_validate_payment_method`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_payment_method == 'Cash':
  record['credit_limit'] = 0
```
  </details>
- **SLS - Validate Phone** (`server_action_2335_sls_validate_phone`, type `code`)
  - Function: Raises an error showing the length and value when a contact's phone is filled in but not exactly 10 characters. Not referenced by any automation in this repo.
  - Depends on: `model res.partner` (base), `res.partner.phone` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python
if record.phone and len(record.phone) != 10:

    raise UserError('Invalid phone number. - ' + str(len(record.phone)) + " - " + str(record.phone))
```
  </details>
**Automations (33):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in ResPartner Inherit Model | `base_automation_336_jin_company_id_in_respartner_inherit_model` |  | When a record is created or updated on Contact, runs _Execute Code_. | `model res.partner` (base)<br>`res.partner.create_date` (base)<br>`server action BugFix-Sales.server_action_2828_jin_company_id_in_respartner_inherit_model` |  |
| JIN - Pricelist in ResPartner Inherit Model | `base_automation_340_jin_pricelist_in_respartner_inherit_model` |  | When a watched field changes in the form on Contact, runs _Execute Code_. | `model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<br>`server action BugFix-Sales.server_action_2891_jin_pricelist_in_respartner_inherit_model` |  |
| SLS - Customer Group - Distributor - Mandatory Bank Guarantee | `base_automation_139_sls_customer_group_distributor_mandatory_bank_guarantee` |  | When a watched field changes in the form on Contact, runs _SLS - Customer Group - Distributor - Mandatory Bank Guarantee_. | `model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<br>`server action BugFix-Sales.server_action_1767_sls_customer_group_distributor_mandatory_bank_guarantee` |  |
| SLS - Customer Group - not in General - Validation | `base_automation_140_sls_customer_group_not_in_general_validation` |  | When a record is created or updated on Contact, runs _SLS - Customer Group - not in General - Validation_. | `model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<br>`server action BugFix-Sales.server_action_1768_sls_customer_group_not_in_general_validation` |  |
| SLS - Track  Address1 in Customer | `base_automation_151_sls_track_address1_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Address1 in Customer_. | `model res.partner` (base)<br>`res.partner.street` (base)<br>`server action BugFix-Sales.server_action_1822_sls_track_address1_in_customer` |  |
| SLS - Track  Address2 in Customer | `base_automation_152_sls_track_address2_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Address2 in Customer_. | `model res.partner` (base)<br>`res.partner.city` (base)<br>`server action BugFix-Sales.server_action_1823_sls_track_address2_in_customer` |  |
| SLS - Track  Address3 in Customer | `base_automation_153_sls_track_address3_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Address3 in Customer_. | `model res.partner` (base)<br>`res.partner.zip` (base)<br>`server action BugFix-Sales.server_action_1824_sls_track_address3_in_customer` |  |
| SLS - Track  Address4 in Customer | `base_automation_159_sls_track_address4_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Address4 in Customer_. | `model res.partner` (base)<br>`res.partner.street2` (base)<br>`server action BugFix-Sales.server_action_1830_sls_track_address4_in_customer` |  |
| SLS - Track  Address5 in Customer | `base_automation_160_sls_track_address5_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Address5 in Customer_. | `model res.partner` (base)<br>`res.partner.country_id` (base)<br>`server action BugFix-Sales.server_action_1831_sls_track_address5_in_customer` |  |
| SLS - Track  Bank Guarantee Expiration Date in Customer | `base_automation_167_sls_track_bank_guarantee_expiration_date_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Bank Guarantee Expiration Date in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_expiry_date`<br>`server action BugFix-Sales.server_action_1838_sls_track_bank_guarantee_expiration_date_in_customer` |  |
| SLS - Track  Customer Group in Customer | `base_automation_155_sls_track_customer_group_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Customer Group in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<br>`server action BugFix-Sales.server_action_1826_sls_track_customer_group_in_customer` |  |
| SLS - Track  Mandatory Bank Guarantee in Customer | `base_automation_168_sls_track_mandatory_bank_guarantee_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Mandatory Bank Guarantee in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_mandatory_bank_guarantee` (Fix-repair)<br>`server action BugFix-Sales.server_action_1839_sls_track_mandatory_bank_guarantee_in_customer` |  |
| SLS - Track  Mobile in Customer | `base_automation_161_sls_track_mobile_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Mobile in Customer_. | `model res.partner` (base)<br>`res.partner.mobile` (base)<br>`server action BugFix-Sales.server_action_1832_sls_track_mobile_in_customer` |  |
| SLS - Track  Payment Term in Customer | `base_automation_157_sls_track_payment_term_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Payment Term in Customer_. | `model res.partner` (base)<br>`res.partner.property_payment_term_id` (account)<br>`server action BugFix-Sales.server_action_1828_sls_track_payment_term_in_customer` |  |
| SLS - Track  Payment Type in Customer | `base_automation_158_sls_track_payment_type_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Payment Type in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_payment_method`<br>`server action BugFix-Sales.server_action_1829_sls_track_payment_type_in_customer` |  |
| SLS - Track  Phone in Customer | `base_automation_156_sls_track_phone_in_customer` | archived | When a record is created or updated on Contact, runs nothing (no action linked). **Archived — does not run.** | `model res.partner` (base) |  |
| SLS - Track  Price List in Customer | `base_automation_162_sls_track_price_list_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Price List in Customer_. | `model res.partner` (base)<br>`res.partner.property_product_pricelist` (product)<br>`server action BugFix-Sales.server_action_1833_sls_track_price_list_in_customer` |  |
| SLS - Track  SVAT Registration No in Customer | `base_automation_166_sls_track_svat_registration_no_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  SVAT Registration No in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_svat_registration_number` (Fix-repair)<br>`server action BugFix-Sales.server_action_1837_sls_track_svat_registration_no_in_customer` |  |
| SLS - Track  SVAT Registration Status in Customer | `base_automation_165_sls_track_svat_registration_status_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  SVAT Registration Status in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_svat_registration_status` (Fix-repair)<br>`server action BugFix-Sales.server_action_1836_sls_track_svat_registration_status_in_customer` |  |
| SLS - Track  Tax ID in Customer | `base_automation_154_sls_track_tax_id_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  Tax ID in Customer_. | `model res.partner` (base)<br>`res.partner.vat` (base)<br>`server action BugFix-Sales.server_action_1825_sls_track_tax_id_in_customer` |  |
| SLS - Track  VAT Exempted Number in Customer | `base_automation_180_sls_track_vat_exempted_number_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  VAT Exempted Number in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_vat_exempted_number` (Fix-repair)<br>`server action BugFix-Sales.server_action_2037_sls_track_vat_exempted_number_in_customer` |  |
| SLS - Track  VAT Registration No in Customer | `base_automation_164_sls_track_vat_registration_no_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  VAT Registration No in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_vat_registration_number` (Fix-repair)<br>`server action BugFix-Sales.server_action_1835_sls_track_vat_registration_no_in_customer` |  |
| SLS - Track  VAT Registration Status in Customer | `base_automation_163_sls_track_vat_registration_status_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track  VAT Registration Status in Customer_. | `model res.partner` (base)<br>`res.partner.x_studio_vat_registration_status` (Fix-repair)<br>`server action BugFix-Sales.server_action_1834_sls_track_vat_registration_status_in_customer` |  |
| SLS - Track Credit Limit in Customer | `base_automation_92_sls_track_credit_limit_in_customer` |  | When a record is created or updated on Contact, runs _Execute Code_. | `model res.partner` (base)<br>`res.partner.credit_limit` (account)<br>`server action BugFix-Sales.server_action_1518_sls_track_credit_limit_in_customer` |  |
| SLS - Track Name in Customer | `base_automation_150_sls_track_name_in_customer` |  | When a record is created or updated on Contact, runs _SLS - Track Name in Customer_. | `model res.partner` (base)<br>`res.partner.name` (base)<br>`server action BugFix-Sales.server_action_1821_sls_track_name_in_customer` |  |
| SLS - Update Payment Term - Customer | `base_automation_2_sls_update_payment_term_customer` |  | When a watched field changes in the form on Contact and `[["x_studio_customer_group","!=",False]]`, runs _Execute Code_. | `model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<br>`server action BugFix-Sales.server_action_810_sls_update_payment_term_customer` |  |
| SLS - Update Payment Term - Vendor | `base_automation_82_sls_update_payment_term_vendor` |  | When a watched field changes in the form on Contact and `[["x_studio_customer_group","!=",False]]`, runs _SLS - Update Payment Term - Vendor_. | `model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<br>`res.partner.x_studio_vendor_group` (studio_usermodel_migration)<br>`server action BugFix-Sales.server_action_1445_sls_update_payment_term_vendor` |  |
| SLS - Validate Credit Limit | `base_automation_77_sls_validate_credit_limit` |  | When a record is created or updated on Contact, runs _Execute Code_. | `model res.partner` (base)<br>`server action BugFix-Sales.server_action_1427_sls_validate_credit_limit` |  |
| SLS - Validate Credit Limit & Bank Guarantee Amount - 1 | `base_automation_141_sls_validate_credit_limit_bank_guarantee_amount_1` | archived | When a watched field changes in the form on Contact, runs _SLS - Validate Credit Limit & Bank Guarantee Amount - 1_. **Archived — does not run.** | `model res.partner` (base)<br>`server action BugFix-Sales.server_action_1771_sls_validate_credit_limit_bank_guarantee_amount_1` |  |
| SLS - Validate Customer Group | `base_automation_88_sls_validate_customer_group` | archived | When a watched field changes in the form on Contact, runs nothing (no action linked). **Archived — does not run.** | `model res.partner` (base) |  |
| SLS - Validate Mobile | `base_automation_218_sls_validate_mobile` |  | When a watched field changes in the form on Contact, runs _SLS - Validate Mobile_. | `model res.partner` (base)<br>`res.partner.mobile` (base)<br>`server action BugFix-Sales.server_action_2336_sls_validate_mobile` |  |
| SLS - Validate Payment Method | `base_automation_78_sls_validate_payment_method` |  | When a watched field changes in the form on Contact, runs _SLS - Validate Payment Method_. | `model res.partner` (base)<br>`res.partner.x_studio_payment_method`<br>`server action BugFix-Sales.server_action_1428_sls_validate_payment_method` |  |
| SLS - Validate Phone | `base_automation_217_sls_validate_phone` | archived | When a watched field changes in the form on Contact, runs nothing (no action linked). **Archived — does not run.** | `model res.partner` (base) |  |

**Window actions (12):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Customers | `aw_f4_res_partner_customers` | Opens **Contact** records (tree,form), filtered to `[('x_studio_customer_group', '=', active_id)]`. | `model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration) |  |
| Customers | `act_window_1447_customers` | Opens **Contact** records (tree,form), filtered to `[('x_studio_customer_group', '=', active_id)]`. | `model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration) |  |
| Customers of this group | `aw_f4_res_partner_customers_of_this_group` | Opens **Contact** records (tree,form), filtered to `[('x_studio_many2one_field_3LBKs', '=', active_id)]`. | `model res.partner` (base) |  |
| Customers of this group | `act_window_782_customers_of_this_group` | Opens **Contact** records (tree,form), filtered to `[('x_studio_many2one_field_3LBKs', '=', active_id)]`. | `model res.partner` (base) |  |
| Customers of this group: | `aw_f4_res_partner_customers_of_this_group_1` | Opens **Contact** records (tree,form), filtered to `[('x_studio_many2one_field_3LBKs', '=', active_id)]`. | `model res.partner` (base) |  |
| Customers of this group: | `act_window_783_customers_of_this_group` | Opens **Contact** records (tree,form), filtered to `[('x_studio_many2one_field_3LBKs', '=', active_id)]`. | `model res.partner` (base) |  |
| New Button | `aw_f4_res_partner_new_button` | Opens **Contact** records (tree,form), filtered to `[('x_studio_many2one_field_3LBKs', '=', active_id)]`. | `model res.partner` (base) |  |
| New Button | `act_window_781_new_button` | Opens **Contact** records (tree,form), filtered to `[('x_studio_many2one_field_3LBKs', '=', active_id)]`. | `model res.partner` (base) |  |
| Vendors | `aw_f4_res_partner_vendors` | Opens **Contact** records (tree,form), filtered to `[('x_studio_vendor_group', '=', active_id)]`. | `model res.partner` (base)<br>`res.partner.x_studio_vendor_group` (studio_usermodel_migration) |  |
| Vendors | `act_window_1448_vendors` | Opens **Contact** records (tree,form), filtered to `[('x_studio_vendor_group', '=', active_id)]`. | `model res.partner` (base)<br>`res.partner.x_studio_vendor_group` (studio_usermodel_migration) |  |
| res.partner | `aw_f4_res_partner_res_partner` | Opens **Contact** records (kanban,tree,form,map,activity). | `model res.partner` (base) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_res_partner` (BugFix-Studio-Misc) |
| res.partner | `act_window_1425_res_partner` | Opens **Contact** records (kanban,tree,form,map,activity). | `model res.partner` (base) |  |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: res.partner.form customization | `ported_view_2299_odoo_studio_res_partner_form_customizati` | form | inside `//sheet`: add field is_coa_installed, field parent_id, field type; after `//button[@name='action_see_documents']`: add button '1696'; set readonly=(type == 'contact' and parent_id) or ((parent_id != False) and (type == 'contact')), required=((x_studio_payment_method == 'Credit') and (x_studio_group_type != 'Dealer')) or (x_studio_group_type == 'Dealer') on `//form[1]/sheet[1]/group[1]/group[1]/div[1]/field[@name='street']`; set invisible=True, readonly=(type == 'contact' and parent_id) or ((parent_id != False) and (type == 'contact')) on `//form[1]/sheet[1]/group[1]/group[1]/div[1]/field[@name='street2']`; set invisible=True, readonly=(type == 'contact' and parent_id) or ((parent_id != False) and (type == 'contact')) on `//form[1]/sheet[1]/group[1]/group[1]/div[1]/field[@name='city']`; set readonly=(parent_id) or (parent_id != False), required=((x_studio_payment_method == 'Credit') and (x_studio_group_type != 'Dealer')) or (x_studio_group_type == 'Dealer') on `//field[@name='vat']`; after `//field[@name='vat']`: add field x_studio_customer_group, field x_studio_vendor_group; set required=False on `//form[1]/sheet[1]/group[1]/group[2]/div[2]/field[@name='mobile']` … | Contact form: adds a Purchase Agreements smart button, customer/vendor group fields, payment method, credit limit/overdue and bank-guarantee fields; makes street and VAT required for credit or dealer customers, hides street2/city and locks address on child contacts. | `group base.group_multi_company` (base)<br>`group base.group_multi_currency` (base)<br>`res.partner.active` (base)<br>`res.partner.company_id` (base)<br>`res.partner.contact_address_complete` (web_map)<details><summary>+19 more</summary>`res.partner.credit_limit` (account)<br>`res.partner.credit` (account)<br>`res.partner.currency_id` (test_access_rights)<br>`res.partner.customer_rank` (account)<br>`res.partner.is_coa_installed` (account)<br>`res.partner.parent_id` (base)<br>`res.partner.supplier_rank` (account)<br>`res.partner.total_overdue` (account_followup)<br>`res.partner.type` (base)<br>`res.partner.x_studio_bank_guarantee_amount`<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<br>`res.partner.x_studio_expiry_date`<br>`res.partner.x_studio_group_type` (studio_usermodel_migration)<br>`res.partner.x_studio_payment_method`<br>`res.partner.x_studio_valid_bank_guarantee`<br>`res.partner.x_studio_vendor_group` (studio_usermodel_migration)<br>`res.partner.x_vendor_id__purchase_requisition_count`<br>`view base.view_partner_form` (base)<br>`window action sale_renting_sign.rental_sign_documents` (sale_renting_sign)</details> | `view Fix-repair.res_partner_form_fix_repair_field_content` (Fix-repair) |
| Odoo Studio: res.partner.tree customization | `ported_view_2300_odoo_studio_res_partner_tree_customizati` | tree | remove `//field[@name='user_id']`; remove `//field[@name='email']`; remove `//field[@name='phone']`; before `//field[@name='display_name']`: add field self, field x_studio_customer_group, field x_studio_vendor_group, field company_registry, field title, field total_overdue, field total_due, field credit, field user_ids, field commercial_company_name, field create_uid, field create_date …; after `//field[@name='display_name']`: add field company_name, field partner_gid, field ref_company_ids, field commercial_partner_id, field color, field channel_ids, field message_bounce, field phone_blacklisted, field mobile_blacklisted, field is_blacklisted, field barcode, field bank_ids …; after `//field[@name='state_id']`: add xpath, field id; set optional=, readonly= on `//field[@name='country_id']` | Contacts list: removes salesperson, email and phone, and adds many columns such as customer/vendor group, registry, overdue, due, credit, credit limit, payment terms, ranks and address details. | `res.partner.account_represented_company_ids` (account_reports)<br>`res.partner.active_lang_count` (base)<br>`res.partner.additional_info` (partner_autocomplete)<br>`res.partner.bank_account_count` (account)<br>`res.partner.bank_ids` (base)<details><summary>+47 more</summary>`res.partner.barcode` (base)<br>`res.partner.channel_ids` (mail)<br>`res.partner.child_ids` (base)<br>`res.partner.color` (base)<br>`res.partner.commercial_company_name` (base)<br>`res.partner.commercial_partner_id` (base)<br>`res.partner.company_name` (base)<br>`res.partner.company_registry` (base)<br>`res.partner.company_type` (base)<br>`res.partner.contact_address_complete` (web_map)<br>`res.partner.contact_address` (base)<br>`res.partner.credit_limit` (account)<br>`res.partner.credit` (account)<br>`res.partner.currency_id` (test_access_rights)<br>`res.partner.customer_rank` (account)<br>`res.partner.date` (base)<br>`res.partner.is_blacklisted` (mail)<br>`res.partner.meeting_count` (calendar)<br>`res.partner.message_attachment_count` (mail)<br>`res.partner.message_bounce` (mail)<br>`res.partner.message_needaction` (mail)<br>`res.partner.mobile_blacklisted` (sms)<br>`res.partner.partner_gid` (partner_autocomplete)<br>`res.partner.payment_token_count` (payment)<br>`res.partner.phone_blacklisted` (sms)<br>`res.partner.property_account_payable_id` (account)<br>`res.partner.property_account_receivable_id` (account)<br>`res.partner.property_payment_term_id` (account)<br>`res.partner.property_stock_customer` (stock)<br>`res.partner.property_supplier_payment_term_id` (account)<br>`res.partner.ref_company_ids` (account)<br>`res.partner.ref` (base)<br>`res.partner.self` (base)<br>`res.partner.signature_count` (sign)<br>`res.partner.supplier_invoice_count` (account)<br>`res.partner.supplier_rank` (account)<br>`res.partner.task_count` (project)<br>`res.partner.task_ids` (project)<br>`res.partner.title` (base)<br>`res.partner.total_due` (account_followup)<br>`res.partner.total_invoiced` (account)<br>`res.partner.total_overdue` (account_followup)<br>`res.partner.type` (base)<br>`res.partner.user_ids` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<br>`res.partner.x_studio_vendor_group` (studio_usermodel_migration)<br>`view base.view_partner_tree` (base)</details> |  |
| res.partner.form.bugfix_sales | `view_partner_form_bugfix_sales` | form | remove `//group[@name='misc']/field[@name='ref']`; before `//div[hasclass('oe_title')]//h1`: add h1 | Contact form: moves the Reference field out of the Sales & Purchase Misc group and shows it in large heading style above the contact/company name. | `res.partner.ref` (base)<br>`view base.view_partner_form` (base) |  |

**Record rules (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jin - Sales - Add/Edit/Del Ca Customers | `rule_498_jin_sales_add_edit_del_ca_customers` | For Sales / Jin - Sales - POS Users: read on Contact only where `[("x_studio_customer_group", "=", "Cash")]`. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration) |  |
| Jin - Sales - Add/Edit/Del Non Ca Customers | `rule_499_jin_sales_add_edit_del_non_ca_customers` | For Sales / Jin - Sales - POS Users: read on Contact only where `[("x_studio_customer_group", "!=", "Cash")]`. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model res.partner` (base)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration) |  |
| res.partner company | `rule_2_res_partner_company` | For everyone (global rule): read/write/create/delete on Contact only where `['|', '|', ('partner_share', '=', False), ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]`. | `model res.partner` (base)<br>`res.partner.company_id` (base)<br>`res.partner.partner_share` (base) |  |
| res_partner: portal/public: read access on my commercial partner | `rule_3_res_partner_portal_public_read_access_on_my_commercial_partn` | For User types / Portal, User types / Public: read on Contact only where `[('id', 'child_of', user.commercial_partner_id.id)]`. | `group base.group_portal` (base)<br>`group base.group_public` (base)<br>`model res.partner` (base) |  |
