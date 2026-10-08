# BugFix-Sales — `sale.order`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `sale.order` — Sales Order

*Extends a model created by `sale`.* Python: `models/sale_order.py`.

Other repos that use this model: `account.bank.statement.line.x_studio_many2one_field_re1H2` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_sale_id` (BugFix-Accounting)<br>`account.move._compute_is_rug_invoice()` (Fix-repair)<br>`account.move._compute_x_studio_rug_confirmed()` (Fix-repair)<br>`account.move.line._delegate_studio_computes_to_native()` (Fix-repair)<br>`account.move.write()` (Fix-repair)<br>`account.move.x_studio_sale_id` (BugFix-Accounting)<br>`account.payment.x_studio_many2one_field_re1H2` (BugFix-Accounting)<details><summary>+60 more</summary>`account.payment.x_studio_sale_id` (BugFix-Accounting)<br>`approval rule BugFix-Approvals.rule_21_sales_order_action_quotation_send_technical_a_warning_can_be` (BugFix-Approvals)<br>`approval rule BugFix-Approvals.rule_33_sales_order_action_cancel_user_types_internal_user_33` (BugFix-Approvals)<br>`approval rule BugFix-Approvals.rule_47_sales_order_action_unlock_sale_repair_sales_unlock_47` (BugFix-Approvals)<br>`approval rule BugFix-Approvals.rule_50_sales_order_action_unlock_user_types_internal_user_50` (BugFix-Approvals)<br>`approval rule BugFix-Approvals.rule_51_sales_order_action_unlock_inventory_administrator_51` (BugFix-Approvals)<br>`approval rule BugFix-Approvals.rule_60_sales_order_action_draft_user_types_internal_user_60` (BugFix-Approvals)<br>`approval rule BugFix-Approvals.rule_61_sales_order_action_quotation_send_user_types_internal_user_6` (BugFix-Approvals)<br>`crossovered.budget.x_studio_created_from_sales_order_1` (BugFix-Accounting)<br>`helpdesk.ticket._delegate_studio_server_actions_to_native()` (Fix-repair)<br>`helpdesk.ticket._get_so_from_serial()` (Fix-repair)<br>`helpdesk.ticket._repair_auto_select_product_for_rug()` (Fix-repair)<br>`helpdesk.ticket._repair_auto_select_product_for_rug_no_company()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_change_repair_type_to_rug()` (Fix-repair)<br>`helpdesk.ticket.x_studio_sale_order` (Fix-repair)<br>`purchase.order.x_studio_subcontracting_so` (BugFix-Purchase)<br>`report BugFix-Studio-Misc.action_report_1440_test_report_kapila` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3445_jinasena_quotation_1` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3446_sales_order_report` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3449_jinasena_quotation` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3450_jinasena_sales_order` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3476_c06_1_sales_invoice_non_vat_product_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3477_template_c06_2_sales_invoice_non_vat_spares_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3478_template_c06_3_sales_invoice_vat_product_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3479_template_c06_4_sales_invoice_vat_spares_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3480_template_c06_5_sales_invoice_svat_product_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3481_template_c06_6_sales_invoice_svat_spares_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3482_c05_proforma_invoice` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3483_c04_sales_order_delivery_order_packing_slip` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3484_c03_customer_payment_receipt` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3485_c02_sales_order_confirmation` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3486_c01_sales_quotation` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3562_c06_2_sales_invoice_non_vat_spares_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3563_c06_3_sales_invoice_vat_product_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3564_c06_4_sales_invoice_vat_spares_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3565_c06_5_sales_invoice_svat_product_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3566_c06_6_sales_invoice_svat_spares_sale` (BugFix-Studio-Misc)<br>`report BugFix-Studio-Misc.action_report_3567_template_c06_1_sales_invoice_non_vat_product_sale` (BugFix-Studio-Misc)<br>`server action BugFix-Accounting.sa_f5_account_move_rr_validate_rug_in_customer_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_account_move_sls_validate_payment_in_customer_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_project_gross_margin` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1519_sls_payment_reconciliation_automate` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1733_srm_update_sales_order_customer_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1751_sls_validate_payment_in_customer_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2102_srm_rpt_project_gross_margin` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2331_rr_validate_rug_in_customer_invoice` (BugFix-Accounting)<br>`server action BugFix-Stock.sa_f5_stock_picking_sls_validate_payment_in_shipment` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1438_sls_validate_payment_in_shipment` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1774_sls_validate_payment_in_xxx` (BugFix-Stock)<br>`server action BugFix-Studio-Misc.server_action_1743_sample_server_action` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2268_sample_server_action_2` (BugFix-Studio-Misc)<br>`stock.picking._action_done()` (Fix-repair)<br>`stock.picking._delegate_studio_computes_to_native()` (Fix-repair)<br>`stock.picking.x_studio_sales_order` (BugFix-Stock)<br>`stock.picking.x_studio_ticket_sales_order` (BugFix-Stock)<br>`x_purchase.request.line.make.purchase.order.x_subcontracting_so` (BugFix-Purchase)<br>`x_purchase_request.x_studio_created_from_so` (BugFix-Purchase)<br>`x_rm_gross_margin_comp.x_studio_sales_order` (BugFix-Accounting)<br>`x_rm_sales_order_line.x_studio_sales_order` (BugFix-Accounting)<br>`x_temp_estimated.x_studio_sales_order` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:sale.order -->
This repo adds over 100 fields to sales orders, centred on Quotation Type (Sales, Project or Repair), which drives most of the logic. The order form gets request and approve buttons for credit limit, temporary credit, overdue, bank guarantee, margin and over-commission, backed by seven approval rules for the matching approver groups, plus checks such as credit limit and bank guarantee validation, over-margin details and a Create Customer Payment button. Automations set the quotation type from the linked task or project, apply the customer's or the project price list, add a _PRJ suffix to project order numbers, validate payment type and project dates, track repair lock and re-estimate status and support Repair-Under-Guarantee (RUG) approval and rejection. Project quotations also get buttons to create budget entries, create purchase requests and update RFQ costs, and every order can carry a chosen document introduction and conclusion text.
<!-- /SUMMARY -->

**Fields (107):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `bugfix_sales_conclusion_id` | Document Conclusion | many2one → `bugfix_sales.doc_conclusion` | Conclusion template chosen on the quotation; when selected an onchange copies its text into the Conclusion field. | stored | `model bugfix_sales.doc_conclusion` | `sale.order._onchange_bugfix_sales_conclusion_id()`<br>`view BugFix-Sales.view_order_form_bugfix_sales` |
| `bugfix_sales_conclusion_text` | Conclusion | text | Editable conclusion text for this quotation, prefilled from the selected conclusion template. | stored |  | `view BugFix-Sales.view_order_form_bugfix_sales` |
| `bugfix_sales_intro_id` | Document Introduction | many2one → `bugfix_sales.doc_intro` | Introduction template chosen on the quotation; when selected an onchange copies its text into the Introduction field. | stored | `model bugfix_sales.doc_intro` | `sale.order._onchange_bugfix_sales_intro_id()`<br>`view BugFix-Sales.view_order_form_bugfix_sales` |
| `bugfix_sales_intro_text` | Introduction | text | Editable introduction text for this quotation, prefilled from the selected introduction template. | stored |  | `view BugFix-Sales.view_order_form_bugfix_sales` |
| `x_studio_` | Test Field | boolean | Studio test checkbox on the sales order ('Test Field'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_account_mandatory` | Account Mandatory | boolean | Flags that analytic account is mandatory on the order; set by the update-analytic-tag-parameters server actions (customer/user). | stored |  | `server action BugFix-Sales.server_action_2414_update_analytic_tag_parameters_sales_order_customer`<br>`server action BugFix-Sales.server_action_2415_update_analytic_tag_parameters_sales_order_user`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_approval_request_sent` | Approval Request Sent | boolean | Marks that a sales approval request was sent; set and validated by the 'SLS Request Approval Sent' actions. | stored |  | `server action BugFix-Sales.server_action_1460_sls_request_approval_sent`<br>`server action BugFix-Sales.server_action_1843_sls_request_approval_sent_validate`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_authorized_repair_user` | Authorized Repair User | boolean | Flags an authorized repair user on the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_bank_guarantee_approved` | Bank Guarantee Approved | boolean | Marks the bank-guarantee exception as approved; set by the 'SLS Bank Guarantee Approval' action and used in order views and invoices. | stored |  | `account.move.x_studio_bank_guarantee_approved` (BugFix-Accounting)<br>`server action BugFix-Sales.server_action_2507_sls_bank_guarantee_approval`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_bank_guarantee_notification` | BG Notification | boolean | Bank guarantee notification flag; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_bank_guarantee_request_sent` | BG Request Sent | boolean | Marks that a bank guarantee approval request was sent; set and validated by the 'SLS Request Bank Guarantee Approval Sent' actions. | stored |  | `server action BugFix-Sales.server_action_1481_sls_request_bank_guarantee_approval_sent`<br>`server action BugFix-Sales.server_action_1845_sls_request_bank_guarantee_approval_sent_validate`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_bank_guarantee_validation` | BG Validation | boolean | Bank guarantee validation flag; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_bg_sent` | BG Sent | boolean | Marks that the bank guarantee notification was sent; set by the 'SLS Send Bank Guarantee Notification' action. | stored |  | `server action BugFix-Sales.server_action_2515_sls_send_bank_guarantee_notification`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_budget_created` | Budget Created | boolean | Marks that project budget entries were created; set by 'PROJ Create Budget Entries' and controls budget buttons. | stored |  | `server action BugFix-Sales.server_action_2178_proj_create_budget_entries`<br>`view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` (BugFix-Accounting)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_cancelled` | Cancelled | boolean | Cancelled flag on the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_clear_free_items` | Clear Free Items | boolean | Flags that free items should be cleared; used by the 'SLS Validate Sales' action and order form buttons. | stored |  | `server action BugFix-Sales.server_action_2337_sls_validate_sales`<br>`view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` (BugFix-Accounting)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_confirm_validation` | Confirm Validation | text | Text holding confirm-time validation messages (default via a default record); shown on the Sales Order form (Studio customization). | stored |  | `default BugFix-Sales.default_415_sale_order_x_studio_confirm_validation`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_confirm_validation_1` | Confirm Validation (v2) | text | Second version of the confirm-validation text (default via a default record); shown on the Sales Order form (Studio customization). | stored |  | `default BugFix-Sales.default_417_sale_order_x_studio_confirm_validation_1`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_credit_limit_approved` | Credit Limit Approved | boolean | Marks the credit-limit exception as approved; set by the 'SLS Credit Limit Approval' action and used in order views and on invoices. | stored |  | `account.move.x_studio_credit_limit_approved` (BugFix-Accounting)<br>`server action BugFix-Sales.server_action_2503_sls_credit_limit_approval`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_credit_limit_validation` | Credit Limit Validation | boolean | Credit limit validation flag; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_current_tot_amount` | Current Total Amount | float | Stored 'current total amount' of the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_current_tot_amount_1` | Current Total Amount (v2) | float | Second version of the stored current total amount; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_cust_total_receivable` | Customer Total Receivable | monetary | Total amount the customer owes, read live from the customer (related to partner credit); shown on the Sales Order form (Studio customization). | related `partner_id.credit`; not stored | `res.partner.credit` (account)<br>`sale.order.partner_id` (sale) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_cust_total_receivable_1` | Customer Total Receivable (v2) | monetary | Duplicate of the customer's total receivable (related to partner credit); shown on the Sales Order form (Studio customization). | related `partner_id.credit`; not stored | `res.partner.credit` (account)<br>`sale.order.partner_id` (sale) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_customer_bank_guarantee` | Customer BG Amount | float | Customer's bank guarantee amount stored on the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_customer_credit_limit` | Customer Credit Limit | float | Customer's credit limit stored on the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_customer_payment_method` | Customer Payment Method | selection | Customer's payment type (Cash/Credit), related from the customer; used to validate the order payment type and when creating the customer payment. | related `partner_id.x_studio_payment_method`; stored | `res.partner.x_studio_payment_method`<br>`sale.order.partner_id` (sale) | `server action BugFix-Sales.server_action_1434_sls_validate_order_payment_type_in_so`<br>`server action BugFix-Sales.server_action_2341_sls_create_customer_payment`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_document_1` | Document 1 | binary | Uploaded supporting document 1 on the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_document_2` | Document 2 | binary | Uploaded supporting document 2 on the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_document_3` | Document 3 | binary | Uploaded supporting document 3 on the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_expired` | Expired | boolean | Flags the quotation as expired; plain checkbox shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_expiry_date` | Bank Guarantee Expiration Date | date | Customer's bank guarantee expiry date, copied (stored related) from the customer; shown on the Sales Order form (Studio customization). | related `partner_id.x_studio_expiry_date`; stored | `res.partner.x_studio_expiry_date`<br>`sale.order.partner_id` (sale) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_fsm_done` | FSM Done | boolean | Marks field service work as done for the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_fully_paid` | Fully Paid | boolean | Marks the order as fully paid; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_grant_temporary_credit` | Grant Temporary Credit | boolean | Requests/grants a temporary credit for the customer; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_guarantee_status` | Guarantee Status | char | Text status of the customer's bank guarantee, set by `_fix_repair_compute_guarantee_status`; shown on the Sales Order form (Studio customization). | stored | `sale.order._jin_compute_guarantee_status()` (Fix-repair) | `sale.order._fix_repair_compute_guarantee_status()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_image_1` | Image 1 | binary | Uploaded image 1 on the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_image_2` | Image 2 | binary | Uploaded image 2 on the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_image_3` | Image 3 | binary | Uploaded image 3 on the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_inventory_short` | Inventory Short | boolean | Flags that the project order has inventory shortage; controls the Create PR and Update RFQ Cost buttons and the budget confirm status. | stored |  | `crossovered.budget._compute_x_studio_confirm_status()` (BugFix-Accounting)<br>`view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_locked` | Locked | boolean | Lock flag of the order maintained by the RR track-lock-status automation and server actions; shown on the order form. | stored |  | `automation BugFix-Sales.base_automation_205_rr_track_lock_status_4`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_track_lock_status_2`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_track_lock_status`<br>`server action BugFix-Sales.server_action_2250_rr_track_lock_status`<br>`server action BugFix-Sales.server_action_2251_rr_track_lock_status_2`<details><summary>+2 more</summary>`server action BugFix-Sales.server_action_2253_rr_track_lock_status_4`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`</details> |
| `x_studio_main_project_2` | Main Project 2 | many2one → `project.project` | Second 'main project' link on the order; shown on the Sales Order form (Studio customization). | stored | `model project.project` (project) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_main_project_no` | Main Project No | many2one → `project.project` | Main project the order belongs to, entered by the user; used by the 'PROJ Create Budget Entries' action. | stored | `model project.project` (project) | `server action BugFix-Sales.server_action_2178_proj_create_budget_entries`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_many2one_field_KjdJ3` | Budgetary Position | many2one → `account.budget.post` | Budgetary position linked to the sales order, shown on the Sales Order form (Studio customization). | stored | `model account.budget.post` (account_budget) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_margin_approval_request_sent` | Margin Approval Request Sent | boolean | Marks that a margin approval request was sent; set by the 'SLS Margin Approval Request Sent' action. | stored |  | `server action BugFix-Sales.server_action_1509_sls_margin_approval_request_sent`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_margin_approved` | Margin Approved | boolean | Marks a below-minimum margin as approved; set by the 'SLS Margin Approval' action and used in order views. | stored |  | `server action BugFix-Sales.server_action_2495_sls_margin_approval`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_margin_exceed` | Margin Exceed | boolean | True when order lines breach the margin rule; set by the 'SLS Item Over Margin Details' action and drives margin approval buttons. | stored |  | `server action BugFix-Sales.server_action_1517_sls_item_over_margin_details`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_new_item_from_project` | New Item from Project | boolean | Flags a project order containing new items; hides the Create PR / Update RFQ Cost buttons and is used on the order form. | stored |  | `view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_one2many_field_ERCBB` | New One2many | one2many → `sale.order.line` | Extra Studio one2many of sales order lines on the order, shown on the Sales Order form (Studio customization). | stored | `model sale.order.line` (sale) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_order_payment_method` | Order Payment Type | selection: Cash=Cash; Credit=Credit | Payment type of this order (Cash or Credit), validated by an automation; drives credit, overdue and bank-guarantee computes and is copied to invoices. | stored |  | `account.move.x_studio_order_payment_method` (BugFix-Accounting)<br>`automation BugFix-Sales.base_automation_80_sls_validate_order_payment_type_in_so`<br>`project.task._compute_x_studio_valid_invoiced_so()` (Fix-repair)<br>`sale.order._fix_repair_compute_guarantee_status()` (Fix-repair)<br>`sale.order._fix_repair_compute_over_bank_guarantee()` (Fix-repair)<details><summary>+17 more</summary>`sale.order._fix_repair_compute_over_bank_guarantee_amount()` (Fix-repair)<br>`sale.order._fix_repair_compute_over_credit()` (Fix-repair)<br>`sale.order._fix_repair_compute_over_credit_amount()` (Fix-repair)<br>`sale.order._fix_repair_compute_overdue()` (Fix-repair)<br>`sale.order._jin_compute_guarantee_status()` (Fix-repair)<br>`sale.order._jin_compute_over_bank_guarantee()` (Fix-repair)<br>`sale.order._jin_compute_over_bank_guarantee_amount()` (Fix-repair)<br>`sale.order._jin_compute_over_credit()` (Fix-repair)<br>`sale.order._jin_compute_over_credit_amount()` (Fix-repair)<br>`sale.order._jin_compute_overdue()` (Fix-repair)<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_repair_sos`<br>`server action BugFix-Sales.server_action_1430_sls_pass_customer_pm_to_so`<br>`server action BugFix-Sales.server_action_1434_sls_validate_order_payment_type_in_so`<br>`server action BugFix-Sales.server_action_1853_sls_view_credit_limit_validation`<br>`server action BugFix-Sales.server_action_1995_rr_auto_generate_quotation_type_for_repair_sos`<br>`server action BugFix-Sales.server_action_2341_sls_create_customer_payment`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`</details> |
| `x_studio_over_bank_guarantee` | Over Bank Guarantee | boolean | True when the order exceeds the customer's bank guarantee; set by the `_fix_repair_compute_over_bank_guarantee` compute and used for approval buttons and on invoices. | stored | `sale.order._jin_compute_over_bank_guarantee()` (Fix-repair) | `account.move.x_studio_over_bank_guarantee` (BugFix-Accounting)<br>`sale.order._fix_repair_compute_over_bank_guarantee()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_over_bank_guarantee_amount` | Over Bank Guarantee Amount | float | Amount by which the order exceeds the customer's bank guarantee; set by `_fix_repair_compute_over_bank_guarantee_amount` and shown on the Sales Order form (Studio customization). | stored | `sale.order._jin_compute_over_bank_guarantee_amount()` (Fix-repair) | `sale.order._fix_repair_compute_over_bank_guarantee_amount()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_over_comm_approval_request_sent` | Over Commission Approval Request Sent | boolean | Marks that an over-commission approval request was sent; set by the 'SLS Over Commission Approval Request Sent' action. | stored |  | `server action BugFix-Sales.server_action_1499_sls_over_commission_approval_request_sent`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_over_commission` | Over Commission | boolean | True when a line's commission exceeds the allowed level; set by `_fix_repair_compute_over_commission` and drives the over-commission approval buttons. | stored | `sale.order._jin_compute_over_commission()` (Fix-repair) | `sale.order._fix_repair_compute_over_commission()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_over_commission_approved` | Over Commission Approved | boolean | Marks over-commission as approved; set by the 'SLS Over Commission Approval' action and used in order views. | stored |  | `server action BugFix-Sales.server_action_2499_sls_over_commission_approval`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_over_credit` | Over Credit | boolean | True when the order exceeds the customer's credit limit; set by the `_fix_repair_compute_over_credit` compute (has a default record) and drives credit approval buttons. | stored | `sale.order._jin_compute_over_credit()` (Fix-repair) | `default BugFix-Sales.default_212_sale_order_x_studio_over_credit`<br>`sale.order._fix_repair_compute_over_credit()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_over_credit_amount` | Over Credit Amount | float | Amount by which the order exceeds the customer's credit limit; set by `_fix_repair_compute_over_credit_amount` and shown on the Sales Order form (Studio customization). | stored | `sale.order._jin_compute_over_credit_amount()` (Fix-repair) | `sale.order._fix_repair_compute_over_credit_amount()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_overdue` | Overdue | boolean | True when the customer has overdue balances; set by `_fix_repair_compute_overdue` and drives the overdue approval buttons. | stored | `sale.order._jin_compute_overdue()` (Fix-repair) | `sale.order._fix_repair_compute_overdue()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_overdue_approved` | Overdue Approved | boolean | Marks the overdue exception as approved; set by the 'SLS Request Overdue Approval' action and used in order views. | stored |  | `server action BugFix-Sales.server_action_2458_sls_request_overdue_approval_final01`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_overdue_request_sent` | Overdue Request Sent | boolean | Marks that an overdue approval request was sent; set and validated by the 'SLS Overdue Approval Request Sent' actions. | stored |  | `server action BugFix-Sales.server_action_1472_sls_overdue_approval_request_sent`<br>`server action BugFix-Sales.server_action_1841_sls_overdue_approval_request_sent_validate`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_petty_cash_reimbursement` | Petty Cash Reimbursement | boolean | Flags the order as a petty cash reimbursement; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_pr_cost_updated` | PR Cost Updated | boolean | Marks that RFQ costs were pulled back into the project quotation; set by 'PROJ Update RFQ Cost to Sales Quotation' and hides the Update RFQ Cost button. | stored |  | `server action BugFix-Sales.server_action_2192_proj_update_rfq_cost_to_sales_quotation`<br>`view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_pr_created` | PR Created | boolean | Marks that a purchase request was created from the project quotation; set by 'PROJ Create PR from Sales Quotation' and controls Create PR / Update RFQ Cost buttons. | stored |  | `server action BugFix-Sales.server_action_2188_proj_create_pr_from_sales_quotation`<br>`server action BugFix-Sales.server_action_2192_proj_update_rfq_cost_to_sales_quotation`<br>`view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_price_not_confirmed` | Price Not Confirmed | boolean | Flags that some prices on the order are not yet confirmed; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_proj_budget_status` | Project Budget Status | selection: draft=Draft; cancel=Cancelled; confirm=Confirmed; validate=Validated; done=Done | Status of the order's project budget (Draft, Cancelled, Confirmed, Validated, Done); shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_project_budget` | Project Budget | many2one → `crossovered.budget` | Project budget created for the sales order; filled by the 'PROJ Create Budget Entries' server action and shown on the Sales Order form (Studio customization). | stored | `model crossovered.budget` (account_budget) | `server action BugFix-Sales.server_action_2178_proj_create_budget_entries`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_project_end_date` | Project End Date | date | End date of the project order; validated against the start date by an automation and used when generating the quotation type, creating budgets and syncing with the main SO. | stored |  | `automation BugFix-Sales.base_automation_260_proj_validate_start_date_and_end_date_for_project_sos`<br>`server action BugFix-Sales.sa_f5_sale_order_proj_validate_start_date_and_end_date_for_project_sos`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos`<br>`server action BugFix-Sales.server_action_2114_rr_auto_generate_quotation_type_for_project_sos`<details><summary>+5 more</summary>`server action BugFix-Sales.server_action_2117_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.server_action_2178_proj_create_budget_entries`<br>`server action BugFix-Sales.server_action_2572_proj_update_with_main_so`<br>`server action BugFix-Sales.server_action_2576_proj_validate_start_date_and_end_date_for_project_sos`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`</details> |
| `x_studio_project_group` | Project Group | many2one → `x_project_groups` | Project group of the sales order; used by the RR auto-generate quotation type server actions for project orders. | stored | `model x_project_groups` (BugFix-Project) | `server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos`<br>`server action BugFix-Sales.server_action_2114_rr_auto_generate_quotation_type_for_project_sos`<br>`server action BugFix-Sales.server_action_2117_rr_auto_generate_quotation_type_for_project_sos_2`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_project_item_approved` | Project Item Approved | boolean | Marks project items as approved; set by the 'PROJ Project Item Approval' action. | stored |  | `server action BugFix-Sales.server_action_2142_proj_project_item_approval`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_project_item_request_sent` | Project Item Request Sent | boolean | Marks that a project item approval request was sent; set by the 'PROJ Project Item Request Sent' action. | stored |  | `server action BugFix-Sales.server_action_2134_proj_project_item_request_sent`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_project_no` | Project No | many2one → `project.project` | Project of the order, copied (stored related) from the linked task's project; used by quotation-type, budget and customer payment server actions. | related `task_id.project_id`; stored | `model project.project` (project)<br>`project.task.project_id` (project)<br>`sale.order.task_id` (industry_fsm_sale) | `server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_repair_sos`<br>`server action BugFix-Sales.server_action_1995_rr_auto_generate_quotation_type_for_repair_sos`<br>`server action BugFix-Sales.server_action_2114_rr_auto_generate_quotation_type_for_project_sos`<details><summary>+4 more</summary>`server action BugFix-Sales.server_action_2117_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.server_action_2178_proj_create_budget_entries`<br>`server action BugFix-Sales.server_action_2341_sls_create_customer_payment`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`</details> |
| `x_studio_project_start_date` | Project Start Date | date | Start date of the project order; validated against the end date by an automation and used when generating the quotation type and creating budgets. | stored |  | `automation BugFix-Sales.base_automation_260_proj_validate_start_date_and_end_date_for_project_sos`<br>`server action BugFix-Sales.sa_f5_sale_order_proj_validate_start_date_and_end_date_for_project_sos`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos`<br>`server action BugFix-Sales.server_action_2114_rr_auto_generate_quotation_type_for_project_sos`<details><summary>+5 more</summary>`server action BugFix-Sales.server_action_2117_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.server_action_2178_proj_create_budget_entries`<br>`server action BugFix-Sales.server_action_2572_proj_update_with_main_so`<br>`server action BugFix-Sales.server_action_2576_proj_validate_start_date_and_end_date_for_project_sos`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`</details> |
| `x_studio_quotation_type` | Quotation Type | selection: Sales=Sales; Project=Project; Repair=Repair | Kind of quotation: Sales, Project or Repair. Central switch for many automations (lock tracking, project numbering, project price list, budgets, credit checks) and button visibility. | stored |  | `automation BugFix-Sales.base_automation_205_rr_track_lock_status_4`<br>`automation BugFix-Sales.base_automation_258_jin_project_sales_order_seq_no_maintain_separate_nos_for_pro`<br>`automation BugFix-Sales.base_automation_341_proj_apply_project_price_list`<br>`automation BugFix-Stock.base_automation_199_proj_notify_transfer_completion` (BugFix-Stock)<br>`crossovered.budget._compute_x_studio_confirm_status()` (BugFix-Accounting)<details><summary>+31 more</summary>`project.task.x_studio_quotation_type` (BugFix-Project)<br>`sale.order._fix_repair_compute_over_credit()` (Fix-repair)<br>`server action BugFix-Sales.sa_f5_sale_order_proj_apply_project_price_list`<br>`server action BugFix-Sales.sa_f5_sale_order_proj_validate_start_date_and_end_date_for_project_sos`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_repair_sos`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_track_lock_status_2`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_track_lock_status`<br>`server action BugFix-Sales.server_action_1995_rr_auto_generate_quotation_type_for_repair_sos`<br>`server action BugFix-Sales.server_action_2113_rr_auto_generate_quotation_type_for_projct_sos`<br>`server action BugFix-Sales.server_action_2114_rr_auto_generate_quotation_type_for_project_sos`<br>`server action BugFix-Sales.server_action_2117_rr_auto_generate_quotation_type_for_project_sos_2`<br>`server action BugFix-Sales.server_action_2250_rr_track_lock_status`<br>`server action BugFix-Sales.server_action_2251_rr_track_lock_status_2`<br>`server action BugFix-Sales.server_action_2253_rr_track_lock_status_4`<br>`server action BugFix-Sales.server_action_2341_sls_create_customer_payment`<br>`server action BugFix-Sales.server_action_2573_project_sales_order_seq_no`<br>`server action BugFix-Sales.server_action_2574_project_sales_order_seq_no_2`<br>`server action BugFix-Sales.server_action_2575_project_sales_order_seq_no_3`<br>`server action BugFix-Sales.server_action_2576_proj_validate_start_date_and_end_date_for_project_sos`<br>`server action BugFix-Sales.server_action_2896_proj_apply_project_price_list`<br>`view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` (BugFix-Accounting)<br>`view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`<br>`view Fix-repair.view_sale_order_rug_direct_buttons` (Fix-repair)<br>`window action BugFix-Sales.act_window_2330_repair_sales_order_list`<br>`window action BugFix-Sales.act_window_2338_project_sales_orders`<br>`window action BugFix-Sales.aw_f4_sale_order_project_sales_orders`<br>`window action BugFix-Sales.aw_f4_sale_order_repair_sales_order_list`</details> |
| `x_studio_re_estimate_count` | Re-estimate Count | integer | Counter incremented each time the repair is re-estimated (default set by a default record); reset by `_re_estimate_reset` and used by the RR lock-status tracking actions. | stored |  | `default BugFix-Sales.default_363_sale_order_x_studio_re_estimate_count`<br>`sale.order._re_estimate_reset()` (Fix-repair)<br>`server action BugFix-Sales.sa_f5_sale_order_rr_track_lock_status`<br>`server action BugFix-Sales.server_action_2250_rr_track_lock_status`<br>`server action BugFix-Sales.server_action_2253_rr_track_lock_status_4`<details><summary>+1 more</summary>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`</details> |
| `x_studio_re_estimate_request_count` | Re-estimate Request Count (bool) | boolean | Boolean variant of the re-estimate request counter on the order. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_re_estimate_request_count_1` | Re-estimate Request Count | integer | Number of re-estimate requests on the order (default via a default record); checked by the 'RR Re-estimate Request Sent Validate' action. | stored |  | `default BugFix-Sales.default_364_sale_order_x_studio_re_estimate_request_count_1`<br>`server action BugFix-Sales.server_action_2246_rr_re_estimate_request_sent_validate`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_re_estimate_request_sent` | Re-estimate Request Sent | boolean | Marks that a re-estimate request was sent; set by the 'RR Re-estimate Request Sent' action and shown on the Sales Order form (Studio customization). | stored |  | `server action BugFix-Sales.server_action_2244_rr_re_estimate_request_sent`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_reject_reason` | Reject Reason | text | Reason entered when the order/approval is rejected; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_related_information` | Related Information | binary | Uploaded file with related information for the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_repair_image_01` | Repair Image 01 | binary | First repair photo uploaded on the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_repair_image_02` | Repair Image 02 | binary | Second repair photo uploaded on the order. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_repair_reason` | Repair Reason | char | Free-text reason for the repair; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_repair_validation` | Repair Validation | char | Text holding repair validation status/messages (default via a default record); shown on the Sales Order form (Studio customization). | stored |  | `default BugFix-Sales.default_374_sale_order_x_studio_repair_validation`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_rug_approved` | RUG Approved | boolean | Repair-Under-Guarantee approved on this order; set by the RR RUG Approval action, releases repair pickings and feeds the ticket's RUG approval status. | stored |  | `helpdesk.ticket._compute_x_studio_rug_approval_status()` (Fix-repair)<br>`project.task._compute_x_studio_valid_invoiced_so()` (Fix-repair)<br>`server action BugFix-Sales.server_action_1981_rr_rug_approval`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`<br>`view Fix-repair.view_sale_order_rug_direct_buttons` (Fix-repair) |
| `x_studio_rug_confirmed` | RUG Confirmed | boolean | Repair-Under-Guarantee confirmed by the operator, one step before final approval; used in button visibility to distinguish 'in review' from decided, and mirrored on invoices. | stored |  | `account.move.x_studio_rug_confirmed` (BugFix-Accounting)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_rug_rejected` | RUG Rejected | boolean | Repair-Under-Guarantee rejected, so the repair becomes customer-paid; set by RUG Rejection and checked by repair invoicing, quotation sending, picking validation blocks and the ticket's RUG status. | stored |  | `account.move.x_studio_rug_rejected` (BugFix-Accounting)<br>`helpdesk.ticket._compute_x_studio_rug_approval_status()` (Fix-repair)<br>`sale.order._create_repair_full_invoice()` (Fix-repair)<br>`sale.order.action_quotation_send()` (Fix-Repair-Wizard-Nav, Fix-repair)<br>`sale.order.action_repair_create_invoice()` (Fix-Repair-Wizard-Nav, Fix-repair)<details><summary>+4 more</summary>`server action BugFix-Sales.server_action_2004_rr_rug_rejection`<br>`stock.picking._compute_nuw_block_validate()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`<br>`view Fix-repair.view_sale_order_rug_direct_buttons` (Fix-repair)</details> |
| `x_studio_rug_request_sent` | RUG Request Sent | boolean | Marks that a Repair-Under-Guarantee approval request was sent; set by 'RR RUG Approval Request Sent' and used by the RUG buttons on the order. | stored |  | `server action BugFix-Sales.server_action_1983_rr_rug_approval_request_sent`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`<br>`view Fix-repair.view_sale_order_rug_direct_buttons` (Fix-repair) |
| `x_studio_sales_order_validity` | Sales Order Validity | integer | Quotation validity in days, computed (not stored) from the company's Sales Order Validity setting; shown on the Sales Order form (Studio customization). | computed by `_compute_x_studio_sales_order_validity`; not stored | `sale.order._compute_x_studio_sales_order_validity()` | `default BugFix-Sales.default_384_sale_order_x_studio_sales_order_validity`<br>`sale.order._compute_x_studio_sales_order_validity()`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_sell_and_win` | Sell and Win | boolean | 'Sell and Win' flag on the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_service_item_available` | Service Item Available | boolean | Computed: True when the order has a service line whose product creates a project only (service tracking 'project_only'); shown on the Sales Order form (Studio customization). | computed by `_compute_x_studio_service_item_available`; not stored | `sale.order._compute_x_studio_service_item_available()` | `sale.order._compute_x_studio_service_item_available()`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_sub_contract` | Sub Contract | boolean | Flags the order as sub-contract; read by 'PROJ Create PR from Sales Quotation'. | stored |  | `server action BugFix-Sales.server_action_2188_proj_create_pr_from_sales_quotation`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_tem_credit_approval_request_sent` | Temporary Credit Approval Request Sent | boolean | Marks that a temporary credit approval request was sent; set by the 'SLS Temporary Credit Approval Sent' action. | stored |  | `server action BugFix-Sales.server_action_1464_sls_temporary_credit_approval_sent`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_temporary_credit_approved` | Temporary Credit Approved | boolean | Marks temporary credit as approved; set by the 'SLS Temporary Credit Approval' action and used in order views. | stored |  | `server action BugFix-Sales.server_action_2511_sls_temporary_credit_approval`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_total` | Total | char | Free-text 'Total' field on the order. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_total_overdue` | Total Overdue | monetary | Customer's total overdue amount, related from the customer; shown on the Sales Order form (Studio customization). | related `partner_id.total_overdue`; not stored | `res.partner.total_overdue` (account_followup)<br>`sale.order.partner_id` (sale) | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_transfer_inventory_ok` | Transfer Inventory OK | boolean | Flags that inventory transfer is OK for the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_unlocked` | Unlocked | boolean | Unlock flag of the order maintained by the RR track-lock-status automation and server actions; shown on the order form. | stored |  | `automation BugFix-Sales.base_automation_205_rr_track_lock_status_4`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_track_lock_status_2`<br>`server action BugFix-Sales.sa_f5_sale_order_rr_track_lock_status`<br>`server action BugFix-Sales.server_action_2250_rr_track_lock_status`<br>`server action BugFix-Sales.server_action_2251_rr_track_lock_status_2`<details><summary>+2 more</summary>`server action BugFix-Sales.server_action_2253_rr_track_lock_status_4`<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`</details> |
| `x_studio_valid_bank_guarantee` | Valid Bank Guarantee | boolean | Copied (stored related) from the customer's Valid Bank Guarantee flag; used by the guarantee status and over-bank-guarantee computes. | related `partner_id.x_studio_valid_bank_guarantee`; stored | `res.partner.x_studio_valid_bank_guarantee`<br>`sale.order.partner_id` (sale) | `sale.order._fix_repair_compute_guarantee_status()` (Fix-repair)<br>`sale.order._fix_repair_compute_over_bank_guarantee()` (Fix-repair)<br>`sale.order._fix_repair_compute_over_bank_guarantee_amount()` (Fix-repair)<br>`sale.order._jin_compute_guarantee_status()` (Fix-repair)<br>`sale.order._jin_compute_over_bank_guarantee()` (Fix-repair)<details><summary>+2 more</summary>`sale.order._jin_compute_over_bank_guarantee_amount()` (Fix-repair)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`</details> |
| `x_studio_valid_order_lines` | Valid Order Lines | boolean | Computed and stored: True when the order has at least one product line with quantity and unit price above zero; used to gate the Confirm button. | computed by `_compute_x_studio_valid_order_lines`; stored | `sale.order._compute_x_studio_valid_order_lines()` | `view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` (BugFix-Accounting)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_valid_order_lines_for_projects` | Valid Order Lines for Projects | boolean | Computed: True when the order has any lines; used to show the Create PR / Update RFQ Cost buttons on project quotations. | computed by `_compute_x_studio_valid_order_lines_for_projects`; not stored | `sale.order._compute_x_studio_valid_order_lines_for_projects()` | `sale.order._compute_x_studio_valid_order_lines_for_projects()`<br>`view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_valid_order_lines_for_update_rfq_cost` | Valid Order Lines for Update RFQ Cost | boolean | Computed: True when real order lines include a positive quantity and none has zero quantity; gates the Update RFQ Cost button. | computed by `_compute_x_studio_valid_order_lines_for_update_rfq_cost`; not stored | `sale.order._compute_x_studio_valid_order_lines_for_update_rfq_cost()` | `sale.order._compute_x_studio_valid_order_lines_for_update_rfq_cost()`<br>`view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)<br>`view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_valid_transfer` | Valid Transfer | boolean | Valid transfer flag on the order; shown on the Sales Order form (Studio customization). | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_studio_warranty_card` | Warranty Card | binary | Uploaded warranty card for the repaired item. | stored |  | `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` |
| `x_x_studio_created_from_sales_order_1_crossovered_budget_count` | Project Budget | integer | Number of budgets created from this sales order, shown on the Project Budget smart button. | not stored |  | `view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` (BugFix-Accounting) |
| `x_x_studio_created_from_so_x_purchase_request_count` | Created From SO count | integer | Number of purchase requests created from this sales order, shown on the Requisitions smart button. | not stored |  | `view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase) |
| `x_x_studio_sales_order_account_payment_count` | Sales Order count | integer | Number of payments linked to this sales order, shown on a smart button. | not stored |  | `view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` (BugFix-Accounting) |
| `x_x_studio_subcontracting_so_purchase_order_count` | Subcontracting SO count | integer | Number of subcontracting purchase orders linked to this sales order, shown on a smart button. | not stored |  | `view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase) |

**Python methods (8):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_x_studio_valid_order_lines` | Compute of Valid Order Lines: True when the order has at least one product line (not section/note) with quantity > 0 and unit price > 0. Gates the Confirm button in the Repair flow. | api.depends('order_line', 'order_line.product_uom_qty', 'order_line.price_unit',… |  | `sale.order.line.display_type` (sale)<br>`sale.order.line.price_unit` (sale)<br>`sale.order.line.product_uom_qty` (sale)<br>`sale.order.order_line` (sale) | `sale.order.x_studio_valid_order_lines` | `models/sale_order.py:196` |
| `_compute_x_studio_sales_order_validity` | Compute of Sales Order Validity on the order: copies the validity days configured on the order's company (0 if none). | api.depends('company_id') |  | `res.company.x_studio_sales_order_validity`<br>`sale.order.company_id` (sale)<br>`sale.order.x_studio_sales_order_validity` | `sale.order.x_studio_sales_order_validity` | `models/sale_order.py:222` |
| `_compute_x_studio_service_item_available` | Compute of Service Item Available: True when any order line is a service product whose service tracking is 'project_only' (creates a project). | api.depends('order_line.product_id.service_tracking', 'order_line.product_type') |  | `product.product.service_tracking` (sale_project)<br>`sale.order.line.product_id` (sale)<br>`sale.order.line.product_type` (sale)<br>`sale.order.order_line` (sale)<br>`sale.order.x_studio_service_item_available` | `sale.order.x_studio_service_item_available` | `models/sale_order.py:312` |
| `_compute_x_studio_valid_order_lines_for_projects` | Compute of Valid Order Lines for Projects: True whenever the order has any order line at all. | api.depends('order_line') |  | `sale.order.order_line` (sale)<br>`sale.order.x_studio_valid_order_lines_for_projects` | `sale.order.x_studio_valid_order_lines_for_projects` | `models/sale_order.py:392` |
| `_compute_x_studio_valid_order_lines_for_update_rfq_cost` | Compute of Valid Order Lines for Update RFQ Cost: True when the order's product lines include at least one with quantity > 0 and none with quantity 0. | api.depends('order_line.product_uom_qty', 'order_line.display_type') |  | `sale.order.line.display_type` (sale)<br>`sale.order.line.product_uom_qty` (sale)<br>`sale.order.order_line` (sale)<br>`sale.order.x_studio_valid_order_lines_for_update_rfq_cost` | `sale.order.x_studio_valid_order_lines_for_update_rfq_cost` | `models/sale_order.py:397` |
| `_onchange_bugfix_sales_intro_id` | Onchange: when a Document Introduction template is chosen on the order, copies its description into the editable introduction text. | api.onchange('bugfix_sales_intro_id') |  | `sale.order.bugfix_sales_intro_id` |  | `models/sale_order.py:492` |
| `_onchange_bugfix_sales_conclusion_id` | Onchange: when a Document Conclusion template is chosen on the order, copies its description into the editable conclusion text. | api.onchange('bugfix_sales_conclusion_id') |  | `sale.order.bugfix_sales_conclusion_id` |  | `models/sale_order.py:498` |
| `_get_view` | Override of form-view loading that hides a configured list of header fields (and their labels) when quotation type is empty or 'Sales', merging with any existing invisible conditions such as the Repair rule. | api.model | yes |  |  | `models/sale_order.py:504` |

**Server actions (95):**

- **Execute Code** (`server_action_1995_rr_auto_generate_quotation_type_for_repair_sos`, type `code`)
  - Function: Run by its automation: sets quotation type to 'Repair' and copies the customer's payment method when the order is linked to a task in a repair project (or its project is a repair project).
  - Depends on: `model project.task` (project), `model sale.order` (sale), `sale.order.partner_id` (sale), `sale.order.x_studio_order_payment_method`, `sale.order.x_studio_project_no`<details><summary>+1 more</summary>`sale.order.x_studio_quotation_type`</details>
  - Used by: `automation BugFix-Sales.base_automation_176_rr_auto_generate_quotation_type_for_repair_sos`
  <details><summary>code (13 lines)</summary>

```python

if record.id:
    # x_studio_project_no is never set by FSM - use task link instead
    task = env['project.task'].search([
        ('sale_order_id', '=', record.id),
        ('project_id.x_studio_repair_project', '=', True)
    ], limit=1)
    if task:
        record['x_studio_quotation_type'] = 'Repair'
        record['x_studio_order_payment_method'] = record.partner_id.x_studio_payment_method
    elif record.x_studio_project_no and record.x_studio_project_no.x_studio_repair_project == True:
        record['x_studio_quotation_type'] = 'Repair'
        record['x_studio_order_payment_method'] = record.partner_id.x_studio_payment_method
```
  </details>
- **Execute Code** (`server_action_2114_rr_auto_generate_quotation_type_for_project_sos`, type `code`)
  - Function: Run by its automation: for task-linked orders sets quotation type (Repair or the project's type) and copies project group, analytic account and contract dates; the warehouse copy never runs (compares a record to True).
  - Depends on: `model project.task` (project), `model sale.order` (sale), `sale.order.task_id` (industry_fsm_sale), `sale.order.x_studio_project_end_date`, `sale.order.x_studio_project_group`<details><summary>+3 more</summary>`sale.order.x_studio_project_no`, `sale.order.x_studio_project_start_date`, `sale.order.x_studio_quotation_type`</details>
  - Used by: `automation BugFix-Sales.base_automation_186_rr_auto_generate_quotation_type_for_project_sos`
  <details><summary>code (17 lines)</summary>

```python

if record.task_id != False:
  if record.x_studio_project_no.x_studio_repair_project == True:
    record['x_studio_quotation_type'] = 'Repair'
  else:
    record['x_studio_quotation_type'] = record.x_studio_project_no.x_studio_quotation_type
  
  record['x_studio_project_group'] = record.x_studio_project_no.x_studio_project_group
  record['analytic_account_id'] = record.x_studio_project_no.sale_order_id.analytic_account_id.id
  
  project_task = env['project.task'].search([('id', '=', record.task_id.id)],limit=1)  
  if project_task:
    record['x_studio_project_start_date'] = project_task.sale_order_id.x_studio_project_start_date
    record['x_studio_project_end_date'] = project_task.sale_order_id.x_studio_project_end_date
    
    if project_task.sale_order_id.warehouse_id == True:
      record['warehouse_id'] = project_task.sale_order_id.warehouse_id.id
```
  </details>
- **Execute Code** (`server_action_2117_rr_auto_generate_quotation_type_for_project_sos_2`, type `code`)
  - Function: Run by its automation: for task-linked orders copies the project's quotation type, project group, analytic account, contract start/end dates and warehouse from the project's original SO.
  - Depends on: `model project.task` (project), `model sale.order` (sale), `sale.order.task_id` (industry_fsm_sale), `sale.order.x_studio_project_end_date`, `sale.order.x_studio_project_group`<details><summary>+3 more</summary>`sale.order.x_studio_project_no`, `sale.order.x_studio_project_start_date`, `sale.order.x_studio_quotation_type`</details>
  - Used by: `automation BugFix-Sales.base_automation_187_rr_auto_generate_quotation_type_for_project_sos_2`
  <details><summary>code (11 lines)</summary>

```python

if record.task_id != False:
  record['x_studio_quotation_type'] = record.x_studio_project_no.x_studio_quotation_type
  record['x_studio_project_group'] = record.x_studio_project_no.x_studio_project_group
  record['analytic_account_id'] = record.x_studio_project_no.sale_order_id.analytic_account_id.id
  
  project_task = env['project.task'].search([('id', '=', record.task_id.id)],limit=1)  
  if project_task:
    record['x_studio_project_start_date'] = project_task.sale_order_id.x_studio_project_start_date
    record['x_studio_project_end_date'] = project_task.sale_order_id.x_studio_project_end_date
    record['warehouse_id'] = project_task.sale_order_id.warehouse_id.id
```
  </details>
- **Execute Code** (`server_action_2250_rr_track_lock_status`, type `code`)
  - Function: Run by its automation: for Repair orders in Locked state, sets Locked, clears Unlocked and syncs the Re-estimate Count from the latest re-estimated line (writes only on change).
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `sale.order.state` (sale), `sale.order.x_studio_locked`, `sale.order.x_studio_quotation_type`<details><summary>+2 more</summary>`sale.order.x_studio_re_estimate_count`, `sale.order.x_studio_unlocked`</details>
  - Used by: `automation BugFix-Sales.base_automation_202_rr_track_lock_status`
  <details><summary>code (15 lines)</summary>

```python

# fix_repair:idempotent-v1
if record.x_studio_quotation_type == 'Repair' and record.state == 'done':
  re_line = env['sale.order.line'].sudo().search(
    [('order_id', '=', record.id), ('x_studio_re_estimated', '=', True)],
    limit=1, order='id desc')
  target_count = re_line.x_studio_count_1 if re_line else 0
  if (not record.x_studio_locked
      or record.x_studio_unlocked
      or record.x_studio_re_estimate_count != target_count):
    record.write({
      'x_studio_locked': True,
      'x_studio_unlocked': False,
      'x_studio_re_estimate_count': target_count,
    })
```
  </details>
- **Execute Code** (`server_action_2251_rr_track_lock_status_2`, type `code`)
  - Function: Run by its automation: for Repair orders in Sales Order state still flagged Locked, clears Locked and sets Unlocked.
  - Depends on: `model sale.order` (sale), `sale.order.state` (sale), `sale.order.x_studio_locked`, `sale.order.x_studio_quotation_type`, `sale.order.x_studio_unlocked`
  - Used by: `automation BugFix-Sales.base_automation_203_rr_track_lock_status_2`
  <details><summary>code (6 lines)</summary>

```python

# fix_repair:idempotent-v1
if (record.x_studio_quotation_type == 'Repair'
    and record.state == 'sale'
    and record.x_studio_locked):
  record.write({'x_studio_locked': False, 'x_studio_unlocked': True})
```
  </details>
- **Execute Code** (`server_action_2576_proj_validate_start_date_and_end_date_for_project_sos`, type `code`)
  - Function: Run by its automation: for Project orders, raises an error if the Contract Start Date is later than the Contract End Date (compared as text).
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_project_end_date`, `sale.order.x_studio_project_start_date`, `sale.order.x_studio_quotation_type`
  - Used by: `automation BugFix-Sales.base_automation_260_proj_validate_start_date_and_end_date_for_project_sos`
  <details><summary>code (7 lines)</summary>

```python

if record.x_studio_quotation_type == 'Project':
  start_date = str(record.x_studio_project_start_date) 
  end_date = str(record.x_studio_project_end_date) 
  
  if start_date > end_date:
    raise UserError('Contract Start Date cannot be later than the Contract End Date.')
```
  </details>
- **Execute Code** (`server_action_2896_proj_apply_project_price_list`, type `code`)
  - Function: Run by its automation: Project orders get the Project Price List pricelist; other orders get the customer's default pricelist.
  - Depends on: `model product.pricelist` (product), `model res.partner` (base), `model sale.order` (sale), `sale.order.partner_id` (sale), `sale.order.x_studio_quotation_type`
  - Used by: `automation BugFix-Sales.base_automation_341_proj_apply_project_price_list`
  <details><summary>code (9 lines)</summary>

```python

if record.x_studio_quotation_type == 'Project':
  pricelist = env['product.pricelist'].search([('x_studio_project_price_list', '=', True)], limit=1)
  if pricelist:
    record['pricelist_id'] = pricelist.id
else:
  customer_pricelist = env['res.partner'].search([('id', '=', record.partner_id.id)], limit=1)
  if customer_pricelist.property_product_pricelist.id: 
    record['pricelist_id'] = customer_pricelist.property_product_pricelist.id
```
  </details>
- **PROJ - Apply Project Price List** (`sa_f5_sale_order_proj_apply_project_price_list`, type `code`)
  - Function: For Project orders, sets the pricelist to the pricelist flagged as Project Price List; for other orders, resets it to the customer's default pricelist.
  - Depends on: `model product.pricelist` (product), `model res.partner` (base), `model sale.order` (sale), `sale.order.partner_id` (sale), `sale.order.x_studio_quotation_type`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (8 lines)</summary>

```python
if record.x_studio_quotation_type == 'Project':
  pricelist = env['product.pricelist'].search([('x_studio_project_price_list', '=', True)], limit=1)
  if pricelist:
    record['pricelist_id'] = pricelist.id
else:
  customer_pricelist = env['res.partner'].search([('id', '=', record.partner_id.id)], limit=1)
  if customer_pricelist.property_product_pricelist.id: 
    record['pricelist_id'] = customer_pricelist.property_product_pricelist.id
```
  </details>
- **PROJ - Create Budget Entries** (`server_action_2178_proj_create_budget_entries`, type `code`)
  - Function: Button action on a Project SO: requires contract start/end dates, creates an analytic account (plan 'Projects') and a budget linked to the SO (using the main project's analytic account if any), then opens the new budget.
  - Depends on: `model account.analytic.account` (analytic), `model account.analytic.plan` (analytic), `model crossovered.budget` (account_budget), `model sale.order` (sale), `sale.order.name` (sale)<details><summary>+8 more</summary>`sale.order.partner_id` (sale), `sale.order.task_id` (industry_fsm_sale), `sale.order.x_studio_budget_created`, `sale.order.x_studio_main_project_no`, `sale.order.x_studio_project_budget`, `sale.order.x_studio_project_end_date`, `sale.order.x_studio_project_no`, `sale.order.x_studio_project_start_date`</details>
  - Used by: `view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` (BugFix-Accounting)
  <details><summary>code (83 lines)</summary>

```python
if record.id:
  seq = ''
  
  # --- FIX: Get required Analytic Plan ---
  plan = env['account.analytic.plan'].search([('name', '=', 'Projects')], limit=1)
  if not plan:
    raise UserError('Required Analytic Plan "Projects" not found!')
  # --- END FIX ---
  
  # --- FIX: Also check for main project plan ---
  analytic_acc_main_project = None
  if record.x_studio_main_project_no:
    analytic_acc_main_project = env['account.analytic.account'].search([
        ('name', '=', record.x_studio_main_project_no.name)
    ], limit=1)
  # --- END FIX ---
  
  if record.x_studio_project_start_date == False and record.x_studio_project_end_date == False:
    raise UserError(' Project Start date and End date must be defined.')
  elif record.x_studio_project_start_date == False:
    raise UserError('Project Start date must be defined.')
  elif record.x_studio_project_end_date == False:
    raise UserError('Project End date must be defined.')
  
  # --- FIX: Add plan_id to create call ---
  analytic_acc = env['account.analytic.account'].create({
      'name': record.name,
      'partner_id': record.partner_id.id,
      'plan_id': plan.id  # THIS IS REQUIRED
  })
  # --- END FIX ---
    
  if record.x_studio_project_no.id == False:
    seq = record.name
    if analytic_acc_main_project:
      budget = env['crossovered.budget'].create({
          'x_studio_created_from_sales_order_1': record.id,
          'name': seq,
          'x_studio_analytic_account': analytic_acc_main_project.id,
          'date_from': record.x_studio_project_start_date,
          'date_to': record.x_studio_project_end_date
      })  
    else:
      budget = env['crossovered.budget'].create({
          'x_studio_created_from_sales_order_1': record.id,
          'name': seq,
          'x_studio_analytic_account': analytic_acc.id,
          'date_from': record.x_studio_project_start_date,
          'date_to': record.x_studio_project_end_date
      })  
  else:
    seq = (str(record.x_studio_project_no.name) + "/" + str(record.task_id.name) + "/" + str(record.name))
    if analytic_acc_main_project:
      budget = env['crossovered.budget'].create({
          'x_studio_created_from_sales_order_1': record.id,
          'name': seq,
          'x_studio_project_no': record.x_studio_project_no.id,
          'x_studio_analytic_account': analytic_acc_main_project.id,
          'date_from': record.x_studio_project_start_date,
          'date_to': record.x_studio_project_end_date
      })   
    else:
      budget = env['crossovered.budget'].create({
          'x_studio_created_from_sales_order_1': record.id,
          'name': seq,
          'x_studio_project_no': record.x_studio_project_no.id,
          'x_studio_analytic_account': analytic_acc.id,
          'date_from': record.x_studio_project_start_date,
          'date_to': record.x_studio_project_end_date
      })  
  
  action = {
          'name': 'Budgets',
          'domain': [('id', '=', budget.id)],
          'type': 'ir.actions.act_window',
          'res_model': 'crossovered.budget',
          'view_mode': 'tree,form',
          'view_type': 'form',
          'view_id': False,
          'context': False,
          } 

  record.write({'x_studio_budget_created': True, 'x_studio_project_budget': budget.id, 'analytic_account_id': analytic_acc.id})
```
  </details>
- **PROJ - Create PR from Sales Quotation** (`server_action_2188_proj_create_pr_from_sales_quotation`, type `code`)
  - Function: Button action: refreshes stock/cost details on each SO line, validates Purchase Type, then creates up to four Purchase Requests (Local/Import, normal shortage vs subcontracting) from the lines, marks lines and SO as PR Created, and opens the created requests.
  - Depends on: `model sale.order` (sale), `model stock.picking.type` (stock), `model stock.quant` (stock), `model stock.warehouse` (stock), `model x_purchase_request` (BugFix-Purchase)<details><summary>+4 more</summary>`sale.order.order_line` (sale), `sale.order.warehouse_id` (sale_stock), `sale.order.x_studio_pr_created`, `sale.order.x_studio_sub_contract`</details>
  - Used by: `view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)
  <details><summary>code (268 lines)</summary>

```python
pr_lines=[]
pr_lines2=[]
pr_lines3=[]
pr_lines4=[]
local_count = 0
import_count = 0
sub_local_count = 0
sub_import_count = 0

onhand_qty = 0
qty_short = 0
re_wh = False
status = True 

#######
for update_line in record.order_line:
  if update_line.x_studio_product_status != 'Blank':
    so_loc = env['stock.warehouse'].search([('id', '=', update_line.warehouse_id.id)],limit=1)
    if so_loc:
      for sup_lines in so_loc.resupply_wh_ids:
        for routes in update_line.product_template_id.route_ids:
          if routes.supplier_wh_id:
            if routes.supplier_wh_id.id == sup_lines.id:
              if routes.supplied_wh_id.id == update_line.warehouse_id.id:
                onhand = env['stock.quant'].search([('product_tmpl_id', '=', update_line.product_template_id.id),('location_id', '=', routes.supplier_wh_id.lot_stock_id.id)], limit=1)
                if onhand:
                  onhand_qty = onhand.available_quantity
              re_wh = routes.supplier_wh_id.id
   
    if update_line.product_template_id.detailed_type == 'service':
      qty_short = 0
    else:
      if update_line.product_uom_qty > onhand_qty:
        qty_short = (update_line.product_uom_qty - onhand_qty)
        status = False
    update_line.write({'x_studio_cost_value': update_line.product_template_id.standard_price, 'x_studio_warehouse_id': re_wh, 'x_studio_current_onhand': onhand_qty, 'x_studio_inventory_shortage': qty_short, 'x_studio_cost_amount_req_qty': (update_line.product_uom_qty * update_line.product_template_id.standard_price), 'x_studio_cost_amount_inventory_shortage': (qty_short * update_line.product_template_id.standard_price), 'x_studio_invt_status': status})
#######

for line in record.order_line:
  if line.x_studio_sub_contract == True:
    if (line.x_studio_purch_type == False):
      raise UserError("The 'Purchase Type' should be filled in for all the Sales lines with subcontracting service items to proceed.")  
      
    if (line.x_studio_purch_type == 'Local'):
      sub_local_count += 1
      pr_lines3.append([0,0,{
          'x_studio_many2one_field_WAqP4':line.product_id.id,
          'x_studio_quantity':line.product_uom_qty,
          'x_studio_requested_by':uid,
          'x_studio_sales_line_id':line.id}])
      
      line.write({'x_studio_pr_created':True}) 
          
    if (line.x_studio_purch_type == 'Import'):
      sub_import_count += 1
      pr_lines4.append([0,0,{
          'x_studio_many2one_field_WAqP4':line.product_id.id,
          'x_studio_quantity':line.product_uom_qty,
          'x_studio_requested_by':uid,
          'x_studio_sales_line_id':line.id}])
          
      line.write({'x_studio_pr_created':True})
  else:
    if (line.x_studio_purch_type == False) and (line.x_studio_inventory_shortage > 0):
      raise UserError("The Purchase Type should be filled in for all the SO lines with inventory items.")
      
    if (line.x_studio_purch_type == 'Local') and (line.x_studio_inventory_shortage > 0):
      local_count += 1
      pr_lines.append([0,0,{
          'x_studio_many2one_field_WAqP4':line.product_id.id,
          'x_studio_quantity':line.x_studio_inventory_shortage,
          'x_studio_requested_by':uid,
          'x_studio_sales_line_id':line.id}])
      
      line.write({'x_studio_pr_created':True}) 
          
    if (line.x_studio_purch_type == 'Import') and (line.x_studio_inventory_shortage > 0):
      import_count += 1
      pr_lines2.append([0,0,{
          'x_studio_many2one_field_WAqP4':line.product_id.id,
          'x_studio_quantity':line.x_studio_inventory_shortage,
          'x_studio_requested_by':uid,
          'x_studio_sales_line_id':line.id}])
          
      line.write({'x_studio_pr_created':True}) 
        
wh = env['stock.picking.type'].search([('warehouse_id', '=', record.warehouse_id.id)],limit=1)

if local_count > 0:
  pr1 = env['x_purchase_request'].create({'x_studio_type': 'Local','x_studio_created_from_so':record.id,'x_studio_so_pr':True,'x_studio_warehouse':wh.id,'x_studio_requested_delivery_date':datetime.datetime.today(),'x_studio_requested_by':uid,'x_studio_order_lines_1':pr_lines})

if import_count > 0:
  pr2 = env['x_purchase_request'].create({'x_studio_type': 'Import','x_studio_created_from_so':record.id,'x_studio_so_pr':True,'x_studio_warehouse':wh.id,'x_studio_requested_delivery_date':datetime.datetime.today(),'x_studio_requested_by':uid,'x_studio_order_lines_1':pr_lines2})

if sub_local_count > 0:
  pr3 = env['x_purchase_request'].create({'x_studio_type': 'Local','x_studio_created_from_so':record.id,'x_studio_subcontracting_pr':True,'x_studio_warehouse':wh.id,'x_studio_requested_delivery_date':datetime.datetime.today(),'x_studio_requested_by':uid,'x_studio_order_lines_1':pr_lines3})

if sub_import_count > 0:
  pr4 = env['x_purchase_request'].create({'x_studio_type': 'Import','x_studio_created_from_so':record.id,'x_studio_subcontracting_pr':True,'x_studio_warehouse':wh.id,'x_studio_requested_delivery_date':datetime.datetime.today(),'x_studio_requested_by':uid,'x_studio_order_lines_1':pr_lines4})

record.write({'x_studio_pr_created':True})  


if (local_count > 0) and (import_count > 0) and (sub_local_count > 0) and (sub_import_count > 0):
  action = {
          'name': 'Purchase Requisition',
          'domain': [('id', '=', [pr1.id,pr2.id,pr3.id,pr4.id])],
          'type': 'ir.actions.act_window',
          'res_model': 'x_purchase_request',
          'view_mode': 'tree,form',
          'view_type': 'form',
          'view_id': False,
          'context': False,
          }
elif (local_count > 0) and (import_count > 0) and (sub_local_count > 0):
  action = {
          'name': 'Purchase Requisition',
          'domain': [('id', '=', [pr1.id,pr2.id,pr3.id])],
          'type': 'ir.actions.act_window',
          'res_model': 'x_purchase_request',
# … 148 more lines
```
  </details>
- **PROJ - Project Item Approval** (`server_action_2142_proj_project_item_approval`, type `object_write`)
  - Function: Sets Project Item Approved to 'Yes' on the sales order. Not referenced by any parent action in this repo.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_project_item_approved`
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
- **PROJ - Project Item Approval Request  Sent - Validate** (`server_action_2138_proj_project_item_approval_request_sent_validate`, type `code`)
  - Function: Lists the order's 'New Item' lines whose product is not yet approved and raises an error 'Pending Approval for Bellow Item/s'. It raises unconditionally, even when no items are pending.
  - Depends on: `model sale.order` (sale), `sale.order.order_line` (sale)
  - Used by: `server action BugFix-Sales.server_action_2140_proj_request_project_item_approval`, `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
  <details><summary>code (13 lines)</summary>

```python
desc = ''

for items in record.order_line:

  if items.x_studio_product_status == 'New Item':

    if items.product_id.x_studio_item_approved == False:

      desc +=  str(items.product_id.name) + "\n"



raise UserError("Pending Approval for Bellow Item/s." + "\n" + "\n" + desc)
```
  </details>
- **PROJ - Project Item Request  Sent** (`server_action_2134_proj_project_item_request_sent`, type `object_write`)
  - Function: Sets Project Item Request Sent to 'Yes' on the sales order; step of 'PROJ - Request Project Item Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_project_item_request_sent`
  - Used by: `server action BugFix-Sales.server_action_2140_proj_request_project_item_approval`
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
- **PROJ - Project Item Request Approval - Notify User** (`server_action_2136_proj_project_item_request_approval_notify_user`, type `next_activity`)
  - Function: Schedules an activity on the sales order to notify the user about a Project Item approval request; called by 'PROJ - Request Project Item Approval'. The code body is only the default template.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_2140_proj_request_project_item_approval`
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
- **PROJ - Request Project Item Approval** (`server_action_2140_proj_request_project_item_approval`, type `multi`)
  - Function: Multi-step action for requesting project item approval: sets Project Item Request Sent, schedules a notify activity, and runs the pending-items check (which always raises an error).
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2134_proj_project_item_request_sent`, `server action BugFix-Sales.server_action_2136_proj_project_item_request_approval_notify_user`, `server action BugFix-Sales.server_action_2138_proj_project_item_approval_request_sent_validate`
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
- **PROJ - Update RFQ Cost to Sales Quotation** (`server_action_2192_proj_update_rfq_cost_to_sales_quotation`, type `code`)
  - Function: Button action: for each line with a PR created, copies the finalized RFQ cost from the linked purchase request line into the line's Cost Value (error if not finalized), then marks the SO PR Cost Updated.
  - Depends on: `model sale.order` (sale), `model x_purchase_request_lin` (BugFix-Purchase), `sale.order.order_line` (sale), `sale.order.x_studio_pr_cost_updated`, `sale.order.x_studio_pr_created`
  - Used by: `view BugFix-Purchase.ported_odoo_studio_sale_ord_pur` (BugFix-Purchase)
  <details><summary>code (11 lines)</summary>

```python
if record.id:
  for line in record.order_line:
    if line.x_studio_pr_created == True:
      pr = env['x_purchase_request_lin'].search([('x_studio_sales_line_id', '=', line.id), ('x_studio_rfq_cost_updated', '=', True)],limit=1)
      if pr:
        line.write({'x_studio_cost_value': pr.x_studio_rfq_cost})
      else:
        raise UserError('RFQs are not finalized to update the cost.')


record.write({'x_studio_pr_cost_updated':True})
```
  </details>
- **PROJ - Update with Main SO** (`server_action_2572_proj_update_with_main_so`, type `code`)
  - Function: Meant to copy contract start/end dates and warehouse from the task's main SO and set Update with Main SO; references an undefined variable `project`, so it errors when run. Not referenced in this repo.
  - Depends on: `model project.task` (project), `model sale.order` (sale), `sale.order.task_id` (industry_fsm_sale), `sale.order.x_studio_project_end_date`, `sale.order.x_studio_project_start_date`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (6 lines)</summary>

```python
project_task = env['project.task'].search([('id', '=', record.task_id.id)],limit=1)  
if project:
  record['x_studio_project_start_date'] = project_task.sale_order_id.x_studio_project_start_date
  record['x_studio_project_end_date'] = project_task.sale_order_id.x_studio_project_end_date
  record['warehouse_id'] = project_task.sale_order_id.warehouse_id.id
  record['x_studio_update_with_main_so'] = True
```
  </details>
- **PROJ - Validate Start date and End date for Project SOs** (`sa_f5_sale_order_proj_validate_start_date_and_end_date_for_project_sos`, type `code`)
  - Function: For Project orders, raises an error if the Contract Start Date is later than the Contract End Date (compared as strings).
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_project_end_date`, `sale.order.x_studio_project_start_date`, `sale.order.x_studio_quotation_type`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (6 lines)</summary>

```python
if record.x_studio_quotation_type == 'Project':
  start_date = str(record.x_studio_project_start_date) 
  end_date = str(record.x_studio_project_end_date) 
  
  if start_date > end_date:
    raise UserError('Contract Start Date cannot be later than the Contract End Date.')
```
  </details>
- **Project Sales Order Seq.No** (`server_action_2573_project_sales_order_seq_no`, type `code`)
  - Function: For Project orders, appends '_PRJ' to the order number (no guard against repeated suffixes).
  - Depends on: `model ir.sequence` (base), `model sale.order` (sale), `sale.order.name` (sale), `sale.order.x_studio_quotation_type`
  - Used by: `automation BugFix-Sales.base_automation_257_jin_project_sales_order_seq_no`
  <details><summary>code (4 lines)</summary>

```python
if record.x_studio_quotation_type == 'Project':
 #seq = env['ir.sequence'].next_by_code('project.sale.order.seq')
 #record.write({'name': seq})
 record.write({'name': record.name + '_PRJ'})
```
  </details>
- **Project Sales Order Seq.No - 2** (`server_action_2574_project_sales_order_seq_no_2`, type `code`)
  - Function: Keeps the order number in sync with quotation type: adds a single '_PRJ' suffix for Project orders and removes it otherwise.
  - Depends on: `model sale.order` (sale), `sale.order.name` (sale), `sale.order.x_studio_quotation_type`
  - Used by: `automation BugFix-Sales.base_automation_258_jin_project_sales_order_seq_no_maintain_separate_nos_for_pro`
  <details><summary>code (8 lines)</summary>

```python
# fix_repair:idempotent-v1
if record.id:
  original_name = (record.name or '').replace('_PRJ', '')
  new_name = (original_name + '_PRJ'
              if record.x_studio_quotation_type == 'Project'
              else original_name)
  if record.name != new_name:
    record.write({'name': new_name})
```
  </details>
- **Project Sales Order Seq.No - 3** (`server_action_2575_project_sales_order_seq_no_3`, type `code`)
  - Function: Keeps the order number in sync with quotation type: adds one '_PRJ' suffix for Project orders and removes it otherwise. Not referenced by any automation in this repo.
  - Depends on: `model sale.order` (sale), `sale.order.name` (sale), `sale.order.x_studio_quotation_type`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (8 lines)</summary>

```python
# fix_repair:idempotent-v1
if record.id:
  original_name = (record.name or '').replace('_PRJ', '')
  new_name = (original_name + '_PRJ'
              if record.x_studio_quotation_type == 'Project'
              else original_name)
  if record.name != new_name:
    record.write({'name': new_name})
```
  </details>
- **RR - Auto Generate Quotation Type for Projct SOs** (`server_action_2113_rr_auto_generate_quotation_type_for_projct_sos`, type `code`)
  - Function: Unconditionally sets the order's quotation type to 'Project' (the task check is commented out). Not referenced by any automation in this repo.
  - Depends on: `model sale.order` (sale), `sale.order.task_id` (industry_fsm_sale), `sale.order.x_studio_quotation_type`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
#if record.task_id == True:
record['x_studio_quotation_type'] = 'Project'
```
  </details>
- **RR - Auto Generate Quotation Type for Project SOs** (`sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos`, type `code`)
  - Function: For orders linked to a project task, sets quotation type to 'Repair' (repair project) or the project's quotation type, and copies project group, analytic account and contract start/end dates from the project's original SO. The warehouse copy never runs (compares a record to True).
  - Depends on: `model project.task` (project), `model sale.order` (sale), `sale.order.task_id` (industry_fsm_sale), `sale.order.x_studio_project_end_date`, `sale.order.x_studio_project_group`<details><summary>+3 more</summary>`sale.order.x_studio_project_no`, `sale.order.x_studio_project_start_date`, `sale.order.x_studio_quotation_type`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (16 lines)</summary>

```python
if record.task_id != False:
  if record.x_studio_project_no.x_studio_repair_project == True:
    record['x_studio_quotation_type'] = 'Repair'
  else:
    record['x_studio_quotation_type'] = record.x_studio_project_no.x_studio_quotation_type
  
  record['x_studio_project_group'] = record.x_studio_project_no.x_studio_project_group
  record['analytic_account_id'] = record.x_studio_project_no.sale_order_id.analytic_account_id.id
  
  project_task = env['project.task'].search([('id', '=', record.task_id.id)],limit=1)  
  if project_task:
    record['x_studio_project_start_date'] = project_task.sale_order_id.x_studio_project_start_date
    record['x_studio_project_end_date'] = project_task.sale_order_id.x_studio_project_end_date
    
    if project_task.sale_order_id.warehouse_id == True:
      record['warehouse_id'] = project_task.sale_order_id.warehouse_id.id
```
  </details>
- **RR - Auto Generate Quotation Type for Project SOs - 2** (`sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos_2`, type `code`)
  - Function: For orders linked to a project task, copies the project's quotation type, project group, analytic account, and the original SO's contract start/end dates and warehouse onto the order.
  - Depends on: `model project.task` (project), `model sale.order` (sale), `sale.order.task_id` (industry_fsm_sale), `sale.order.x_studio_project_end_date`, `sale.order.x_studio_project_group`<details><summary>+3 more</summary>`sale.order.x_studio_project_no`, `sale.order.x_studio_project_start_date`, `sale.order.x_studio_quotation_type`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (10 lines)</summary>

```python
if record.task_id != False:
  record['x_studio_quotation_type'] = record.x_studio_project_no.x_studio_quotation_type
  record['x_studio_project_group'] = record.x_studio_project_no.x_studio_project_group
  record['analytic_account_id'] = record.x_studio_project_no.sale_order_id.analytic_account_id.id
  
  project_task = env['project.task'].search([('id', '=', record.task_id.id)],limit=1)  
  if project_task:
    record['x_studio_project_start_date'] = project_task.sale_order_id.x_studio_project_start_date
    record['x_studio_project_end_date'] = project_task.sale_order_id.x_studio_project_end_date
    record['warehouse_id'] = project_task.sale_order_id.warehouse_id.id
```
  </details>
- **RR - Auto Generate Quotation Type for Repair SOs** (`sa_f5_sale_order_rr_auto_generate_quotation_type_for_repair_sos`, type `code`)
  - Function: Sets quotation type to 'Repair' and copies the customer's payment method to the order when the order is linked to a task in a repair project (or its project is a repair project).
  - Depends on: `model project.task` (project), `model sale.order` (sale), `sale.order.partner_id` (sale), `sale.order.x_studio_order_payment_method`, `sale.order.x_studio_project_no`<details><summary>+1 more</summary>`sale.order.x_studio_quotation_type`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
if record.id:
    # x_studio_project_no is never set by FSM - use task link instead
    task = env['project.task'].search([
        ('sale_order_id', '=', record.id),
        ('project_id.x_studio_repair_project', '=', True)
    ], limit=1)
    if task:
        record['x_studio_quotation_type'] = 'Repair'
        record['x_studio_order_payment_method'] = record.partner_id.x_studio_payment_method
    elif record.x_studio_project_no and record.x_studio_project_no.x_studio_repair_project == True:
        record['x_studio_quotation_type'] = 'Repair'
        record['x_studio_order_payment_method'] = record.partner_id.x_studio_payment_method
```
  </details>
- **RR - Insufficient Transfer Inventory Details** (`server_action_2096_rr_insufficient_transfer_inventory_details`, type `code`)
  - Function: Button action that builds a list of order lines whose total ordered qty exceeds stock in the resupply (or own) warehouse, showing location, order qty, on-hand and shortage, and displays it as an error message.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `model stock.quant` (stock), `model stock.warehouse` (stock), `sale.order.order_line` (sale)<details><summary>+1 more</summary>`sale.order.warehouse_id` (sale_stock)</details>
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
  <details><summary>code (50 lines)</summary>

```python
desc = ''
onhand_qty = 0
onhand_qty2 = 0
resupply_count = 0

so_loc = env['stock.warehouse'].search([('id', '=', record.warehouse_id.id)],limit=1)
if so_loc:
  for sup_lines in so_loc.resupply_wh_ids:
    resupply_count += 1
    for line in record.order_line:
      same_item = env['sale.order.line'].search([('order_id', '=', record.id),('product_template_id', '=', line.product_template_id.id)])
      if same_item:
        onhand_qty = 0
        for sameitems in same_item:
          onhand_qty += sameitems.product_uom_qty
      else:
       onhand_qty = line.product_uom_qty 
      for routes in line.product_template_id.route_ids:
        if routes.supplier_wh_id:
          if routes.supplier_wh_id.id == sup_lines.id:
            if routes.supplied_wh_id.id == record.warehouse_id.id:
              onhand = env['stock.quant'].search([('product_tmpl_id', '=', line.product_template_id.id),('location_id', '=', routes.supplier_wh_id.lot_stock_id.id),('quantity', '>=', onhand_qty)], limit=1)
              if not onhand:
                onhand2 = env['stock.quant'].search([('product_tmpl_id', '=', line.product_template_id.id),('location_id', '=', routes.supplier_wh_id.lot_stock_id.id)], limit=1)
                if onhand2:
                  onhand_qty2 = onhand2.quantity
                else: 
                  onhand_qty2 = 0
                desc +=  "Item No: " + str(line.product_template_id.default_code) + "     " + "Location: " + str(routes.supplier_wh_id.lot_stock_id.display_name) + "     " + "Order Qty (Line): " + str(line.product_uom_qty) + "     "  + "     " + "Order Qty (Total): " + str(onhand_qty) + "     "  + "Onhand Qty: " + str(onhand_qty2) + "     " + "Inventory Shortage: " + str(onhand_qty - onhand_qty2) + "\n"

if resupply_count == 0:
  for line in record.order_line:
    same_item = env['sale.order.line'].search([('order_id', '=', record.id),('product_template_id', '=', line.product_template_id.id)])
    if same_item:
      onhand_qty = 0
      for sameitems in same_item:
        onhand_qty += sameitems.product_uom_qty
    else:
     onhand_qty = line.product_uom_qty 
    
    onhand = env['stock.quant'].search([('product_tmpl_id', '=', line.product_template_id.id),('location_id', '=', record.warehouse_id.lot_stock_id.id),('quantity', '>=', onhand_qty)], limit=1)
    if not onhand:
      onhand2 = env['stock.quant'].search([('product_tmpl_id', '=', line.product_template_id.id),('location_id', '=', record.warehouse_id.lot_stock_id.id)], limit=1)
      if onhand2:
        onhand_qty2 = onhand2.quantity
      else: 
        onhand_qty2 = 0
      desc +=  "Item No: " + str(line.product_template_id.default_code) + "     " + "Location: " + str(record.warehouse_id.lot_stock_id.display_name) + "     " + "Order Qty (Line): " + str(line.product_uom_qty) + "     "  + "     " + "Order Qty (Total): " + str(onhand_qty) + "     "  + "Onhand Qty: " + str(onhand_qty2) + "     " + "Inventory Shortage: " + str(onhand_qty - onhand_qty2) + "\n"
    
raise UserError(desc)
```
  </details>
- **RR - RUG Approval** (`server_action_1981_rr_rug_approval`, type `object_write`)
  - Function: Sets RUG Approved to 'Yes' on the (Repair) sales order. Not referenced by any parent action in this repo.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_rug_approved`
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
- **RR - RUG Approval Request Sent** (`server_action_1983_rr_rug_approval_request_sent`, type `object_write`)
  - Function: Sets RUG Request Sent to 'Yes' on the sales order; step of 'RR - Request RUG Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_rug_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1980_rr_request_rug_approval`
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
- **RR - RUG Rejection** (`server_action_2004_rr_rug_rejection`, type `code`)
  - Function: Marks the order RUG Rejected and restores each line's unit price from its saved Original Price.
  - Depends on: `model sale.order` (sale), `sale.order.order_line` (sale), `sale.order.x_studio_rug_rejected`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (6 lines)</summary>

```python
if record.id:
  record.write({'x_studio_rug_rejected': True})
  
  for lines in record.order_line:
    original_price = lines.x_studio_price_unit_original
    lines.write({'price_unit':original_price})
```
  </details>
- **RR - RUG Request Approval - Notify User** (`server_action_1985_rr_rug_request_approval_notify_user`, type `next_activity`)
  - Function: Schedules an activity on the sales order to notify the user of a RUG approval request; called by 'RR - Request RUG Approval'. The code body is only the default template.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1980_rr_request_rug_approval`
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
- **RR - Re-estimate Request  Sent** (`server_action_2244_rr_re_estimate_request_sent`, type `object_write`)
  - Function: Sets Re-estimate Request Sent to 'Yes' on the sales order; step of 'RR - Request Re-estimate Permission'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_re_estimate_request_sent`
  - Used by: `server action BugFix-Sales.server_action_2248_rr_request_re_estimate_permission`
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
- **RR - Re-estimate Request  Sent - Validate** (`server_action_2246_rr_re_estimate_request_sent_validate`, type `code`)
  - Function: Increments the order's Re-estimate Request Count by one; step of 'RR - Request Re-estimate Permission'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_re_estimate_request_count_1`
  - Used by: `server action BugFix-Sales.server_action_2248_rr_request_re_estimate_permission`
  <details><summary>code (2 lines)</summary>

```python
if record.id:
  record['x_studio_re_estimate_request_count_1'] += 1
```
  </details>
- **RR - Re-estimate Request - Notify User** (`server_action_2243_rr_re_estimate_request_notify_user`, type `next_activity`)
  - Function: Schedules an activity on the sales order to notify the user of a re-estimate permission request; called by 'RR - Request Re-estimate Permission'. The code body is only the default template.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_2248_rr_request_re_estimate_permission`
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
- **RR - Request RUG Approval** (`server_action_1980_rr_request_rug_approval`, type `multi`)
  - Function: Multi-step action behind the Repair 'Request RUG Approval' button: sets RUG Request Sent and schedules a notify activity for the approver.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_1983_rr_rug_approval_request_sent`, `server action BugFix-Sales.server_action_1985_rr_rug_request_approval_notify_user`
  - Used by: `view Fix-repair.view_sale_order_rug_direct_buttons` (Fix-repair)
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
- **RR - Request Re-estimate Permission** (`server_action_2248_rr_request_re_estimate_permission`, type `multi`)
  - Function: Multi-step action requesting re-estimate permission on a Repair order: sets Re-estimate Request Sent, schedules a notify activity, and increments the re-estimate request count.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2243_rr_re_estimate_request_notify_user`, `server action BugFix-Sales.server_action_2244_rr_re_estimate_request_sent`, `server action BugFix-Sales.server_action_2246_rr_re_estimate_request_sent_validate`
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
- **RR - Track Lock Status** (`sa_f5_sale_order_rr_track_lock_status`, type `code`)
  - Function: For Repair orders in Locked (done) state, marks the order Locked, clears Unlocked and syncs the Re-estimate Count from the latest re-estimated line; writes only when something differs.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `sale.order.state` (sale), `sale.order.x_studio_locked`, `sale.order.x_studio_quotation_type`<details><summary>+2 more</summary>`sale.order.x_studio_re_estimate_count`, `sale.order.x_studio_unlocked`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (14 lines)</summary>

```python
# fix_repair:idempotent-v1
if record.x_studio_quotation_type == 'Repair' and record.state == 'done':
  re_line = env['sale.order.line'].sudo().search(
    [('order_id', '=', record.id), ('x_studio_re_estimated', '=', True)],
    limit=1, order='id desc')
  target_count = re_line.x_studio_count_1 if re_line else 0
  if (not record.x_studio_locked
      or record.x_studio_unlocked
      or record.x_studio_re_estimate_count != target_count):
    record.write({
      'x_studio_locked': True,
      'x_studio_unlocked': False,
      'x_studio_re_estimate_count': target_count,
    })
```
  </details>
- **RR - Track Lock Status - 2** (`sa_f5_sale_order_rr_track_lock_status_2`, type `code`)
  - Function: For Repair orders back in Sales Order state that are flagged Locked, clears Locked and sets Unlocked (i.e. order was unlocked).
  - Depends on: `model sale.order` (sale), `sale.order.state` (sale), `sale.order.x_studio_locked`, `sale.order.x_studio_quotation_type`, `sale.order.x_studio_unlocked`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
# fix_repair:idempotent-v1
if (record.x_studio_quotation_type == 'Repair'
    and record.state == 'sale'
    and record.x_studio_locked):
  record.write({'x_studio_locked': False, 'x_studio_unlocked': True})
```
  </details>
- **RR - Track Lock Status - 4** (`server_action_2253_rr_track_lock_status_4`, type `code`)
  - Function: For Repair orders in Locked state, sets Locked, clears Unlocked and syncs the Re-estimate Count from the latest re-estimated line (writes only on change). Not referenced in this repo.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `sale.order.state` (sale), `sale.order.x_studio_locked`, `sale.order.x_studio_quotation_type`<details><summary>+2 more</summary>`sale.order.x_studio_re_estimate_count`, `sale.order.x_studio_unlocked`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (14 lines)</summary>

```python
# fix_repair:idempotent-v1
if record.x_studio_quotation_type == 'Repair' and record.state == 'done':
  re_line = env['sale.order.line'].sudo().search(
    [('order_id', '=', record.id), ('x_studio_re_estimated', '=', True)],
    limit=1, order='id desc')
  target_count = re_line.x_studio_count_1 if re_line else 0
  if (not record.x_studio_locked
      or record.x_studio_unlocked
      or record.x_studio_re_estimate_count != target_count):
    record.write({
      'x_studio_locked': True,
      'x_studio_unlocked': False,
      'x_studio_re_estimate_count': target_count,
    })
```
  </details>
- **SLS - Bank Guarantee - Notify User** (`server_action_1769_sls_bank_guarantee_notify_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order to notify a user about the customer's bank guarantee status. Not referenced by any automation or parent action in this repo.
  - Depends on: `model sale.order` (sale)
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
- **SLS - Bank Guarantee - Notify User** (`server_action_2260_sls_bank_guarantee_notify_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order to notify a user about the customer's bank guarantee status (duplicate of action 1769). Not referenced by any automation or parent action in this repo.
  - Depends on: `model sale.order` (sale)
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
- **SLS - Bank Guarantee Approval** (`server_action_2507_sls_bank_guarantee_approval`, type `object_write`)
  - Function: Sets Bank Guarantee Approved to 'Yes' on the sales order; step of 'SLS - Bank Guarantee Approval - Main'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_bank_guarantee_approved`
  - Used by: `server action BugFix-Sales.server_action_1487_sls_bank_guarantee_approval_main`
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
- **SLS - Bank Guarantee Approval - Confirm** (`server_action_2509_sls_bank_guarantee_approval_confirm`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order confirming the bank guarantee approval; step of 'SLS - Bank Guarantee Approval - Main'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1487_sls_bank_guarantee_approval_main`
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
- **SLS - Bank Guarantee Approval - Main** (`server_action_1487_sls_bank_guarantee_approval_main`, type `multi`)
  - Function: Multi-step bank guarantee approval button (gated by an approval rule): sets Bank Guarantee Approved to 'Yes' and schedules a confirmation activity.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2507_sls_bank_guarantee_approval`, `server action BugFix-Sales.server_action_2509_sls_bank_guarantee_approval_confirm`
  - Used by: `approval rule BugFix-Sales.ar_final_sales_order_sls_bank_guarantee_approval_sales_bank_guarantee`, `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Create Customer Payment** (`server_action_2341_sls_create_customer_payment`, type `code`)
  - Function: Button action creating a draft customer payment for the SO in the 'Advance Payment' (or 'Advance Payment - Repairs') journal: amount is the unpaid balance, or for a first Repair payment the company Advance Payment %; then opens it. Gated by an approval rule.
  - Depends on: `model account.journal` (account), `model account.payment` (account), `model res.company` (base), `model sale.order` (sale), `sale.order.amount_total` (sale)<details><summary>+6 more</summary>`sale.order.company_id` (sale), `sale.order.partner_id` (sale), `sale.order.x_studio_customer_payment_method`, `sale.order.x_studio_order_payment_method`, `sale.order.x_studio_project_no`, `sale.order.x_studio_quotation_type`</details>
  - Used by: `approval rule BugFix-Sales.ar_final_sales_order_sls_create_customer_payment_user_types_internal_`, `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
  <details><summary>code (106 lines)</summary>

```python
# bugfix_sales:config-cutover-v22
if record.id:

  sum_total = 0

  so_value = 0

  journal = 0

  

  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]

  company = env['res.company'].browse(company_id)

  

  if record.x_studio_quotation_type == 'Repair':

    journal = env['account.journal'].search([('name', '=', 'Advance Payment - Repairs'),('company_id', '=', company.id)], limit=1) 

    if not journal:

       raise UserError('The required journal has not been setup. Process terminated.')

    

    payment = env['account.payment'].search([('x_studio_sales_order', '=', record.id),('state', '!=', 'cancel')])

    if payment:

      for total in payment:

        sum_total += total.amount

        

      so_value = (record.amount_total - sum_total)

    else:

      min_magin = record.company_id

      if min_magin:

        so_value = round(record.amount_total * (min_magin.x_studio_advance_payment_/100),2)

      

  else:

    journal = env['account.journal'].search([('name', '=', 'Advance Payment'),('company_id', '=', company.id)], limit=1) 

    if not journal:

       raise UserError('The required journal has not been setup. Process terminated.')

    

    payment = env['account.payment'].search([('x_studio_sales_order', '=', record.id),('state', '!=', 'cancel')])

    if payment:

      for total in payment:

        sum_total += total.amount

        

      so_value = (record.amount_total - sum_total)

    else:

      min_magin = record.company_id

      if min_magin:

        so_value = record.amount_total

  

  

  customer_payment = env['account.payment'].create({'x_studio_sales_order':record.id,'x_studio_project_no_1': record.x_studio_project_no.id if record.x_studio_project_no else False,'partner_id':record.partner_id.id,'amount':so_value,'date':datetime.date.today(),'x_studio_order_payment_method':record.x_studio_customer_payment_method,'journal_id':journal.id,'payment_method_line_id':journal.inbound_payment_method_line_ids[:1].id if journal.inbound_payment_method_line_ids else False})

  

  action = {

           'name': 'Draft Payment',

           'domain': [('id', '=', customer_payment.id)],

           'type': 'ir.actions.act_window',

           'res_model': 'account.payment',

           'view_mode': 'tree,form',

           'view_type': 'form',

           'view_id': False,

           'context': False,

           }
```
  </details>
- **SLS - Credit Limit Approval** (`server_action_2503_sls_credit_limit_approval`, type `object_write`)
  - Function: Sets Credit Limit Approved to 'Yes' on the sales order; step of 'SLS - Credit Limit Approval - Main'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_credit_limit_approved`
  - Used by: `server action BugFix-Sales.server_action_1435_sls_credit_limit_approval_main`
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
- **SLS - Credit Limit Approval - Confirm** (`server_action_2505_sls_credit_limit_approval_confirm`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order confirming the credit limit approval; step of 'SLS - Credit Limit Approval - Main'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1435_sls_credit_limit_approval_main`
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
- **SLS - Credit Limit Approval - Main** (`server_action_1435_sls_credit_limit_approval_main`, type `multi`)
  - Function: Multi-step action on sales orders that runs two child actions in order: 'SLS - Credit Limit Approval' then its confirm step. Triggered by the Approve Credit Limit button and set as the action of the credit-limit approval rule.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2503_sls_credit_limit_approval`, `server action BugFix-Sales.server_action_2505_sls_credit_limit_approval_confirm`
  - Used by: `approval rule BugFix-Sales.ar_final_sales_order_sls_credit_limit_approval_sales_credit_limit_app`, `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Item Over Margin Details** (`server_action_1517_sls_item_over_margin_details`, type `code`)
  - Function: Button action: when the order exceeds margin, raises an error listing each over-margin line with base price, discounts, commission, cost, net margin and the company's Minimum Sales Margin %.
  - Depends on: `model sale.order` (sale), `sale.order.company_id` (sale), `sale.order.order_line` (sale), `sale.order.x_studio_margin_exceed`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
  <details><summary>code (102 lines)</summary>

```python
# bugfix_sales:config-cutover-v22
if record.x_studio_margin_exceed == True:

  base_price = 0  

  discounts = 0

  commission = 0

  cost = 0

  value_1 = 0

  value_2 = 0

  item_code = ""

  message = ""

  title = "Insufficient margin. You need approval to proceed."

  

  message += title + '\n' + '\n' + '\n'

  

  min_magin = record.company_id

  

  for margin_lines in record.order_line:

    if margin_lines.x_studio_margin_exceed == True:

      item_code = margin_lines.product_id.name

      base_price = margin_lines.price_unit

      discounts = (margin_lines.price_unit * margin_lines.product_uom_qty) - margin_lines.price_subtotal

      commission = margin_lines.price_subtotal * (margin_lines.x_studio_commission/100)

      cost = margin_lines.product_id.standard_price

      

      if margin_lines.product_uom_qty != 0.00:

        value_1 = ((margin_lines.price_subtotal/margin_lines.product_uom_qty)-(margin_lines.price_subtotal*(margin_lines.x_studio_commission/100))-margin_lines.product_id.standard_price)

        value_2 = (margin_lines.price_subtotal/margin_lines.product_uom_qty)-(margin_lines.price_subtotal*(margin_lines.x_studio_commission/100))

        

      if value_2 > 0.00:

        net_margin = (value_1/value_2)*100

      else:

        net_margin = 0

        

        

      message +=  ( 'Item Code: ' + str(item_code) + '\n' +

                    'Base Price: ' + str(base_price) + '\n' +

                    'Discounts: ' + str(discounts) + '\n' +

                    'Other Charges (Commission): ' + str(commission) + '\n' +

                    'Cost: ' + str(cost) + '\n' +

                    'Net Margin: ' + str(net_margin) + '\n' + 

                    'Min. Sales Margin %: ' + str(min_magin.x_studio_minimum_sales_margin_) + '\n' + '\n')

                    

  raise UserError(message)

  

  

"""        

  action = {

            'type': 'ir.actions.client',

            'tag': 'display_notification',

            'params': {'title': title,'message': message,'sticky': True,}

            } 

"""
```
  </details>
- **SLS - Margin Approval** (`server_action_2495_sls_margin_approval`, type `object_write`)
  - Function: Sets Margin Approved to 'Yes' on the sales order; step of 'SLS - Margin Approval - Main'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_margin_approved`
  - Used by: `server action BugFix-Sales.server_action_1515_sls_margin_approval_main`
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
- **SLS - Margin Approval - Confirm** (`server_action_2497_sls_margin_approval_confirm`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order confirming the margin approval; step of 'SLS - Margin Approval - Main'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1515_sls_margin_approval_main`
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
- **SLS - Margin Approval - Main** (`server_action_1515_sls_margin_approval_main`, type `multi`)
  - Function: Multi-step action on sales orders that runs the 'SLS - Margin Approval' child action followed by its confirm step. Used by the Approve Insufficient Margin button and the margin approval rule.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2495_sls_margin_approval`, `server action BugFix-Sales.server_action_2497_sls_margin_approval_confirm`
  - Used by: `approval rule BugFix-Sales.ar_final_sales_order_sls_margin_approval_sales_margin_approver_27`, `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Margin Approval Request  Sent** (`server_action_1509_sls_margin_approval_request_sent`, type `object_write`)
  - Function: Sets Margin Approval Request Sent to 'Yes' on the sales order; step of 'SLS - Request Margin Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_margin_approval_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1513_sls_request_margin_approval`
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
- **SLS - Margin Request Approval - Notify User** (`server_action_1511_sls_margin_request_approval_notify_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order to notify the approver of a margin approval request; step of 'SLS - Request Margin Approval'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1513_sls_request_margin_approval`
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
- **SLS - Over Commission Approval** (`server_action_2499_sls_over_commission_approval`, type `object_write`)
  - Function: Sets Over Commission Approved to 'Yes' on the sales order; step of 'SLS - Over Commission Approval - Main'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_over_commission_approved`
  - Used by: `server action BugFix-Sales.server_action_1505_sls_over_commission_approval_main`
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
- **SLS - Over Commission Approval - Confirm** (`server_action_2501_sls_over_commission_approval_confirm`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order confirming the over-commission approval; step of 'SLS - Over Commission Approval - Main'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1505_sls_over_commission_approval_main`
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
- **SLS - Over Commission Approval - Main** (`server_action_1505_sls_over_commission_approval_main`, type `multi`)
  - Function: Multi-step action on sales orders that runs the 'SLS - Over Commission Approval' child action followed by its confirm step. Used by the Approve Over Commission button and the over-commission approval rule.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2499_sls_over_commission_approval`, `server action BugFix-Sales.server_action_2501_sls_over_commission_approval_confirm`
  - Used by: `approval rule BugFix-Sales.ar_final_sales_order_sls_over_commission_approval_sales_over_commissi`, `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Over Commission Approval Request  Sent** (`server_action_1499_sls_over_commission_approval_request_sent`, type `object_write`)
  - Function: Sets Over Commission Approval Request Sent to 'Yes' on the sales order; step of 'SLS - Request Over Commission Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_over_comm_approval_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1503_sls_request_over_commission_approval`
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
- **SLS - Over Commission Request Approval - Notify User** (`server_action_1501_sls_over_commission_request_approval_notify_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order to notify the approver of an over-commission approval request; step of 'SLS - Request Over Commission Approval'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1503_sls_request_over_commission_approval`
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
- **SLS - Overdue Approval** (`server_action_1478_sls_overdue_approval`, type `multi`)
  - Function: Multi-step action on sales orders that runs two child actions: notify the requesting user and finalise the overdue approval. Used by the Approve Overdue button and by the sales and credit-note overdue approval rules.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2458_sls_request_overdue_approval_final01`, `server action BugFix-Sales.server_action_2460_sls_overdue_request_approval_notify_user_01`
  - Used by: `approval rule BugFix-Accounting.ar_relaxed_journal_entry_sls_overdue_approval_sales_credit_note_approve` (BugFix-Accounting), `approval rule BugFix-Sales.ar_final_sales_order_sls_overdue_approval_sales_overdue_approver_22`, `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Overdue Approval Request  Sent** (`server_action_1472_sls_overdue_approval_request_sent`, type `object_write`)
  - Function: Sets Overdue Request Sent to 'Yes' on the sales order; step of 'SLS - Request Overdue Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_overdue_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1476_sls_request_overdue_approval`
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
- **SLS - Overdue Approval Request  Sent - Validate** (`server_action_1841_sls_overdue_approval_request_sent_validate`, type `code`)
  - Function: When Overdue Request Sent is set, raises an error if the order has no lines; step of 'SLS - Request Overdue Approval'.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `sale.order.x_studio_overdue_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1476_sls_request_overdue_approval`
  <details><summary>code (7 lines)</summary>

```python
if record.x_studio_overdue_request_sent == True:

  null_so_lines = env['sale.order.line'].search([('order_id', '=', record.id)])

  if not null_so_lines:

   raise UserError("Valid SO lines should be existed to proceed!")
```
  </details>
- **SLS - Overdue Request Approval - Notify User** (`server_action_1474_sls_overdue_request_approval_notify_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order to notify the approver of an overdue-balance approval request; step of 'SLS - Request Overdue Approval'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1476_sls_request_overdue_approval`
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
- **SLS - Overdue Request Approval - Notify User - 01** (`server_action_2460_sls_overdue_request_approval_notify_user_01`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order as a notification during overdue approval; step of 'SLS - Overdue Approval'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1478_sls_overdue_approval`
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
- **SLS - Pass Customer PM to SO** (`server_action_1430_sls_pass_customer_pm_to_so`, type `code`)
  - Function: When a customer is set on an order, picks the current company's pricelist matching the customer's payment method and group type, and copies the customer's payment method to the order.
  - Depends on: `model product.pricelist` (product), `model res.company` (base), `model sale.order` (sale), `sale.order.partner_id` (sale), `sale.order.x_studio_order_payment_method`
  - Used by: `automation BugFix-Sales.base_automation_79_sls_pass_customer_pm_to_so`
  <details><summary>code (9 lines)</summary>

```python
if record.partner_id.id  != False:
  
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  pricelist = env['product.pricelist'].search([('x_studio_order_payment_method', '=', record.partner_id.x_studio_payment_method),('x_studio_group_type', '=', record.partner_id.x_studio_customer_group.x_studio_group_type),('company_id', '=', company.id)], limit=1)
  if pricelist:
    record['pricelist_id'] = pricelist.id
record['x_studio_order_payment_method'] = record.partner_id.x_studio_payment_method
```
  </details>
- **SLS - Request Approval - Notify User** (`server_action_1462_sls_request_approval_notify_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order to notify the approver of a credit limit approval request; step of 'SLS - Request Credit Limit Approval'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1458_sls_request_credit_limit_approval`
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
- **SLS - Request Approval Sent** (`server_action_1460_sls_request_approval_sent`, type `object_write`)
  - Function: Sets Approval Request Sent to 'Yes' on the sales order; step of 'SLS - Request Credit Limit Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_approval_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1458_sls_request_credit_limit_approval`
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
- **SLS - Request Approval Sent - Validate** (`server_action_1843_sls_request_approval_sent_validate`, type `code`)
  - Function: When Approval Request Sent is set, raises an error if the order has no lines; step of 'SLS - Request Credit Limit Approval'.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `sale.order.x_studio_approval_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1458_sls_request_credit_limit_approval`
  <details><summary>code (7 lines)</summary>

```python
if record.x_studio_approval_request_sent == True:

  null_so_lines = env['sale.order.line'].search([('order_id', '=', record.id)])

  if not null_so_lines:

   raise UserError("Valid SO lines should be existed to proceed!")
```
  </details>
- **SLS - Request Bank Guarantee Approval** (`server_action_1485_sls_request_bank_guarantee_approval`, type `multi`)
  - Function: Multi-step action behind the Request Bank Guarantee Approval button: notifies the approver, marks the bank-guarantee request as sent and validates the request flag via three child actions.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_1481_sls_request_bank_guarantee_approval_sent`, `server action BugFix-Sales.server_action_1483_sls_request_bank_guarantee_approval_notify_user`, `server action BugFix-Sales.server_action_1845_sls_request_bank_guarantee_approval_sent_validate`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Request Bank Guarantee Approval - Notify User** (`server_action_1483_sls_request_bank_guarantee_approval_notify_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order to notify the approver of a bank guarantee approval request; step of 'SLS - Request Bank Guarantee Approval'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1485_sls_request_bank_guarantee_approval`
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
- **SLS - Request Bank Guarantee Approval Sent** (`server_action_1481_sls_request_bank_guarantee_approval_sent`, type `object_write`)
  - Function: Sets Bank Guarantee Request Sent to 'Yes' on the sales order; step of 'SLS - Request Bank Guarantee Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_bank_guarantee_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1485_sls_request_bank_guarantee_approval`
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
- **SLS - Request Bank Guarantee Approval Sent - Validate** (`server_action_1845_sls_request_bank_guarantee_approval_sent_validate`, type `code`)
  - Function: When Bank Guarantee Request Sent is set, raises an error if the order has no lines; step of 'SLS - Request Bank Guarantee Approval'.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `sale.order.x_studio_bank_guarantee_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1485_sls_request_bank_guarantee_approval`
  <details><summary>code (7 lines)</summary>

```python
if record.x_studio_bank_guarantee_request_sent == True:

  null_so_lines = env['sale.order.line'].search([('order_id', '=', record.id)])

  if not null_so_lines:

   raise UserError("Valid SO lines should be existed to proceed!")
```
  </details>
- **SLS - Request Credit Limit Approval** (`server_action_1458_sls_request_credit_limit_approval`, type `multi`)
  - Function: Multi-step action behind the Request Credit Limit Approval button: runs child actions that notify the approver, mark the approval request as sent and validate the sent flag.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_1460_sls_request_approval_sent`, `server action BugFix-Sales.server_action_1462_sls_request_approval_notify_user`, `server action BugFix-Sales.server_action_1843_sls_request_approval_sent_validate`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Request Margin Approval** (`server_action_1513_sls_request_margin_approval`, type `multi`)
  - Function: Multi-step action behind the Request Insufficient Margin Approval button: marks the margin approval request as sent and notifies the approver via two child actions.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_1509_sls_margin_approval_request_sent`, `server action BugFix-Sales.server_action_1511_sls_margin_request_approval_notify_user`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Request Over Commission Approval** (`server_action_1503_sls_request_over_commission_approval`, type `multi`)
  - Function: Multi-step action behind the Request Over Commission Approval button: marks the over-commission approval request as sent and notifies the approver via two child actions.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_1499_sls_over_commission_approval_request_sent`, `server action BugFix-Sales.server_action_1501_sls_over_commission_request_approval_notify_user`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Request Overdue Approval** (`server_action_1476_sls_request_overdue_approval`, type `multi`)
  - Function: Multi-step action behind the Request Overdue Approval button: marks the overdue approval request as sent, validates that flag and notifies the approver via three child actions.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_1472_sls_overdue_approval_request_sent`, `server action BugFix-Sales.server_action_1474_sls_overdue_request_approval_notify_user`, `server action BugFix-Sales.server_action_1841_sls_overdue_approval_request_sent_validate`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Request Overdue Approval - Final01** (`server_action_2458_sls_request_overdue_approval_final01`, type `object_write`)
  - Function: Sets Overdue Approved to 'Yes' on the sales order; step of 'SLS - Overdue Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_overdue_approved`
  - Used by: `server action BugFix-Sales.server_action_1478_sls_overdue_approval`
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
- **SLS - Request Temporary Credit Approval** (`server_action_1468_sls_request_temporary_credit_approval`, type `multi`)
  - Function: Multi-step action behind the Request Temporary Credit Approval button: notifies the approver and marks the temporary-credit approval request as sent via two child actions.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_1464_sls_temporary_credit_approval_sent`, `server action BugFix-Sales.server_action_1466_sls_request_temporary_credit_approval_notify_user`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Request Temporary Credit Approval - Notify User** (`server_action_1466_sls_request_temporary_credit_approval_notify_user`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order to notify the approver of a temporary credit approval request; step of 'SLS - Request Temporary Credit Approval'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1468_sls_request_temporary_credit_approval`
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
- **SLS - Send Bank Guarantee Notification** (`server_action_2515_sls_send_bank_guarantee_notification`, type `code`)
  - Function: For non-General customers without a mandatory bank guarantee, posts a chatter note and sets BG Sent when the guarantee has expired or the customer's balance plus this sale exceeds the guarantee amount.
  - Depends on: `model sale.order` (sale), `sale.order.amount_total` (sale), `sale.order.partner_id` (sale), `sale.order.partner_invoice_id` (sale), `sale.order.x_studio_bg_sent`
  - Used by: `server action BugFix-Sales.server_action_1850_sls_send_bank_guarantee_notification_main`
  <details><summary>code (19 lines)</summary>

```python
if record.partner_id.customer_rank > 0:

  if record.partner_id.x_studio_customer_group.x_studio_group_type != 'General':

    if record.partner_id.x_studio_mandatory_bank_guarantee == False:

      if record.partner_id.x_studio_expiry_date and record.partner_id.x_studio_expiry_date < datetime.date.today():

        records.message_post(body="Customer's bank guarantee is expired." + "\n" + "Bank guaranty expiry date: " + str(record.partner_id.x_studio_expiry_date))

        record['x_studio_bg_sent'] = True

      else:

        if record.partner_id.x_studio_bank_guarantee_amount < (record.partner_invoice_id.credit + record.amount_total):

          records.message_post(body="Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee amount: " + str(record.partner_id.x_studio_bank_guarantee_amount) + "\n" + "Current Balance: " + str(record.partner_invoice_id.credit) + '\n' + "This Sale: " + str(record.amount_total) + "\n" + "New balance: " + str(record.partner_invoice_id.credit + record.amount_total))

          record['x_studio_bg_sent'] = True
```
  </details>
- **SLS - Send Bank Guarantee Notification - Confirm** (`server_action_2516_sls_send_bank_guarantee_notification_confirm`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order confirming the bank guarantee notification; step of 'SLS - Send Bank Guarantee Notification - Main'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1850_sls_send_bank_guarantee_notification_main`
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
- **SLS - Send Bank Guarantee Notification - Main** (`server_action_1850_sls_send_bank_guarantee_notification_main`, type `multi`)
  - Function: Multi-step action behind the Send Bank Guarantee Validity Notification button: runs the 'Send Bank Guarantee Notification' child action followed by its confirm step.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2515_sls_send_bank_guarantee_notification`, `server action BugFix-Sales.server_action_2516_sls_send_bank_guarantee_notification_confirm`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - TEST** (`server_action_1507_sls_test`, type `code`)
  - Function: Test action that only shows a sticky notification 'Calculate Assessable Value' with no computed value. No business effect.
  - Depends on: `model sale.order` (sale)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (8 lines)</summary>

```python
title = "Calculate Assessable Value"
message = "Assessable Value: "
      
action = {
          'type': 'ir.actions.client',
          'tag': 'display_notification',
          'params': {'title': title,'message': message,'sticky': True,}
          }
```
  </details>
- **SLS - Temporary Credit Approval** (`server_action_2511_sls_temporary_credit_approval`, type `object_write`)
  - Function: Sets Temporary Credit Approved to 'Yes' on the sales order; step of 'SLS - Temporary Credit Approval - Main'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_temporary_credit_approved`
  - Used by: `server action BugFix-Sales.server_action_1470_sls_temporary_credit_approval_main`
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
- **SLS - Temporary Credit Approval - Confirm** (`server_action_2513_sls_temporary_credit_approval_confirm`, type `next_activity`)
  - Function: Schedules a follow-up activity on the sales order confirming the temporary credit approval; step of 'SLS - Temporary Credit Approval - Main'.
  - Depends on: `model sale.order` (sale)
  - Used by: `server action BugFix-Sales.server_action_1470_sls_temporary_credit_approval_main`
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
- **SLS - Temporary Credit Approval - Main** (`server_action_1470_sls_temporary_credit_approval_main`, type `multi`)
  - Function: Multi-step action on sales orders that runs the 'SLS - Temporary Credit Approval' child action followed by its confirm step. Used by the Approve Temporary Credit button and the temporary-credit approval rule.
  - Depends on: `model sale.order` (sale), `server action BugFix-Sales.server_action_2511_sls_temporary_credit_approval`, `server action BugFix-Sales.server_action_2513_sls_temporary_credit_approval_confirm`
  - Used by: `approval rule BugFix-Sales.ar_final_sales_order_sls_temporary_credit_approval_sales_temporary_cr`, `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
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
- **SLS - Temporary Credit Approval Sent** (`server_action_1464_sls_temporary_credit_approval_sent`, type `object_write`)
  - Function: Sets Temporary Credit Approval Request Sent to 'Yes' on the sales order; step of 'SLS - Request Temporary Credit Approval'.
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_tem_credit_approval_request_sent`
  - Used by: `server action BugFix-Sales.server_action_1468_sls_request_temporary_credit_approval`
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
- **SLS - Validate Bank Guarantee in SO Confirm** (`server_action_1783_sls_validate_bank_guarantee_in_so_confirm`, type `code`)
  - Function: On Locked orders of non-General customers: if the bank guarantee is mandatory, blocks with an error when it is expired or exceeded by balance plus this sale; otherwise only posts a chatter warning.
  - Depends on: `model sale.order` (sale), `sale.order.amount_total` (sale), `sale.order.partner_id` (sale), `sale.order.partner_invoice_id` (sale), `sale.order.state` (sale)
  - Used by: `automation BugFix-Sales.base_automation_147_sls_validate_bank_guarantee_in_so_confirm`
  <details><summary>code (40 lines)</summary>

```python

if record.partner_id.customer_rank > 0:

  if record.state == 'done':

    if record.partner_id.x_studio_customer_group.x_studio_group_type != 'General':

      if record.partner_id.x_studio_mandatory_bank_guarantee == True:

        if record.partner_id.x_studio_expiry_date and record.partner_id.x_studio_expiry_date < datetime.date.today():

          #raise UserError("Customer's bank guarantee is expired.")

          raise UserError("Customer's bank guarantee is expired." + "\n" + "Bank guaranty expiry date: " + str(record.partner_id.x_studio_expiry_date))

          

        else:

          #if record.partner_id.x_studio_mandatory_bank_guarantee < (record.partner_invoice_id.credit + record.amount_total):

          if record.partner_id.x_studio_bank_guarantee_amount < (record.partner_invoice_id.credit + record.amount_total):

            #raise UserError("Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee limit: " + "\n" + str(record.partner_id.x_studio_mandatory_bank_guarantee) + "\n" + "New balance: " + "\n" + str((record.partner_invoice_id.credit + record.amount_total)))

            raise UserError("Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee amount: " + str(record.partner_id.x_studio_bank_guarantee_amount) + "\n" + "Current Balance: " + str(record.partner_invoice_id.credit) + '\n' + "This Sale: " + str(record.amount_total) + "\n" + "New balance: " + str(record.partner_invoice_id.credit + record.amount_total))

      else:

        if record.partner_id.x_studio_expiry_date and record.partner_id.x_studio_expiry_date < datetime.date.today():

          records.message_post(body="Customer's bank guarantee is expired." + "\n" + "Bank guaranty expiry date: " + str(record.partner_id.x_studio_expiry_date))

        else:

          if record.partner_id.x_studio_bank_guarantee_amount < (record.partner_invoice_id.credit + record.amount_total):

            #records.message_post(body="Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee limit: " + "\n" + str(record.partner_id.x_studio_mandatory_bank_guarantee) + "\n" + "New balance: " + "\n" + str((record.partner_invoice_id.credit + record.amount_total)))

            records.message_post(body="Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee amount: " + str(record.partner_id.x_studio_bank_guarantee_amount) + "\n" + "Current Balance: " + str(record.partner_invoice_id.credit) + '\n' + "This Sale: " + str(record.amount_total) + "\n" + "New balance: " + str(record.partner_invoice_id.credit + record.amount_total))
```
  </details>
- **SLS - Validate Bank Guarantee in SO Confirm** (`server_action_1773_sls_validate_bank_guarantee_in_so_confirm`, type `code`)
  - Function: Older version of the bank-guarantee check on Locked orders; compares the boolean Mandatory Bank Guarantee against amounts and errors if Expiry Date is empty, so its logic is faulty. Not referenced by any automation in this repo.
  - Depends on: `model sale.order` (sale), `sale.order.amount_total` (sale), `sale.order.partner_id` (sale), `sale.order.partner_invoice_id` (sale), `sale.order.state` (sale)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (14 lines)</summary>

```python
if record.state == 'done':
  if record.partner_id.x_studio_customer_group.x_studio_group_type != 'General':
    if record.partner_id.x_studio_mandatory_bank_guarantee == True:
      if record.partner_id.x_studio_expiry_date < datetime.date.today():
        raise UserError("Customer's bank guarantee is expired.")
      else:
        if record.partner_id.x_studio_mandatory_bank_guarantee < (record.partner_invoice_id.credit + record.amount_total):
          raise UserError("Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee limit: " + "\n" + str(record.partner_id.x_studio_mandatory_bank_guarantee) + "\n" + "New balance: " + "\n" + str((record.partner_invoice_id.credit + record.amount_total)))
    else:
      if record.partner_id.x_studio_expiry_date < datetime.date.today():
        records.message_post(body="Customer's bank guarantee is expired." + "\n" + "Bank guaranty expiry date: " + str(record.partner_id.x_studio_expiry_date))
      else:
        if record.partner_id.x_studio_mandatory_bank_guarantee < (record.partner_invoice_id.credit + record.amount_total):
          records.message_post(body="Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee limit: " + "\n" + str(record.partner_id.x_studio_mandatory_bank_guarantee) + "\n" + "New balance: " + "\n" + str((record.partner_invoice_id.credit + record.amount_total)))
```
  </details>
- **SLS - Validate Order Payment Type in SO** (`server_action_1434_sls_validate_order_payment_type_in_so`, type `code`)
  - Function: Raises an error if a cash customer's order is switched to Credit payment method ('Cash Sales Orders can not be Converted in to Credit Sales Orders').
  - Depends on: `model sale.order` (sale), `sale.order.x_studio_customer_payment_method`, `sale.order.x_studio_order_payment_method`
  - Used by: `automation BugFix-Sales.base_automation_80_sls_validate_order_payment_type_in_so`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_customer_payment_method == 'Cash' and record.x_studio_order_payment_method == 'Credit':
  raise UserError('Cash Sales Orders can not be Converted in to Credit Sales Orders.')
```
  </details>
- **SLS - Validate SOs without Lines** (`server_action_1840_sls_validate_sos_without_lines`, type `code`)
  - Function: Raises 'Valid SO lines should be existed to proceed!' when a non-draft order has no lines. Not referenced by any automation in this repo.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `sale.order.state` (sale)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
if record.state != 'draft':
  null_so_lines = env['sale.order.line'].search([('order_id', '=', record.id)])
  if not null_so_lines:
   raise UserError("Valid SO lines should be existed to proceed!")
```
  </details>
- **SLS - Validate Sales** (`server_action_2337_sls_validate_sales`, type `code`)
  - Function: 'Validate Sales Lines' button action: when Clear Free Items is set, deletes the order's reward (free) lines and clears the Clear Free Items flag on the remaining lines.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `sale.order.x_studio_clear_free_items`
  - Used by: `view BugFix-Accounting.ported_odoo_studio_sale_ord_acct` (BugFix-Accounting)
  <details><summary>code (7 lines)</summary>

```python
if record.id:
  if record.x_studio_clear_free_items == True:
    free_items_delete = env['sale.order.line'].search([('order_id', '=', record.id),('is_reward_line', '=', True)]).unlink()
    free_items_update = env['sale.order.line'].search([('order_id', '=', record.id),('x_studio_clear_free_items', '=', True)])
    if free_items_update:
      for update in free_items_update:
        update.write({'x_studio_clear_free_items':False})
```
  </details>
- **SLS - View Bank Guarantee Validation** (`server_action_1849_sls_view_bank_guarantee_validation`, type `code`)
  - Function: Button check: for non-General customers with a mandatory bank guarantee, raises an error if the guarantee is expired or the customer's balance plus this sale exceeds the guarantee amount.
  - Depends on: `model sale.order` (sale), `sale.order.amount_total` (sale), `sale.order.partner_id` (sale), `sale.order.partner_invoice_id` (sale)
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
  <details><summary>code (17 lines)</summary>

```python
if record.partner_id.customer_rank > 0:

  if record.partner_id.x_studio_customer_group.x_studio_group_type != 'General':

    if record.partner_id.x_studio_mandatory_bank_guarantee == True:

      if record.partner_id.x_studio_expiry_date and record.partner_id.x_studio_expiry_date < datetime.date.today():

        raise UserError("Customer's bank guarantee is expired." + "\n" + "Bank guaranty expiry date: " + str(record.partner_id.x_studio_expiry_date))

          

      else:

        if record.partner_id.x_studio_bank_guarantee_amount < (record.partner_invoice_id.credit + record.amount_total):

          raise UserError("Customer's balance exceeds the bank guarantee amount." + "\n" + "Bank guarantee amount: " + str(record.partner_id.x_studio_bank_guarantee_amount) + "\n" + "Current Balance: " + str(record.partner_invoice_id.credit) + '\n' + "This Sale: " + str(record.amount_total) + "\n" + "New balance: " + str(record.partner_invoice_id.credit + record.amount_total))
```
  </details>
- **SLS - View Credit Limit Validation** (`server_action_1853_sls_view_credit_limit_validation`, type `code`)
  - Function: Button check for Credit orders: raises an error showing credit limit, receivable, this sale and overrun when the customer's receivable plus this sale exceeds the credit limit.
  - Depends on: `model sale.order` (sale), `sale.order.amount_total` (sale), `sale.order.partner_id` (sale), `sale.order.partner_invoice_id` (sale), `sale.order.x_studio_order_payment_method`
  - Used by: `view BugFix-Sales.ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3`
  <details><summary>code (27 lines)</summary>

```python
if record.partner_id.customer_rank > 0:

  if record.partner_id.id:

    if record.x_studio_order_payment_method == 'Credit':

      if (record.partner_invoice_id.credit + record.amount_total) > record.partner_invoice_id.credit_limit:

        #raise UserError("Customer's credit limit is exceeded." + "\n" + "Customer credit limit: " + str(record.partner_invoice_id.credit_limit) + "\n" + "Cust. Total Receivable: " + str(record.partner_invoice_id.credit) + "\n" + "Current Tot. Amount: " + str(record.amount_total) + "\n" + "Over Credit Amount: " + str((record.partner_invoice_id.credit + record.amount_total) - record.partner_invoice_id.credit_limit))

        #raise UserError("Customer's credit limit is exceeded." + "\n" + "Customer credit limit: " + str(record.partner_invoice_id.credit_limit) + "\n" + "Cust. Total Receivable: " + str(record.partner_invoice_id.credit) + "\n" + "This Sale: " + str(record.amount_total) + "\n" + "Total receivable + This sale : " + str((record.partner_invoice_id.credit + record.amount_total)) + "\n" + "Over Credit Amount: " + str((record.partner_invoice_id.credit + record.amount_total) - record.partner_invoice_id.credit_limit))

        raise UserError(

            "Customer's credit limit is exceeded.\n\n"

            + "Customer credit limit: {:,.2f}\n".format(record.partner_invoice_id.credit_limit)

            + "Cust. Total Receivable: {:,.2f}\n".format(record.partner_invoice_id.credit)

            + "This Sale: {:,.2f}\n".format(record.amount_total)

            + "Total receivable + This sale: {:,.2f}\n".format(record.partner_invoice_id.credit + record.amount_total)

            + "Over Credit Amount: {:,.2f}".format((record.partner_invoice_id.credit + record.amount_total) - record.partner_invoice_id.credit_limit)

)
```
  </details>
- **Update Analytic Tag Parameters - Sales Order - Customer** (`server_action_2414_update_analytic_tag_parameters_sales_order_customer`, type `code`)
  - Function: Sets the order's Account Mandatory flag from the Partner Mandatory setting of the analytic distribution model for the order's customer (False if none).
  - Depends on: `model account.analytic.distribution.model` (analytic), `model sale.order` (sale), `sale.order.partner_id` (sale), `sale.order.x_studio_account_mandatory`
  - Used by: `automation BugFix-Sales.base_automation_234_update_analytic_tag_parameters_sales_order_customer`
  <details><summary>code (6 lines)</summary>

```python
if record.partner_id:
  tag_rule= env['account.analytic.distribution.model'].search([('partner_id', '=', record.partner_id.id)],limit=1)
  if tag_rule:
    record['x_studio_account_mandatory'] = tag_rule.x_studio_partner_mandatory
  else:
    record['x_studio_account_mandatory'] = False
```
  </details>
- **Update Analytic Tag Parameters - Sales Order - User** (`server_action_2415_update_analytic_tag_parameters_sales_order_user`, type `code`)
  - Function: Sets the order's Account Mandatory flag from the User Mandatory setting of the analytic distribution model whose partner's salesperson is the order creator (False if none); writes only on change.
  - Depends on: `model account.analytic.distribution.model` (analytic), `model sale.order` (sale), `sale.order.x_studio_account_mandatory`
  - Used by: `automation BugFix-Sales.base_automation_235_update_analytic_tag_parameters_sales_order_user`
  <details><summary>code (7 lines)</summary>

```python
# fix_repair:idempotent-v1
if record.create_uid:
  tag_rule = env['account.analytic.distribution.model'].sudo().search(
    [('partner_id.user_id', '=', record.create_uid.id)], limit=1)
  target = tag_rule.x_studio_user_mandatory if tag_rule else False
  if record.x_studio_account_mandatory != target:
    record.write({'x_studio_account_mandatory': target})
```
  </details>
**Automations (17):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN-Project Sales Order Seq.No | `base_automation_257_jin_project_sales_order_seq_no` |  | When a record is created or updated on Sales Order, runs _Project Sales Order Seq.No_. | `model sale.order` (sale)<br>`sale.order.create_date` (sale)<br>`server action BugFix-Sales.server_action_2573_project_sales_order_seq_no` |  |
| JIN-Project Sales Order Seq.No (Maintain Separate Nos for Project SOs On Create) | `base_automation_258_jin_project_sales_order_seq_no_maintain_separate_nos_for_pro` |  | When a watched field changes in the form on Sales Order, runs _Project Sales Order Seq.No - 2_. | `model sale.order` (sale)<br>`sale.order.x_studio_quotation_type`<br>`server action BugFix-Sales.server_action_2574_project_sales_order_seq_no_2` |  |
| JIN-Project Sales Order Seq.No (Maintain Separate Nos for Project SOs On Update) | `base_automation_259_jin_project_sales_order_seq_no_maintain_separate_nos_for_pro` | archived | When a record is created or updated on Sales Order, runs nothing (no action linked). **Archived — does not run.** | `model sale.order` (sale) |  |
| PROJ - Apply Project Price List | `base_automation_341_proj_apply_project_price_list` |  | When a watched field changes in the form on Sales Order, runs _Execute Code_. | `model sale.order` (sale)<br>`sale.order.x_studio_quotation_type`<br>`server action BugFix-Sales.server_action_2896_proj_apply_project_price_list` |  |
| PROJ - Validate Start date and End date for Project SOs | `base_automation_260_proj_validate_start_date_and_end_date_for_project_sos` |  | When a watched field changes in the form on Sales Order and `[["task_id","!=",False]]`, runs _Execute Code_. | `model sale.order` (sale)<br>`sale.order.task_id` (industry_fsm_sale)<br>`sale.order.x_studio_project_end_date`<br>`sale.order.x_studio_project_start_date`<br>`server action BugFix-Sales.server_action_2576_proj_validate_start_date_and_end_date_for_project_sos` |  |
| RR - Auto Generate Quotation Type for Project SOs | `base_automation_186_rr_auto_generate_quotation_type_for_project_sos` |  | When a record is created or updated on Sales Order and `[["task_id","!=",False]]`, runs _Execute Code_. | `model sale.order` (sale)<br>`sale.order.task_id` (industry_fsm_sale)<br>`server action BugFix-Sales.server_action_2114_rr_auto_generate_quotation_type_for_project_sos` |  |
| RR - Auto Generate Quotation Type for Project SOs - 2 | `base_automation_187_rr_auto_generate_quotation_type_for_project_sos_2` |  | When a watched field changes in the form on Sales Order and `[["task_id","!=",False]]`, runs _Execute Code_. | `model sale.order` (sale)<br>`sale.order.task_id` (industry_fsm_sale)<br>`server action BugFix-Sales.server_action_2117_rr_auto_generate_quotation_type_for_project_sos_2` |  |
| RR - Auto Generate Quotation Type for Repair SOs | `base_automation_176_rr_auto_generate_quotation_type_for_repair_sos` |  | When a record is created or updated on Sales Order, runs _Execute Code_. | `model sale.order` (sale)<br>`sale.order.create_date` (sale)<br>`server action BugFix-Sales.server_action_1995_rr_auto_generate_quotation_type_for_repair_sos` |  |
| RR - Track Lock Status | `base_automation_202_rr_track_lock_status` |  | When a record is created or updated on Sales Order, runs _Execute Code_. | `model sale.order` (sale)<br>`server action BugFix-Sales.server_action_2250_rr_track_lock_status` |  |
| RR - Track Lock Status - 2 | `base_automation_203_rr_track_lock_status_2` |  | When a record is created or updated on Sales Order, runs _Execute Code_. | `model sale.order` (sale)<br>`server action BugFix-Sales.server_action_2251_rr_track_lock_status_2` |  |
| RR - Track Lock Status - 4 | `base_automation_205_rr_track_lock_status_4` | archived | When a record is updated on Sales Order and `['&', '&', '&', ('state', '=', 'sale'), ('x_studio_locked', '=', True), ('x_studio_quotation_type', '=', 'Repair'), ('x_studio_unlocked', '=', True)]`, runs nothing (no action linked). **Archived — does not run.** | `model sale.order` (sale)<br>`sale.order.state` (sale)<br>`sale.order.x_studio_locked`<br>`sale.order.x_studio_quotation_type`<br>`sale.order.x_studio_unlocked` |  |
| SLS - Pass Customer PM to SO | `base_automation_79_sls_pass_customer_pm_to_so` |  | When a watched field changes in the form on Sales Order and `[]`, runs _SLS - Pass Customer PM to SO_. | `model sale.order` (sale)<br>`sale.order.partner_id` (sale)<br>`server action BugFix-Sales.server_action_1430_sls_pass_customer_pm_to_so` |  |
| SLS - Validate Bank Guarantee in SO Confirm | `base_automation_147_sls_validate_bank_guarantee_in_so_confirm` | archived | When a record is updated on Sales Order, runs _SLS - Validate Bank Guarantee in SO Confirm_. **Archived — does not run.** | `model sale.order` (sale)<br>`server action BugFix-Sales.server_action_1783_sls_validate_bank_guarantee_in_so_confirm` |  |
| SLS - Validate Order Payment Type in SO | `base_automation_80_sls_validate_order_payment_type_in_so` |  | When a watched field changes in the form on Sales Order, runs _SLS - Validate Order Payment Type in SO_. | `model sale.order` (sale)<br>`sale.order.x_studio_order_payment_method`<br>`server action BugFix-Sales.server_action_1434_sls_validate_order_payment_type_in_so` |  |
| SLS - Validate SOs without Lines | `base_automation_169_sls_validate_sos_without_lines` | archived | When a record is created or updated on Sales Order, runs nothing (no action linked). **Archived — does not run.** | `model sale.order` (sale) |  |
| Update Analytic Tag Parameters - Sales Order - Customer | `base_automation_234_update_analytic_tag_parameters_sales_order_customer` |  | When a watched field changes in the form on Sales Order, runs _Update Analytic Tag Parameters - Sales Order - Customer_. | `model sale.order` (sale)<br>`sale.order.partner_id` (sale)<br>`server action BugFix-Sales.server_action_2414_update_analytic_tag_parameters_sales_order_customer` |  |
| Update Analytic Tag Parameters - Sales Order - User | `base_automation_235_update_analytic_tag_parameters_sales_order_user` |  | When a record is created or updated on Sales Order, runs _Update Analytic Tag Parameters - Sales Order - User_. | `model sale.order` (sale)<br>`server action BugFix-Sales.server_action_2415_update_analytic_tag_parameters_sales_order_user` |  |

**Approval rules (7):**

| Name | Record name | Approver group | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Sales Order/SLS - Bank Guarantee Approval (Sales / Bank Guarantee Approver) (23) | `ar_final_sales_order_sls_bank_guarantee_approval_sales_bank_guarantee` | Sales / Jin - Sales - Bank Guarantee Approvers | Before action _SLS - Bank Guarantee Approval - Main_ on Sales Order runs, an approval from **Sales / Jin - Sales - Bank Guarantee Approvers** is required (step 1). | `group BugFix-Approvals.group_128_jin_sales_bank_guarantee_approvers` (BugFix-Approvals)<br>`model sale.order` (sale)<br>`server action BugFix-Sales.server_action_1487_sls_bank_guarantee_approval_main` |  |
| Sales Order/SLS - Create Customer Payment (User types / Internal User) (99) | `ar_final_sales_order_sls_create_customer_payment_user_types_internal_` | User types / Internal User | Before action _SLS - Create Customer Payment_ on Sales Order runs, an approval from **User types / Internal User** is required (step 1). | `group base.group_user` (base)<br>`model sale.order` (sale)<br>`server action BugFix-Sales.server_action_2341_sls_create_customer_payment` |  |
| Sales Order/SLS - Credit Limit Approval (Sales / Credit Limit Approver) (18) | `ar_final_sales_order_sls_credit_limit_approval_sales_credit_limit_app` | Sales / Jin - Sales - Credit Limit Approvers | Before action _SLS - Credit Limit Approval - Main_ on Sales Order runs, an approval from **Sales / Jin - Sales - Credit Limit Approvers** is required (step 1). | `group BugFix-Approvals.group_125_jin_sales_credit_limit_approvers` (BugFix-Approvals)<br>`model sale.order` (sale)<br>`server action BugFix-Sales.server_action_1435_sls_credit_limit_approval_main` |  |
| Sales Order/SLS - Margin Approval (Sales / Margin Approver) (27) | `ar_final_sales_order_sls_margin_approval_sales_margin_approver_27` | Sales / Jin - Sales - Sales Margin Approvers | Before action _SLS - Margin Approval - Main_ on Sales Order runs, an approval from **Sales / Jin - Sales - Sales Margin Approvers** is required (step 1). | `group BugFix-Approvals.group_131_jin_sales_sales_margin_approvers` (BugFix-Approvals)<br>`model sale.order` (sale)<br>`server action BugFix-Sales.server_action_1515_sls_margin_approval_main` |  |
| Sales Order/SLS - Over Commission Approval (Sales / Over Commission Approver) (26) | `ar_final_sales_order_sls_over_commission_approval_sales_over_commissi` | Sales / Jin - Sales - Over Commission Approvers | Before action _SLS - Over Commission Approval - Main_ on Sales Order runs, an approval from **Sales / Jin - Sales - Over Commission Approvers** is required (step 1). | `group BugFix-Approvals.group_130_jin_sales_over_commission_approvers` (BugFix-Approvals)<br>`model sale.order` (sale)<br>`server action BugFix-Sales.server_action_1505_sls_over_commission_approval_main` |  |
| Sales Order/SLS - Overdue Approval (Sales / Overdue Approver) (22) | `ar_final_sales_order_sls_overdue_approval_sales_overdue_approver_22` | Sales / Jin - Sales - Overdue Approvers | Before action _SLS - Overdue Approval_ on Sales Order runs, an approval from **Sales / Jin - Sales - Overdue Approvers** is required (step 1). | `group BugFix-Approvals.group_127_jin_sales_overdue_approvers` (BugFix-Approvals)<br>`model sale.order` (sale)<br>`server action BugFix-Sales.server_action_1478_sls_overdue_approval` |  |
| Sales Order/SLS - Temporary Credit Approval (Sales / Temporary Credit Approver) (19) | `ar_final_sales_order_sls_temporary_credit_approval_sales_temporary_cr` | Sales / Jin - Sales - Temporary Credit Approvers | Before action _SLS - Temporary Credit Approval - Main_ on Sales Order runs, an approval from **Sales / Jin - Sales - Temporary Credit Approvers** is required (step 1). | `group BugFix-Approvals.group_126_jin_sales_temporary_credit_approvers` (BugFix-Approvals)<br>`model sale.order` (sale)<br>`server action BugFix-Sales.server_action_1470_sls_temporary_credit_approval_main` |  |

**Window actions (12):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Project Sales Orders | `aw_f4_sale_order_project_sales_orders` | Opens **Sales Order** records (kanban,tree,form,calendar,pivot,graph,activity), filtered to `[('x_studio_quotation_type', '=', 'Project')]`. | `model sale.order` (sale)<br>`sale.order.x_studio_quotation_type` | `menu BugFix-Sales.menu_f6_project_sales_orders` |
| Project Sales Orders | `act_window_2338_project_sales_orders` | Opens **Sales Order** records (kanban,tree,form,calendar,pivot,graph,activity), filtered to `[('x_studio_quotation_type', '=', 'Project')]`. | `model sale.order` (sale)<br>`sale.order.x_studio_quotation_type` | `menu BugFix-Sales.menu_1089_project_sales_orders` |
| Repair Sales Order List | `aw_f4_sale_order_repair_sales_order_list` | Opens **Sales Order** records (kanban,tree,form,calendar,pivot,graph,activity), filtered to `[('x_studio_quotation_type', '=', 'Repair')]`. | `model sale.order` (sale)<br>`sale.order.x_studio_quotation_type` | `menu BugFix-Sales.menu_f6_repair_sales_order_list` |
| Repair Sales Order List | `act_window_2330_repair_sales_order_list` | Opens **Sales Order** records (kanban,tree,form,calendar,pivot,graph,activity), filtered to `[('x_studio_quotation_type', '=', 'Repair')]`. | `model sale.order` (sale)<br>`sale.order.x_studio_quotation_type` | `menu BugFix-Sales.menu_1088_repair_sales_order_list` |
| SS | `aw_f4_sale_order_ss` | Opens **Sales Order** records (kanban,tree,form,calendar,pivot,graph,activity). | `model sale.order` (sale) |  |
| SS | `act_window_2439_ss` | Opens **Sales Order** records (kanban,tree,form,calendar,pivot,graph,activity). | `model sale.order` (sale) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_ss` (BugFix-Studio-Misc) |
| Sales Orders | `aw_f4_sale_order_sales_orders` | Opens **Sales Order** records (tree,form), filtered to `[('task_id', '=', active_id)]`. | `model sale.order` (sale)<br>`sale.order.task_id` (industry_fsm_sale) |  |
| Sales Orders | `act_window_2571_sales_orders` | Opens **Sales Order** records (tree,form), filtered to `[('task_id', '=', active_id)]`. | `model sale.order` (sale)<br>`sale.order.task_id` (industry_fsm_sale) |  |
| Sales orders | `aw_f4_sale_order_sales_orders_1` | Opens **Sales Order** records (tree,form), filtered to `[('x_studio_related_field_f6P0a', '=', active_id)]`. | `model sale.order` (sale) |  |
| Sales orders | `act_window_785_sales_orders` | Opens **Sales Order** records (tree,form), filtered to `[('x_studio_related_field_f6P0a', '=', active_id)]`. | `model sale.order` (sale) |  |
| sale.order | `aw_f4_sale_order_sale_order` | Opens **Sales Order** records (kanban,tree,form,calendar,pivot,graph,activity). | `model sale.order` (sale) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_sale_order` (BugFix-Studio-Misc) |
| sale.order | `act_window_2283_sale_order` | Opens **Sales Order** records (kanban,tree,form,calendar,pivot,graph,activity). | `model sale.order` (sale) |  |

**Views (8):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: sale.order.form customization | `ported_odoo_studio_sale_ord_ec04cc0c_2274_4a3f_8a1d_c240a65d1ca3` | form | set create=false on `//form[1]`; inside `//sheet`: add field x_studio_overdue, field x_studio_overdue_approved, field x_studio_overdue_request_sent, field x_studio_valid_order_lines, field x_studio_clear_free_items, field x_studio_expired; inside `//header`: add button 'Request Overdue Approval', button 'Approve Overdue'; inside `//sheet`: add field x_studio_over_commission, field x_studio_over_commission_approved, field x_studio_over_comm_approval_request_sent; inside `//header`: add button 'Request Over Commission Approval', button 'Approve Over Commission'; inside `//sheet`: add field x_studio_margin_exceed, field x_studio_margin_approved, field x_studio_margin_approval_request_sent; inside `//header`: add button 'Request Insufficient Marginn Approval', button 'Approve Insufficient Margin', button 'Insufficient Margin Details'; inside `//sheet`: add field x_studio_over_credit, field x_studio_credit_limit_approved, field x_studio_approval_request_sent, field x_studio_credit_limit_validation, field x_studio_order_payment_method, field x_studio_grant_temporary_credit, field x_studio_temporary_credit_approved, field x_studio_tem_credit_approval_request_sent … | Sales order form: disables Create and adds the approval-control buttons (request/approve Overdue, Over Commission, Insufficient Margin, Credit Limit, Temporary Credit, Bank Guarantee, Project Item status) plus detail/notification buttons, each shown only when its hidden control flags apply. | `group stock.group_adv_location` (stock)<br>`group uom.group_uom` (uom)<br>`sale.order.is_expired` (sale)<br>`sale.order.line.currency_id` (sale)<br>`sale.order.line.discount` (sale)<details><summary>+141 more</summary>`sale.order.line.invoice_status` (sale)<br>`sale.order.line.name` (sale)<br>`sale.order.line.order_id` (sale)<br>`sale.order.line.price_subtotal` (sale)<br>`sale.order.line.product_id` (sale)<br>`sale.order.line.product_uom_qty` (sale)<br>`sale.order.line.product_uom` (sale)<br>`sale.order.line.qty_delivered` (sale)<br>`sale.order.line.qty_invoiced` (sale)<br>`sale.order.line.qty_to_deliver` (sale_stock)<br>`sale.order.line.qty_to_invoice` (sale)<br>`sale.order.line.route_id` (sale_stock)<br>`sale.order.line.salesman_id` (sale)<br>`sale.order.line.warehouse_id` (sale_stock)<br>`sale.order.line.x_studio_category`<br>`sale.order.line.x_studio_cost_amount_inventory_shortage`<br>`sale.order.line.x_studio_cost_amount_req_qty`<br>`sale.order.line.x_studio_cost_value`<br>`sale.order.line.x_studio_current_onhand`<br>`sale.order.line.x_studio_inventory_shortage`<br>`sale.order.line.x_studio_invt_status`<br>`sale.order.line.x_studio_project_no`<br>`sale.order.line.x_studio_warehouse_id`<br>`sale.order.state` (sale)<br>`sale.order.task_id` (industry_fsm_sale)<br>`sale.order.x_studio_account_mandatory`<br>`sale.order.x_studio_approval_request_sent`<br>`sale.order.x_studio_authorized_repair_user`<br>`sale.order.x_studio_bank_guarantee_approved`<br>`sale.order.x_studio_bank_guarantee_notification`<br>`sale.order.x_studio_bank_guarantee_request_sent`<br>`sale.order.x_studio_bank_guarantee_validation`<br>`sale.order.x_studio_bg_sent`<br>`sale.order.x_studio_budget_created`<br>`sale.order.x_studio_cancelled`<br>`sale.order.x_studio_clear_free_items`<br>`sale.order.x_studio_confirm_validation_1`<br>`sale.order.x_studio_confirm_validation`<br>`sale.order.x_studio_credit_limit_approved`<br>`sale.order.x_studio_credit_limit_validation`<br>`sale.order.x_studio_current_tot_amount_1`<br>`sale.order.x_studio_current_tot_amount`<br>`sale.order.x_studio_cust_total_receivable_1`<br>`sale.order.x_studio_cust_total_receivable`<br>`sale.order.x_studio_customer_bank_guarantee`<br>`sale.order.x_studio_customer_credit_limit`<br>`sale.order.x_studio_customer_payment_method`<br>`sale.order.x_studio_document_1`<br>`sale.order.x_studio_document_2`<br>`sale.order.x_studio_document_3`<br>`sale.order.x_studio_expired`<br>`sale.order.x_studio_expiry_date`<br>`sale.order.x_studio_fsm_done`<br>`sale.order.x_studio_fully_paid`<br>`sale.order.x_studio_grant_temporary_credit`<br>`sale.order.x_studio_guarantee_status`<br>`sale.order.x_studio_image_1`<br>`sale.order.x_studio_image_2`<br>`sale.order.x_studio_image_3`<br>`sale.order.x_studio_inventory_short`<br>`sale.order.x_studio_locked`<br>`sale.order.x_studio_main_project_2`<br>`sale.order.x_studio_main_project_no`<br>`sale.order.x_studio_many2one_field_KjdJ3`<br>`sale.order.x_studio_margin_approval_request_sent`<br>`sale.order.x_studio_margin_approved`<br>`sale.order.x_studio_margin_exceed`<br>`sale.order.x_studio_new_item_from_project`<br>`sale.order.x_studio_one2many_field_ERCBB`<br>`sale.order.x_studio_order_payment_method`<br>`sale.order.x_studio_over_bank_guarantee_amount`<br>`sale.order.x_studio_over_bank_guarantee`<br>`sale.order.x_studio_over_comm_approval_request_sent`<br>`sale.order.x_studio_over_commission_approved`<br>`sale.order.x_studio_over_commission`<br>`sale.order.x_studio_over_credit_amount`<br>`sale.order.x_studio_over_credit`<br>`sale.order.x_studio_overdue_approved`<br>`sale.order.x_studio_overdue_request_sent`<br>`sale.order.x_studio_overdue`<br>`sale.order.x_studio_petty_cash_reimbursement`<br>`sale.order.x_studio_pr_cost_updated`<br>`sale.order.x_studio_pr_created`<br>`sale.order.x_studio_price_not_confirmed`<br>`sale.order.x_studio_proj_budget_status`<br>`sale.order.x_studio_project_budget`<br>`sale.order.x_studio_project_end_date`<br>`sale.order.x_studio_project_group`<br>`sale.order.x_studio_project_item_approved`<br>`sale.order.x_studio_project_item_request_sent`<br>`sale.order.x_studio_project_no`<br>`sale.order.x_studio_project_start_date`<br>`sale.order.x_studio_quotation_type`<br>`sale.order.x_studio_re_estimate_count`<br>`sale.order.x_studio_re_estimate_request_count_1`<br>`sale.order.x_studio_re_estimate_request_sent`<br>`sale.order.x_studio_reject_reason`<br>`sale.order.x_studio_related_information`<br>`sale.order.x_studio_repair_image_01`<br>`sale.order.x_studio_repair_image_02`<br>`sale.order.x_studio_repair_reason`<br>`sale.order.x_studio_repair_validation`<br>`sale.order.x_studio_rug_approved`<br>`sale.order.x_studio_rug_confirmed`<br>`sale.order.x_studio_rug_rejected`<br>`sale.order.x_studio_rug_request_sent`<br>`sale.order.x_studio_sales_order_validity`<br>`sale.order.x_studio_sell_and_win`<br>`sale.order.x_studio_service_item_available`<br>`sale.order.x_studio_sub_contract`<br>`sale.order.x_studio_tem_credit_approval_request_sent`<br>`sale.order.x_studio_temporary_credit_approved`<br>`sale.order.x_studio_total_overdue`<br>`sale.order.x_studio_transfer_inventory_ok`<br>`sale.order.x_studio_unlocked`<br>`sale.order.x_studio_valid_bank_guarantee`<br>`sale.order.x_studio_valid_order_lines_for_projects`<br>`sale.order.x_studio_valid_order_lines_for_update_rfq_cost`<br>`sale.order.x_studio_valid_order_lines`<br>`sale.order.x_studio_valid_transfer`<br>`sale.order.x_studio_warranty_card`<br>`server action BugFix-Sales.server_action_1435_sls_credit_limit_approval_main`<br>`server action BugFix-Sales.server_action_1458_sls_request_credit_limit_approval`<br>`server action BugFix-Sales.server_action_1468_sls_request_temporary_credit_approval`<br>`server action BugFix-Sales.server_action_1470_sls_temporary_credit_approval_main`<br>`server action BugFix-Sales.server_action_1476_sls_request_overdue_approval`<br>`server action BugFix-Sales.server_action_1478_sls_overdue_approval`<br>`server action BugFix-Sales.server_action_1485_sls_request_bank_guarantee_approval`<br>`server action BugFix-Sales.server_action_1487_sls_bank_guarantee_approval_main`<br>`server action BugFix-Sales.server_action_1503_sls_request_over_commission_approval`<br>`server action BugFix-Sales.server_action_1505_sls_over_commission_approval_main`<br>`server action BugFix-Sales.server_action_1513_sls_request_margin_approval`<br>`server action BugFix-Sales.server_action_1515_sls_margin_approval_main`<br>`server action BugFix-Sales.server_action_1517_sls_item_over_margin_details`<br>`server action BugFix-Sales.server_action_1849_sls_view_bank_guarantee_validation`<br>`server action BugFix-Sales.server_action_1850_sls_send_bank_guarantee_notification_main`<br>`server action BugFix-Sales.server_action_1853_sls_view_credit_limit_validation`<br>`server action BugFix-Sales.server_action_2096_rr_insufficient_transfer_inventory_details`<br>`server action BugFix-Sales.server_action_2138_proj_project_item_approval_request_sent_validate`<br>`server action BugFix-Sales.server_action_2341_sls_create_customer_payment`<br>`view sale.view_order_form` (sale)</details> |  |
| Odoo Studio: sale.order.form customization_button | `ported_odoo_studio_sale_ord_2b440c7b_edb5_4cd8_827e_19fbb95a85a9` | form | set invisible=((x_studio_rug_rejected == False) and ((x_studio_rug_approved == False) and (x_studio_rug_confirmed == True))) or (((x_studio_bg_sent == False) and (x_studio_bank_guarantee_notification == True)) or (((x_studio_margin_approved == False) and (x_studio_margin_exceed == True)) or (((x_studio_over_commission_approved == False) and (x_studio_over_commission == True)) or (((x_studio_overdue_approved == False) and (x_studio_overdue == True)) or (((x_studio_bank_guarantee_approved != True) and (x_studio_over_bank_guarantee != False)) or (((x_studio_temporary_credit_approved != True) and (x_studio_grant_temporary_credit != False)) or (((x_studio_tem_credit_approval_request_sent != True) and (x_studio_grant_temporary_credit != False)) or (((x_studio_credit_limit_approved != True) and (x_studio_over_credit != False)) or ((x_studio_new_item_from_project != False) or ((state not in ['sent']) or ((x_studio_valid_order_lines == False) or ((x_studio_bank_guarantee_validation == True) or ((x_studio_credit_limit_validation == True) or ((x_studio_transfer_inventory_ok == True) or ((x_studio_expired == True) or ((x_studio_cancelled == True) or (x_studio_clear_free_items == True))))))))))))))))) on `//header/button[@name='action_confirm' and @id='action_confirm']` | Inactive view (archived). Would hide the Confirm button on sales orders unless all approval, validity, credit, bank-guarantee and inventory conditions are met; has no effect while inactive. | `view sale.view_order_form` (sale) |  |
| Odoo Studio: sale.order.form customization_button_2 | `view_3922_odoo_studio_sale_order_form_customization_button_2_e` | form |  | Inactive, empty view: all its button changes were stripped during migration, so it has no effect. | `view sale.view_order_form` (sale) |  |
| Odoo Studio: sale.order.pivot customization | `ported_odoo_studio_sale_ord_71749d4c_8fb8_46b0_a187_bfa8977a25fd` | pivot | set display_quantity=true on `//pivot[1]` | Sales order pivot view: turns on display of the record count/quantity measure. | `view sale.view_sale_order_pivot` (sale) |  |
| Odoo Studio: sale.order.tree (orders) customization | `ported_odoo_studio_sale_ord_42b65c93_ce32_435b_8978_554c017d8d4c` | tree | set create=true on `//tree[1]` | Sales Orders list: explicitly allows the Create button. | `view sale.view_order_tree` (sale) |  |
| Odoo Studio: sale.order.tree customization | `ported_odoo_studio_sale_ord_d30b53b2_bf08_42d7_a477_18497e66a5f5` | tree | set create=false on `//tree[1]`; after `//tree[1]/field[@name='name']`: add field x_studio_quotation_type; after `//field[@name='date_order']`: add field create_date; set sum=Sum of Total on `//field[@name='amount_total']`; after `//field[@name='invoice_status']`: add field id, xpath, field x_studio_credit_limit_approved, field x_studio_overdue_approved, field x_studio_bank_guarantee_approved, field x_studio_temporary_credit_approved, field x_studio_over_commission_approved, field x_studio_margin_approved, field x_studio_overdue, field x_studio_over_credit, field x_studio_over_bank_guarantee, field x_studio_margin_exceed …; set optional=hide, invisible= on `//field[@name='state']` | Sales order list: disables Create, adds Quotation Type and Creation Date columns, a Total sum, and optional (hidden) columns for each approval and exceed flag (credit, overdue, bank guarantee, temporary credit, commission, margin); Status becomes optional. | `sale.order.x_studio_bank_guarantee_approved`<br>`sale.order.x_studio_credit_limit_approved`<br>`sale.order.x_studio_margin_approved`<br>`sale.order.x_studio_margin_exceed`<br>`sale.order.x_studio_over_bank_guarantee`<details><summary>+8 more</summary>`sale.order.x_studio_over_commission_approved`<br>`sale.order.x_studio_over_commission`<br>`sale.order.x_studio_over_credit`<br>`sale.order.x_studio_overdue_approved`<br>`sale.order.x_studio_overdue`<br>`sale.order.x_studio_quotation_type`<br>`sale.order.x_studio_temporary_credit_approved`<br>`view sale.sale_order_tree` (sale)</details> |  |
| Odoo Studio: sale.order.tree customization | `ported_odoo_studio_sale_ord_b4d2d01a_3a8c_4827_885c_7390c53f2113` | tree | set create=true on `//tree[1]` | Quotations list: explicitly allows the Create button. | `view sale.view_quotation_tree_with_onboarding` (sale) |  |
| sale.order.form.bugfix_sales | `view_order_form_bugfix_sales` | form | after `//field[@name='validity_date']`: add field bugfix_sales_intro_id, field bugfix_sales_conclusion_id; inside `//notebook`: add page 'Document Text' | Sales order form: adds Document Introduction and Document Conclusion selectors after the expiration date, and a 'Document Text' tab where the introduction and conclusion texts can be edited per quotation. | `sale.order.bugfix_sales_conclusion_id`<br>`sale.order.bugfix_sales_conclusion_text`<br>`sale.order.bugfix_sales_intro_id`<br>`sale.order.bugfix_sales_intro_text`<br>`view sale.view_order_form` (sale) |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Inv - Administrator | `access_6246_inv___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Sales Order records. | `group stock.group_stock_manager` (stock)<br>`model sale.order` (sale) |  |
| Sales Order | `access_6849_sales_order` | Gives **Sales / Jin - Sales - POS Users** read/write/create access to Sales Order records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model sale.order` (sale) |  |
| User | `access_6086_user` | Gives **Helpdesk / User** read/write/create access to Sales Order records. | `group helpdesk.group_helpdesk_user` (helpdesk)<br>`model sale.order` (sale) |  |

**Record rules (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| All Orders | `rule_165_all_orders` | For Sales / User: All Documents: read/write/create/delete on Sales Order with no record filter (empty domain = all records). | `group sales_team.group_sale_salesman_all_leads` (sales_team)<br>`model sale.order` (sale) |  |
| Personal Orders | `rule_164_personal_orders` | For Sales / User: Own Documents Only: read/write/create/delete on Sales Order only where `['|',('user_id','=',user.id),('user_id','=',False)]`. | `group sales_team.group_sale_salesman` (sales_team)<br>`model sale.order` (sale)<br>`sale.order.user_id` (sale) |  |
| Portal Personal Quotations/Sales Orders | `rule_162_portal_personal_quotations_sales_orders` | For User types / Portal: read/write/create/delete on Sales Order only where `[('message_partner_ids','child_of',[user.commercial_partner_id.id])]`. | `group base.group_portal` (base)<br>`model sale.order` (sale)<br>`sale.order.message_partner_ids` (sale) |  |
| Sales Order - View Only | `rule_500_sales_order_view_only` | For everyone (global rule): read on Sales Order with no record filter (empty domain = all records). | `model sale.order` (sale) |  |
| Sales Order multi-company | `rule_157_sales_order_multi_company` | For everyone (global rule): read/write/create/delete on Sales Order only where `[('company_id', 'in', company_ids)]`. | `model sale.order` (sale)<br>`sale.order.company_id` (sale) |  |
| Sales Orders for Sales Centers | `rule_337_sales_orders_for_sales_centers` | For everyone (global rule): read/write/create/delete on Sales Order with no record filter (empty domain = all records). | `model sale.order` (sale) |  |
| Subscription multi-company | `rule_191_subscription_multi_company` | For everyone (global rule): read/write/create/delete on Sales Order only where `[('company_id', 'in', company_ids + [False])]`. | `model sale.order` (sale)<br>`sale.order.company_id` (sale) |  |
| Subscription portal access | `rule_198_subscription_portal_access` | For User types / Portal: read/write on Sales Order only where `[('partner_id','in',[user.partner_id.id,user.commercial_partner_id.id])]`. | `group base.group_portal` (base)<br>`model sale.order` (sale)<br>`sale.order.partner_id` (sale) |  |
