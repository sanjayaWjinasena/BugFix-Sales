# BugFix-Sales — `x_sales_report_type`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_sales_report_type` — Sales Report Type

*Extends a model created by `Jinasena_Masterdata_Reporting`.* Python: `models/x_sales_report_type.py`.

Other repos that use this model: `access right BugFix-Accounting.access_1500_sales_report_type_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_1501_sales_report_type_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_x_sales_report_type_user` (BugFix-Accounting)<br>`access right Jinasena_Masterdata_Reporting.access_x_sales_report_type_user` (Jinasena_Masterdata_Reporting)<br>`account.bank.statement.line.x_studio_many2one_field_L9MIu` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_report_type_s_cust_aging` (Jinasena_Masterdata_Reporting)<br>`account.move.line.x_studio_many2one_field_kiSUJ` (Jinasena_Masterdata_Reporting)<br>`account.move.line.x_studio_sales_report_type` (Jinasena_Masterdata_Reporting)<details><summary>+22 more</summary>`account.move.x_studio_report_type_s_cust_aging` (Jinasena_Masterdata_Reporting)<br>`account.payment.x_studio_many2one_field_L9MIu` (BugFix-Accounting)<br>`account.payment.x_studio_report_type_s_cust_aging` (Jinasena_Masterdata_Reporting)<br>`mrp.production.x_studio_report_type_m_wip` (Jinasena_Masterdata_Reporting)<br>`sale.order.line.x_studio_sales_report_type` (Jinasena_Masterdata_Reporting)<br>`server action BugFix-Accounting.server_action_1732_srm_auto_populate_report_type_in_account_move_lines` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1740_srm_auto_populate_report_type_in_account_move` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2116_project_gross_margin_report` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2127_project_gross_margin_delete_reports` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2128_project_gross_margin_report_management_purpose` (BugFix-Accounting)<br>`server action BugFix-MRP.server_action_1738_srm_auto_populate_report_type_in_production_order` (BugFix-MRP)<br>`server action BugFix-Project.server_action_2130_project_update_project_gross_margin_report_auto_generate` (BugFix-Project)<br>`server action BugFix-Project.server_action_2131_project_update_project_gross_margin_report_auto_generate` (BugFix-Project)<br>`server action BugFix-Stock.server_action_1742_srm_auto_populate_report_type_in_product_moves` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1752_srm_auto_populate_report_type_in_product_moves_2` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1755_srm_auto_populate_report_type_in_product_variance_moves` (BugFix-Stock)<br>`stock.move.line.x_studio_report_type_production_summary_split` (Jinasena_Masterdata_Reporting)<br>`stock.move.line.x_studio_report_type_sales_prod_purch` (Jinasena_Masterdata_Reporting)<br>`stock.move.line.x_studio_report_type_slow_moving_items` (Jinasena_Masterdata_Reporting)<br>`stock.move.x_studio_report_type_production_job_variance` (Jinasena_Masterdata_Reporting)<br>`window action BugFix-Accounting.action_1668_sales_report_type` (BugFix-Accounting)<br>`x_sales_report_model.x_studio_report_type` (Jinasena_Masterdata_Reporting)</details>

**Summary:**

<!-- SUMMARY:model:x_sales_report_type -->
This repo only adds a Sales Report Type window action and a user access right for this model, which is created by Jinasena_Masterdata_Reporting. Sales order lines in this repo link to it through their Sales Report Type field.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Report Type | `act_window_1668_sales_report_type` | Opens **Sales Report Type** records (tree,form). | `model x_sales_report_type` (Jinasena_Masterdata_Reporting) |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_sales_report_type user access | `access_x_sales_report_type_user` | Gives **User types / Internal User** read/write/create/delete access to Sales Report Type records. | `group base.group_user` (base)<br>`model x_sales_report_type` (Jinasena_Masterdata_Reporting) |  |
