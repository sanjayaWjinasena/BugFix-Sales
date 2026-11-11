# BugFix-Sales — `product.category`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.category` — Product Category

*Extends a model created by `product`.*

Other repos that use this model: `account.analytic.account.bugfix_analytics_product_category_id` (BugFix-Analytics)<br>`account.move.line.product_category` (BugFix-Accounting)<br>`window action BugFix-Studio-Misc.action_product_categories_d7` (BugFix-Studio-Misc)<br>`rm_none_moving.product_category` (BugFix-Accounting)<br>`rm_sales_order_line.product_category` (BugFix-Accounting)<br>`rm_sales_prod_purch.product_category` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:product.category -->
This repo adds one automation, JIN - Company Id in Product Category, which runs on create and update and fills the category's Company with the user's current company while the category is still unsaved.
<!-- /SUMMARY -->

**Server actions (1):**

- **Execute Code** (`action_jin_company_id_in_product_category`, type `code`)
  - Function: Run by an automation on product categories: when the category is still unsaved, sets its Company (`accounting_company_id`) to the user's currently active company.
  - Depends on: `model product.category` (product), `model res.company` (base), `product.category.accounting_company_id` (BugFix-Studio-Misc)
  - Used by: `automation BugFix-Sales.automation_jin_company_id_in_product_category`
  <details><summary>code (5 lines)</summary>

```python
if record.id == False:
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    record["accounting_company_id"] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Product Category | `automation_jin_company_id_in_product_category` |  | When a record is created or updated on Product Category, runs _Execute Code_. | `model product.category` (product)<br>`product.category.create_date` (product)<br>`server action BugFix-Sales.action_jin_company_id_in_product_category` |  |
