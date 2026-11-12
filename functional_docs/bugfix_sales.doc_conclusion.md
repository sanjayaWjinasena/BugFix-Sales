# BugFix-Sales — `bugfix_sales.doc_conclusion`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `bugfix_sales.doc_conclusion` — Quotation Document Conclusion

*Created by this repo.* Python: `models/doc_conclusion.py`.

**Summary:**

<!-- SUMMARY:model:bugfix_sales.doc_conclusion -->
A Document Conclusion is a reusable closing text for printed quotations, with a title, the conclusion text, a company and an archive flag. Users maintain them under Sales, Configuration, Document Conclusions. When one is chosen on a sales order, its text is copied into the order's editable Conclusion field, which is printed after the totals on the quotation.
<!-- /SUMMARY -->

**Fields (10):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `active` | Active | boolean | Archive flag for the conclusion template (default active); archived templates are hidden from selection. | default `True`; stored |  | `view BugFix-Sales.view_doc_conclusion_form` |
| `company_id` | Company | many2one → `res.company` | Company owning the conclusion template; defaults to the current company. | default `lambda self: self.env.company`; stored | `model res.company` (base) | `view BugFix-Sales.view_doc_conclusion_form`<br>`view BugFix-Sales.view_doc_conclusion_tree` |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `description` | Conclusion Text | text | Multi-line conclusion text printed after the totals on the quotation; copied into the sales order's Conclusion when the template is chosen. | stored; required |  | `view BugFix-Sales.view_doc_conclusion_form` |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `name` | Title | char | Title of a reusable quotation conclusion template, shown in its list and form. | stored; required |  | `view BugFix-Sales.view_doc_conclusion_form`<br>`view BugFix-Sales.view_doc_conclusion_tree` |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Document Conclusions | `action_doc_conclusion` | Opens **Quotation Document Conclusion** records (tree,form). | `model bugfix_sales.doc_conclusion` | `menu BugFix-Sales.menu_doc_conclusion`<br>`menu BugFix-Sales.menu_f6_document_conclusions` |
| Document Conclusions | `act_window_3636_document_conclusions` | Opens **Quotation Document Conclusion** records (tree,form). | `model bugfix_sales.doc_conclusion` |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| bugfix_sales.doc_conclusion.form | `view_doc_conclusion_form` | form | full form layout with 4 fields | Form view for a Document Conclusion: title, company (multi-company only) and the multi-line conclusion text (availability, payment terms, delivery, guarantee, salutation) printed after the totals. | `bugfix_sales.doc_conclusion.active`<br>`bugfix_sales.doc_conclusion.company_id`<br>`bugfix_sales.doc_conclusion.description`<br>`bugfix_sales.doc_conclusion.name`<br>`group base.group_multi_company` (base) |  |
| bugfix_sales.doc_conclusion.tree | `view_doc_conclusion_tree` | tree | full tree layout with 2 fields | List view of Document Conclusions (quotation closing texts) showing the title and, for multi-company users, an optional Company column. | `bugfix_sales.doc_conclusion.company_id`<br>`bugfix_sales.doc_conclusion.name`<br>`group base.group_multi_company` (base) |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| bugfix_sales.doc_conclusion manager | `access_8713_bugfix_sales_doc_conclusion_manager` | Gives **Sales / Administrator** read/write/create/delete access to Quotation Document Conclusion records. | `group sales_team.group_sale_manager` (sales_team)<br>`model bugfix_sales.doc_conclusion` |  |
| bugfix_sales.doc_conclusion user | `access_8712_bugfix_sales_doc_conclusion_user` | Gives **Sales / User: Own Documents Only** read access to Quotation Document Conclusion records. | `group sales_team.group_sale_salesman` (sales_team)<br>`model bugfix_sales.doc_conclusion` |  |
