# BugFix-Sales — `product.packaging`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.packaging` — Product Packaging

*Extends a model created by `product`.*

**Summary:**

<!-- SUMMARY:model:product.packaging -->
This repo only ships the multi-company record rule for product packaging (product packaging company rule). It adds no fields, views or logic.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| product packaging company rule | `rule_43_product_packaging_company_rule` | For everyone (global rule): read/write/create/delete on Product Packaging only where `['|', ('company_id', '=', False), ('company_id', 'parent_of', company_ids)]`. | `model product.packaging` (product)<br>`product.packaging.company_id` (product) |  |
