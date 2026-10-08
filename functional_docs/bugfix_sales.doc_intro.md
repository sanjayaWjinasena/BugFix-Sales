# BugFix-Sales — `bugfix_sales.doc_intro`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `bugfix_sales.doc_intro` — Quotation Document Introduction

*Created by this repo.* Python: `models/doc_intro.py`.

**Summary:**

<!-- SUMMARY:model:bugfix_sales.doc_intro -->
A Document Introduction is a reusable opening text for printed quotations, with a title, the introduction text, a company and an archive flag. Users maintain them under Sales, Configuration, Document Introductions. When one is chosen on a sales order, its text is copied into the order's editable Introduction field, which is printed at the top of the quotation.
<!-- /SUMMARY -->

**Fields (10):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `active` | Active | boolean | Archive flag for the introduction template (default active); archived templates are hidden from selection. | default `True`; stored |  | `view BugFix-Sales.view_doc_intro_form` |
| `company_id` | Company | many2one → `res.company` | Company owning the introduction template; defaults to the current company. | default `lambda self: self.env.company`; stored | `model res.company` (base) | `view BugFix-Sales.view_doc_intro_form`<br>`view BugFix-Sales.view_doc_intro_tree` |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `description` | Introduction Text | text | Multi-line introduction text printed at the top of the quotation; copied into the sales order's Introduction when the template is chosen. | stored; required |  | `view BugFix-Sales.view_doc_intro_form` |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `name` | Title | char | Title of a reusable quotation introduction template, shown in its list and form. | stored; required |  | `view BugFix-Sales.view_doc_intro_form`<br>`view BugFix-Sales.view_doc_intro_tree` |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Document Introductions | `action_doc_intro` | Opens **Quotation Document Introduction** records (tree,form). | `model bugfix_sales.doc_intro` | `menu BugFix-Sales.menu_doc_intro` |
| Document Introductions | `act_window_3635_document_introductions` | Opens **Quotation Document Introduction** records (tree,form). | `model bugfix_sales.doc_intro` | `menu BugFix-Sales.menu_f6_document_introductions` |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| bugfix_sales.doc_intro.form | `view_doc_intro_form` | form | full form layout with 4 fields | Form view for a Document Introduction: title, company (multi-company only) and the multi-line introduction text printed at the top of the quotation. | `bugfix_sales.doc_intro.active`<br>`bugfix_sales.doc_intro.company_id`<br>`bugfix_sales.doc_intro.description`<br>`bugfix_sales.doc_intro.name`<br>`group base.group_multi_company` (base) |  |
| bugfix_sales.doc_intro.tree | `view_doc_intro_tree` | tree | full tree layout with 2 fields | List view of Document Introductions (quotation intro texts) showing the title and, for multi-company users, an optional Company column. | `bugfix_sales.doc_intro.company_id`<br>`bugfix_sales.doc_intro.name`<br>`group base.group_multi_company` (base) |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| bugfix_sales.doc_intro manager | `access_8711_bugfix_sales_doc_intro_manager` | Gives **Sales / Administrator** read/write/create/delete access to Quotation Document Introduction records. | `group sales_team.group_sale_manager` (sales_team)<br>`model bugfix_sales.doc_intro` |  |
| bugfix_sales.doc_intro user | `access_8710_bugfix_sales_doc_intro_user` | Gives **Sales / User: Own Documents Only** read access to Quotation Document Introduction records. | `group sales_team.group_sale_salesman` (sales_team)<br>`model bugfix_sales.doc_intro` |  |
