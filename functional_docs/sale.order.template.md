# BugFix-Sales — `sale.order.template`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `sale.order.template` — Quotation Template

*Extends a model created by `sale_management`.*

**Summary:**

<!-- SUMMARY:model:sale.order.template -->
This repo only ships the quotation template access right and multi-company record rule. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| sale.order.template | `access_6855_sale_order_template` | Gives **Sales / Jin - Sales - POS Users** read access to Quotation Template records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model sale.order.template` (sale_management) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Quotation Template multi-company | `rule_185_quotation_template_multi_company` | For everyone (global rule): read/write/create/delete on Quotation Template only where `[('company_id', 'in', company_ids + [False])]`. | `model sale.order.template` (sale_management)<br>`sale.order.template.company_id` (sale_management) |  |
