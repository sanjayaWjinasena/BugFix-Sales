# BugFix-Sales — `sale.mass.cancel.orders`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `sale.mass.cancel.orders` — Cancel multiple quotations

*Extends a model created by `sale`.*

**Summary:**

<!-- SUMMARY:model:sale.mass.cancel.orders -->
This repo only ships a record rule that limits each user to their own Cancel multiple quotations wizard. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Mass Cancel Orders: access only your own wizard | `rule_779_sales_mass_cancel_orders_access_only_your_own_wizard` | For everyone (global rule): read/write/create/delete on Cancel multiple quotations only where `[('create_uid', '=', user.id)]`. | `model sale.mass.cancel.orders` (sale) |  |
