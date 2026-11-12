# BugFix-Sales — `product.pricelist.item`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.pricelist.item` — Pricelist Rule

*Extends a model created by `product`.* Python: `models/product_pricelist.py`.

Other repos that use this model: `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_costing_work_sheet` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2490_srm_rpt_costing_work_sheet` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:product.pricelist.item -->
This repo adds a single Price Confirmed checkbox to pricelist rules. It is not used by any view or logic in this repo; the sales order line Price Confirmed actions read the matching pricelist item for Project lines.
<!-- /SUMMARY -->

**Fields (1):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_price_confirmed` | Price Confirmed | boolean | Checkbox on a pricelist rule indicating the price is confirmed. Not used by any view or logic in this repo. | stored |  |  |
