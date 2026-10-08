# BugFix-Sales — `sale.order.alert`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `sale.order.alert` — Sale Order Alert

*Extends a model created by `sale_subscription`.* Python: `models/sale_order_alert.py`.

**Summary:**

<!-- SUMMARY:model:sale.order.alert -->
This repo adds four Studio fields to subscription alerts (Comments, Status and two unnamed fields). None of them is used by any view or logic in this repo.
<!-- /SUMMARY -->

**Fields (4):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_char_field_dpQHc` | New Text | char | Unnamed Studio text field on sale order alerts ('New Text'). Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_comments` | Comments | char | Free-text comments on a sale order alert record. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_selection_field_ogQSe` | New Selection | selection | Unnamed Studio selection on sale order alerts with no options declared in code. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_status` | Status | selection | Status of a sale order alert; its options are not declared in the Python field (empty selection). Not used by any view or logic in this repo. | stored |  |  |
