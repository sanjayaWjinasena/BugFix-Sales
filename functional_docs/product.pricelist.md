# BugFix-Sales — `product.pricelist`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.pricelist` — Pricelist

*Extends a model created by `product`.* Python: `models/product_pricelist.py`.

Other repos that use this model: `server action BugFix-Accounting.action_sales_report_model_srm_rpt_costing_work_sheet` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_srm_rpt_costing_work_sheet` (BugFix-Accounting)<br>`bve.salesreport.bve_t1_pricelist_id` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:product.pricelist -->
This repo adds Group Type (General, Distributor or Dealer), Order Payment Method (Cash or Credit) and a Project Price List flag to pricelists, shown on the pricelist form and list, plus a legacy unused selection kept for data loading. These fields let sales orders pick the right pricelist for the customer's group and payment type, and let Project quotations use the project price list. An automation sets the pricelist's Company to the user's current company, and the repo ships the pricelist multi-company record rules.
<!-- /SUMMARY -->

**Fields (4):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `group_type` | Group Type | selection: General=General; Distributor=Distributor; Dealer=Dealer | Customer group the pricelist is meant for: General, Distributor or Dealer; entered by the user on the pricelist form and list. | stored |  | `view BugFix-Sales.view_product_pricelist_tree_inherit`<br>`view BugFix-Sales.view_product_pricelist_form_inherit` |
| `order_payment_method` | Order Payment Method | selection: Cash=Cash; Credit=Credit | Payment type the pricelist applies to (Cash or Credit); entered on the pricelist form and list. | stored |  | `view BugFix-Sales.view_product_pricelist_tree_inherit`<br>`view BugFix-Sales.view_product_pricelist_form_inherit` |
| `project_price_list` | Project Price List | boolean | Marks the pricelist as a Project price list; entered on the pricelist form. | stored |  | `view BugFix-Sales.view_product_pricelist_form_inherit` |
| `zzzz` | zzzz | selection: 0=Normal; 1=Low; 2=High; 3=Very High | Legacy Studio selection (Normal/Low/High/Very High) kept only so migrated pricelist data loads. Not used by any view or logic in this repo. | stored |  |  |

**Server actions (2):**

- **Execute Code** (`action_jin_company_id_in_pricelist`, type `code`)
  - Function: Run by its automation: sets the pricelist's Company to the user's currently selected company.
  - Depends on: `model product.pricelist` (product), `model res.company` (base)
  - Used by: `automation BugFix-Sales.automation_jin_company_id_in_pricelist`
  <details><summary>code (5 lines)</summary>

```python
company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
company = env["res.company"].browse(company_id)

record["company_id"] = company.id
```
  </details>
- **JIN - Company Id in Pricelist** (`action_product_pricelist_jin_company_id_in_pricelist`, type `code`)
  - Function: Sets the pricelist's Company to the user's currently selected company.
  - Depends on: `model product.pricelist` (product), `model res.company` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
company = env["res.company"].browse(company_id)

record["company_id"] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Pricelist | `automation_jin_company_id_in_pricelist` |  | When a record is created or updated on Pricelist, runs _Execute Code_. | `model product.pricelist` (product)<br>`product.pricelist.create_date` (product)<br>`server action BugFix-Sales.action_jin_company_id_in_pricelist` |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: product.pricelist.form customization | `view_product_pricelist_form_inherit` | form | after `//form[1]/sheet[1]/group[1]/group[@name='pricelist_settings']/field[@name='currency_id']`: add field group_type, field order_payment_method, field project_price_list; set force_save=True, readonly=1 on `//form[1]/sheet[1]/group[1]/group[@name='pricelist_settings']/field[@name='company_id']`; after `//field[@name='date_end']`: add | Pricelist form: adds required Group Type and Order Payment Method plus Project Price List after currency, and makes Company read-only. | `product.pricelist.group_type`<br>`product.pricelist.order_payment_method`<br>`product.pricelist.project_price_list`<br>`view product.product_pricelist_view` (product) |  |
| Odoo Studio: product.pricelist.tree customization | `view_product_pricelist_tree_inherit` | tree | after `//field[@name='currency_id']`: add field group_type, field order_payment_method, field id; after `//field[@name='company_id']`: add field create_uid | Pricelist list: adds Group Type, Order Payment Method and ID columns, plus an optional hidden Created By column. | `product.pricelist.group_type`<br>`product.pricelist.order_payment_method`<br>`view product.product_pricelist_view_tree` (product) |  |

**Record rules (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| product pricelist company rule | `rule_40_product_pricelist_company_rule` | For everyone (global rule): read/write/create/delete on Pricelist only where `['|', ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]`. | `model product.pricelist` (product)<br>`product.pricelist.company_id` (product) |  |
| product pricelist company rule | `rule_product_pricelist_company_rule` | For everyone (global rule): read/write/create/delete on Pricelist only where `['|', ('company_id', 'in', [False,website.company_id.id]), ('company_id', 'in', company_ids)]`. | `model product.pricelist` (product)<br>`product.pricelist.company_id` (product) |  |
