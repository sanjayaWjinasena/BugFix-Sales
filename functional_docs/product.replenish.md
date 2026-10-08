# BugFix-Sales — `product.replenish`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.replenish` — Product Replenish

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:product.replenish -->
This repo only ships one access right on the replenish wizard (Jin - Administrator). It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jin - Administrator | `access_7277_jin___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Product Replenish records. | `group stock.group_stock_manager` (stock)<br>`model product.replenish` (stock) |  |
