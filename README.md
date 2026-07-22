# BugFix - Sales

**Version:** 17.0.1.0.20
**Odoo base:** 17.0 (Enterprise)
**Category:** Sales
**Author:** Jinasena Agricultural Machinery (Pvt) Ltd.
**License:** LGPL-3

BugFix-Sales is the companion module to [Fix-repair](../Fix-repair/README.md).
It carries **cross-cutting Sales workflow fixes** that aren't repair-specific
— things any Sales SO or Contact form benefits from — plus the shared
per-company **Sales Configurations** used by both modules.

Whereas Fix-repair scopes to the helpdesk-repair pipeline, BugFix-Sales
scopes to the plain Sales side: `sale.order`, `res.partner`,
report templates like C01 Sales Quotation, and configuration.

---

## Table of contents

1. [Scope](#1-scope)
2. [Runtime dependencies](#2-runtime-dependencies)
3. [Module layout](#3-module-layout)
4. [Feature areas](#4-feature-areas)
   - 4.1 Document Introduction & Conclusion on quotations
   - 4.2 Reference field UX on Contact form
   - 4.3 Sales Configurations moved to Settings
   - 4.4 Per-company config seeding
   - 4.5 Studio menu hide + orphan cleanup
   - 4.6 Dynamic C01 report inheritance
5. [Models & fields](#5-models--fields)
6. [Views](#6-views)
7. [Seed / migration functions](#7-seed--migration-functions)
8. [How it's used by Fix-repair](#8-how-its-used-by-fix-repair)
9. [Development notes](#9-development-notes)

---

## 1. Scope

**In scope:**

- `sale.order` — Document Introduction / Conclusion selectors and text
  fields on every quotation
- `res.partner` — Reference field UX
- `res.config.settings` — Sales Configurations block with four
  per-company values that Fix-repair also reads
- The `x_minimum_sales_margin` Studio catalogue — this module is the
  authoritative writer of the four config values it carries
- C01 Sales Quotation QWeb report — Intro / Conclusion overlay
  attached dynamically at install/upgrade time (portable across
  databases with different Studio state)

**Out of scope:**

- Helpdesk-repair, project.task-repair, stock.picking (that's
  Fix-repair)
- HR, Accounting, Purchase, Inventory workflows
- Studio artefacts on other models

## 2. Runtime dependencies

```python
'depends': [
    'base_setup',
    'sale',
    'sale_stock',
],
```

Deliberately minimal. Fix-repair depends on **this** module (not the
other way around), so BugFix-Sales stays free of any helpdesk dependency.

## 3. Module layout

```
BugFix-Sales/
├── __manifest__.py
├── __init__.py
│
├── models/
│   ├── __init__.py
│   ├── doc_intro.py                # bugfix_sales.doc.intro model
│   ├── doc_conclusion.py           # bugfix_sales.doc.conclusion model
│   ├── minimum_sales_margin_seed.py # AbstractModel; per-company seed
│   │                                 + Studio menu hide + orphan
│   │                                 pin cleanup + C01 inheritance
│   ├── res_config_settings.py      # Sales Configurations block —
│   │                                 four fields passthrough to
│   │                                 x_minimum_sales_margin row
│   └── sale_order.py               # bugfix_sales_intro_id/text +
│                                     bugfix_sales_conclusion_id/text
│
├── views/
│   ├── doc_intro_views.xml         # doc.intro CRUD form + tree
│   ├── doc_conclusion_views.xml    # doc.conclusion CRUD form + tree
│   ├── res_partner_views.xml       # Reference field position override
│   ├── res_config_settings_views.xml # Sales Configurations block
│   └── sale_order_views.xml        # Header selectors + Document Text tab
│
├── security/
│   └── ir.model.access.csv         # doc_intro / doc_conclusion access rules
│
└── data/
    └── bugfix_sales_data.xml       # <function> calls for all seed /
                                      patch functions (run on every
                                      install and upgrade)
```

## 4. Feature areas

### 4.1 Document Introduction & Conclusion on quotations

Two custom models hold reusable text blocks that the salesperson picks
per-quote:

| Model | What it stores |
|---|---|
| `bugfix_sales.doc.intro` | Reusable "Introduction" text (goes above the items table on printed quotations). Fields: `name`, `description`. |
| `bugfix_sales.doc.conclusion` | Reusable "Conclusion" text (goes after totals). Same fields. |

On every `sale.order`:

- `bugfix_sales_intro_id` — Many2one → `bugfix_sales.doc.intro`
- `bugfix_sales_intro_text` — Text (defaults from the picked intro,
  editable per quote)
- `bugfix_sales_conclusion_id` — Many2one → `bugfix_sales.doc.conclusion`
- `bugfix_sales_conclusion_text` — Text (same pattern)

**Header selectors** (next to `validity_date`) let the salesperson
choose the intro / conclusion; **Document Text tab** lets them tweak
the resulting text before printing.

**Print flow:**

- Standard sale.report_saleorder_document — inheritance lives in
  Fix-repair's `views/sale_report_templates.xml` (the target reports
  are the repair-scope ones)
- C01 Sales Quotation Studio report — inheritance attached
  dynamically by `_attach_c01_intro_conclusion_view` (see 4.6)

### 4.2 Reference field UX on Contact form

The stock `res.partner.ref` field lived deep in Sales & Purchase →
Misc. Moved to the top form header, right above the H1 Contact/Company
name, styled as its own H1 (big + bold, matches the name typography).
Same field, same data — pure view-position change on
`base.view_partner_form`.

File: `views/res_partner_views.xml`.

### 4.3 Sales Configurations moved to Settings

Four per-company values that were previously edited via a Studio-
generated list view:

| Field | Type | Used by |
|---|---|---|
| `x_studio_minimum_sales_margin_` | float, % | Confirm-button margin gate |
| `x_studio_advance_payment_` | float, % | Advance-payment threshold in Fix-repair's payment-register wizard; also gates the delivery Validate button until at least a partial payment lands |
| `x_studio_sales_order_validity` | int, days | Quotation expiry on Confirm gate |
| `x_studio_last_purchase_price_validity_days` | int, days | Last-purchase-price staleness threshold |

Now edited via **Settings → Sales → Sales Configurations**. The Settings
block is a passthrough (fields have the same names as the underlying
`x_minimum_sales_margin` row); `get_values` reads the row for
`self.env.company`, `set_values` writes it back.

**One row per company**, guarded by Studio's automation 146 ("Only one
Minimum Sales Margin % can exist"). Since automation 146 fires on
create only (`on_create_or_write` with `trigger_field=create_date`),
plain UPDATE writes from the Settings page are safe. Fresh-company
INSERT uses raw SQL to bypass the guard (same idiom used in the seed
function below).

Files: `models/res_config_settings.py`, `views/res_config_settings_views.xml`.

### 4.4 Per-company config seeding

`bugfix_sales.minimum_sales_margin.seed._seed_minimum_sales_margin_per_company`
runs on every install / upgrade. Ensures every active `res.company`
has a row on `x_minimum_sales_margin` — creates the missing ones via
raw SQL INSERT (bypasses automation 146's cross-company block).
Idempotent: reruns skip companies that already have a row.

**Default values** for freshly-seeded rows:

| Value | Default |
|---|---|
| Advance Payment % | 50 |
| Minimum Sales Margin % | 35 |
| Sales Order Validity | 1 day |
| Last Purchase Price Validity | 30 days |

Rows can then be edited per-company via the Settings UI.

### 4.5 Studio menu hide + orphan cleanup

Two Studio-generated "Sales Configurations" menus (paths
*Sales → Configuration → Sales Configurations* and
*TEST APP 05 → Sales → Sales Configurations*) opened the list view
of `x_minimum_sales_margin`. Since v17 replaced this UX with the
Settings block, the menus are redundant and confusing (users could
accidentally create a second row, hitting automation 146's guard).

`_hide_minimum_sales_margin_menus` deactivates every menu that opens
a Studio action on `x_minimum_sales_margin`. Reversible: only
`active=False` flips; records preserved.

`_cleanup_orphan_studio_menu_pins` (v19) walks
`ir.model.data` where `module='studio_customization'` and
`model='ir.ui.menu'`, and unlinks any pin whose target menu no longer
exists. Handles the dangling-pin case that emerges when Studio's own
housekeeping deletes menu records after our deactivation.

### 4.6 Dynamic C01 report inheritance

Before v20, the module carried a static XML template that inherited
from a per-database Studio UUID xml_id. This worked on the database
where Studio originally generated the C01 template, but broke module
install on every other DB with `ValueError: External ID not found`.

`_attach_c01_intro_conclusion_view` (v20) resolves the target template
dynamically:

1. Look up `ir.actions.report` where `name = 'C01 Sales Quotation'`
   and `model = 'sale.order'` — the report's human name is stable
   across DBs
2. Read `report_name`, derive the `_document` sub-template's key by
   inserting `_document` at the `_copy` boundary in the Studio naming
   convention
3. Look up the `ir.ui.view` with that key
4. Create or update the inheritance view under
   `bugfix_sales.bugfix_sales_c01_quotation_intro_conclusion`

**Absent-target behaviour:** if C01 doesn't exist on the current
database, the method skips silently. Module installs cleanly;
enhancement stays dormant.

## 5. Models & fields

### 5.1 `bugfix_sales.doc.intro` (`models/doc_intro.py`)

New model. Fields:

- `name` — Char (display label in dropdowns)
- `description` — Text (the actual body that flows into the printed intro)

### 5.2 `bugfix_sales.doc.conclusion` (`models/doc_conclusion.py`)

New model, same shape as `doc.intro` — reusable text blocks for the
"Conclusion" section of quotations.

### 5.3 `sale.order` extensions (`models/sale_order.py`)

Four native fields on every SO:

- `bugfix_sales_intro_id` — Many2one → `bugfix_sales.doc.intro`
- `bugfix_sales_intro_text` — Text (default from intro, editable)
- `bugfix_sales_conclusion_id` — Many2one → `bugfix_sales.doc.conclusion`
- `bugfix_sales_conclusion_text` — Text (default from conclusion,
  editable)

### 5.4 `res.config.settings` extensions (`models/res_config_settings.py`)

Four Float / Integer fields that mirror the four
`x_minimum_sales_margin` values by name for straight passthrough:

- `x_studio_minimum_sales_margin_` — Float
- `x_studio_advance_payment_` — Float
- `x_studio_sales_order_validity` — Integer
- `x_studio_last_purchase_price_validity_days` — Integer

`get_values` reads from and `set_values` writes to the
`x_minimum_sales_margin` row for `self.env.company`. No new
persistent columns.

### 5.5 `bugfix_sales.minimum_sales_margin.seed` (`models/minimum_sales_margin_seed.py`)

AbstractModel — no records, just holds four `@api.model` methods
invoked from the data XML:

- `_seed_minimum_sales_margin_per_company` (v16)
- `_hide_minimum_sales_margin_menus` (v18)
- `_cleanup_orphan_studio_menu_pins` (v19)
- `_attach_c01_intro_conclusion_view` (v20)

## 6. Views

| File | Overrides |
|---|---|
| `doc_intro_views.xml` | CRUD list + form for `bugfix_sales.doc.intro`. Sales → Configuration menu entry. |
| `doc_conclusion_views.xml` | Same for `bugfix_sales.doc.conclusion`. |
| `sale_order_views.xml` | Inherits `sale.view_order_form`. Adds intro/conclusion Many2ones next to validity_date; adds "Document Text" notebook page hosting the two textareas. |
| `res_partner_views.xml` | Inherits `base.view_partner_form`. Removes `ref` from Sales & Purchase → Misc group; re-adds it above the H1 name, wrapped in its own H1 for big/bold styling. |
| `res_config_settings_views.xml` | Inherits `sale.res_config_settings_view_form`. Adds a "Sales Configurations" block inside the Sales app with four settings. |

## 7. Seed / migration functions

Every function is registered in `data/bugfix_sales_data.xml` and
runs on every install / upgrade. All are idempotent — reruns find no
work and no-op.

| Function | Purpose |
|---|---|
| `_seed_minimum_sales_margin_per_company` | Ensure one row per active company on `x_minimum_sales_margin` — creates missing rows via raw SQL INSERT (bypasses automation 146). |
| `_hide_minimum_sales_margin_menus` | Deactivate the two Studio-generated menus that opened the list view (redundant after Settings block). |
| `_cleanup_orphan_studio_menu_pins` | Unlink `ir.model.data` pins under `studio_customization` on `ir.ui.menu` whose target no longer exists. |
| `_attach_c01_intro_conclusion_view` | Look up the Studio C01 Sales Quotation report by name; derive the `_document` sub-template key; create the inheritance view. Skips silently when C01 isn't present on the current DB. |

## 8. How it's used by Fix-repair

The two modules cooperate via three surfaces:

1. **Manifest dependency** — Fix-repair's `depends` list includes
   `BugFix-Sales`. Upgrade order is enforced by Odoo.

2. **Shared config storage** — Fix-repair's threshold checks read
   `env['x_minimum_sales_margin'].search([...], limit=1)` scoped by
   `company_id`. BugFix-Sales owns the write path (Settings block +
   seed function); Fix-repair owns the read path (payment-register
   wizard, delivery-Validate gate).

3. **Shared report inheritance** — Fix-repair's
   `views/sale_report_templates.xml` and BugFix-Sales's
   `_attach_c01_intro_conclusion_view` both hook the
   Introduction / Conclusion overlay onto their respective report
   templates. Fix-repair covers the helpdesk-repair reports; BugFix-Sales
   covers the plain sales-quotation C01 report.

## 9. Development notes

- **Idempotence-first** — every seed/patch function is designed for
  repeated re-execution. Existing rows / menus / views are inspected
  before any write; no-op when the desired state is already in place.
- **Raw SQL bypasses** are used deliberately to sidestep Studio's
  automation 146 (which enforces "one row per install" across
  companies). Every use is called out with a comment.
- **Portable across DBs** — no hardcoded Studio UUIDs (v20 removed the
  last one on the C01 report inheritance). The module installs
  cleanly on any Odoo instance whether or not the Studio C01 report
  exists there.
- **No new persistent columns on shared models** — Sales Configurations
  is a Settings-only field cluster that passes through to the existing
  `x_minimum_sales_margin` row.

For a runtime verification of Fix-repair's Studio → Python migration
that touches shared surfaces (advance-payment threshold, delivery
gate), run the audit test in the companion Playwright repo:

```bash
cd "D:\Odoo Playwright Tests\PlayWrite Testings"
npm run audit
```

Produces an HTML report at
`studio-migration-audit-output/report.html`.
