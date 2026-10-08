# BugFix-Sales — `res.config.settings`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `res.config.settings` — Config Settings

*Extends a model created by `base`.* Python: `models/res_config_settings.py`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_res_config_settings_group_system` (BugFix-Studio-Misc)<br>`server action BugFix-Accounting.server_action_1370_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:res.config.settings -->
This repo adds a Sales Configurations block to the Sales settings screen with the company's Minimum Sales Margin %, Advance Payment %, Sales Order Validity (Days) and Last Purchase Price Validity (Days). The fields are linked to the company values, so editing them here updates the current company's settings.
<!-- /SUMMARY -->

**Fields (4):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_advance_payment_` | Advance Payment % | float | Settings-screen field for the company's Advance Payment % (related to the company value) required before repair deliveries. | related `company_id.x_studio_advance_payment_`; not stored | `res.company.x_studio_advance_payment_`<br>`res.config.settings.company_id` (base_setup) | `view BugFix-Sales.res_config_settings_view_form_bugfix_sales` |
| `x_studio_last_purchase_price_validity_days` | Last Purchase Price Validity (Days) | integer | Settings-screen field for the company's Last Purchase Price Validity in days (related to the company value). | related `company_id.x_studio_last_purchase_price_validity_days`; not stored | `res.company.x_studio_last_purchase_price_validity_days`<br>`res.config.settings.company_id` (base_setup) | `view BugFix-Sales.res_config_settings_view_form_bugfix_sales` |
| `x_studio_minimum_sales_margin_` | Minimum Sales Margin % | float | Settings-screen field for the company's Minimum Sales Margin % (related to the company value) enforced at quotation Confirm. | related `company_id.x_studio_minimum_sales_margin_`; not stored | `res.company.x_studio_minimum_sales_margin_`<br>`res.config.settings.company_id` (base_setup) | `view BugFix-Sales.res_config_settings_view_form_bugfix_sales` |
| `x_studio_sales_order_validity` | Sales Order Validity (Days) | integer | Settings-screen field for the company's quotation validity in days (related to the company value). | related `company_id.x_studio_sales_order_validity`; not stored | `res.company.x_studio_sales_order_validity`<br>`res.config.settings.company_id` (base_setup) | `view BugFix-Sales.res_config_settings_view_form_bugfix_sales` |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| res.config.settings.form.bugfix_sales | `res_config_settings_view_form_bugfix_sales` | form | inside `//app[@name='sale_management']`: add block | Sales settings: adds a 'Sales Configurations' block with Minimum Sales Margin %, Advance Payment %, Sales Order Validity (Days) and Last Purchase Price Validity (Days). | `res.config.settings.x_studio_advance_payment_`<br>`res.config.settings.x_studio_last_purchase_price_validity_days`<br>`res.config.settings.x_studio_minimum_sales_margin_`<br>`res.config.settings.x_studio_sales_order_validity`<br>`view sale.res_config_settings_view_form` (sale) |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| res.config.settings group_system | `access_1531_res_config_settings_group_system` | Gives **Administration / Settings** read/write/create/delete access to Config Settings records. | `group base.group_system` (base)<br>`model res.config.settings` (base) |  |
| res.config.settings group_user | `access_1532_res_config_settings_group_user` | Gives **User types / Internal User** read/write/create access to Config Settings records. | `group base.group_user` (base)<br>`model res.config.settings` (base) |  |
