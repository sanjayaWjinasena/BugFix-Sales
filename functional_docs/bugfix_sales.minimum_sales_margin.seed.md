# BugFix-Sales — `bugfix_sales.minimum_sales_margin.seed`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `bugfix_sales.minimum_sales_margin.seed` — Seed Minimum Sales Margin config per company

*Created by this repo.* Python: `models/minimum_sales_margin_seed.py`.

**Summary:**

<!-- SUMMARY:model:bugfix_sales.minimum_sales_margin.seed -->
A technical helper with no fields or views; it holds the install and upgrade routines for the sales configuration. Its methods seed one Minimum Sales Margin % row and default company-scoped system parameters for every company, move the margin settings into system parameters, patch Studio server actions and computes to read the company's settings, attach the introduction and conclusion texts to the C01 Sales Quotation report, archive the old Minimum Sales Margin menus, remove orphan Studio menu references and disable the Clear Free Items automation.
<!-- /SUMMARY -->

**Python methods (9):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_seed_minimum_sales_margin_per_company` | Upgrade/install helper that inserts (via SQL) one default Minimum Sales Margin % row for every company lacking one, using the module's default margin, advance %, and validity values. Idempotent; per the later docstring this old-model seed was dropped in v22. | api.model |  | `model res.company` (base) |  | `models/minimum_sales_margin_seed.py:60` |
| `_seed_ir_config_parameter_defaults` | Upgrade/install helper that writes default per-company Sales config values (margin %, advance %, validity days) into ir.config_parameter for any company missing a key, so the margin gate is active on new companies. Never overwrites existing values. | api.model |  | `model ir.config_parameter` (base)<br>`model res.company` (base) |  | `models/minimum_sales_margin_seed.py:134` |
| `_suppress_validate_sales_lines_button` | Upgrade helper that deactivates the 'SLS - Clear Free Items SO Lines' automation on sale.order.line, so the Clear Free Items flag never flips and the 'Validate Sales Lines' button stays hidden. Reversible by reactivating the automation. | api.model |  | `model base.automation` (base_automation) |  | `models/minimum_sales_margin_seed.py:202` |
| `_convert_line_margin_flag_to_computed` | Upgrade helper that rewrites the Studio field sale.order.line Margin Exceed into a non-stored compute (fresh on every read), tightens the SO header rollup's depends, and deactivates the old on-change automation. Skips when the fields are already Python-declared. | api.model |  | `model base.automation` (base_automation)<br>`model ir.model.fields` (base) |  | `models/minimum_sales_margin_seed.py:244` |
| `_patch_studio_readers_to_use_company` | Upgrade helper that patches Studio server actions and computed fields reading `env['x_minimum_sales_margin'].search(...)` so they read the margin settings from the record's company (or env.company) instead. Idempotent via a marker comment and only patches verbatim matches. | api.model |  | `model ir.actions.server` (base)<br>`model ir.model.fields` (base) |  | `models/minimum_sales_margin_seed.py:334` |
| `_migrate_to_config_parameter` | One-shot upgrade helper copying each company's Minimum Sales Margin % row values into company-scoped ir.config_parameter keys, without overwriting existing keys. Skips if the Studio model does not exist. | api.model |  | `model ir.config_parameter` (base)<br>`model res.company` (base)<br>`model x_minimum_sales_margin` |  | `models/minimum_sales_margin_seed.py:469` |
| `_attach_c01_intro_conclusion_view` | Upgrade helper that finds the Studio 'C01 Sales Quotation' report, derives its document sub-template, and creates/updates an inheriting QWeb view adding the Document Introduction/Conclusion text; removes the overlay if the report no longer exists. | api.model |  | `model ir.actions.report` (base)<br>`model ir.model.data` (base)<br>`model ir.ui.view` (base) |  | `models/minimum_sales_margin_seed.py:555` |
| `_cleanup_orphan_studio_menu_pins` | Upgrade housekeeping that deletes studio_customization external-ID records pointing at menus that no longer exist. Idempotent, touches only ir.ui.menu pins. | api.model |  | `model ir.model.data` (base)<br>`model ir.ui.menu` (base) |  | `models/minimum_sales_margin_seed.py:657` |
| `_hide_minimum_sales_margin_menus` | Upgrade helper that archives every menu opening a window action on the Minimum Sales Margin % model, since these values are now edited in Settings > Sales. Data, views and actions are kept. | api.model |  | `model ir.actions.act_window` (base)<br>`model ir.ui.menu` (base) |  | `models/minimum_sales_margin_seed.py:696` |
