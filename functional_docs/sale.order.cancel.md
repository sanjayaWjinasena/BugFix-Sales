# BugFix-Sales — `sale.order.cancel`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `sale.order.cancel` — Sales Order Cancel

*Extends a model created by `sale`.*

**Summary:**

<!-- SUMMARY:model:sale.order.cancel -->
This repo only ships a record rule for the Sales Order Cancel wizard. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Order Cancel Rule | `rule_180_sales_order_cancel_rule` | For everyone (global rule): read/write/create/delete on Sales Order Cancel only where `[('create_uid', '=', user.id)]`. | `model sale.order.cancel` (sale) |  |
