# BugFix-Sales — `minimum_sales_margin`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `minimum_sales_margin` — Minimum Sales Margin %

*Created by this repo.* Python: `models/minimum_sales_margin.py`, `models/x_minimum_sales_margin_gap.py`. Record name field: `name`.

**Summary:**

<!-- SUMMARY:model:minimum_sales_margin -->
A Minimum Sales Margin % record holds a company's sales configuration: minimum sales margin %, advance payment %, sales order validity days and last purchase price validity days. An automation allows only one active record. These values are now edited in Settings and stored per company in system parameters; this model is kept as the legacy source, and its menus are archived on upgrade.
<!-- /SUMMARY -->

**Fields (39):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Sales.view_minimum_sales_margin_form`<br>`minimum_sales_margin.activity_summary`<br>`minimum_sales_margin.activity_type_icon`<br>`minimum_sales_margin.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`minimum_sales_margin.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`minimum_sales_margin.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`minimum_sales_margin.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Sales.view_minimum_sales_margin_form` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Sales.view_minimum_sales_margin_form` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Standard active/archive flag of a Minimum Sales Margin % record (defaults on); used by the default form and search views to archive or filter records. | stored |  | `default BugFix-Sales.default_minimum_sales_margin_active`<br>`view BugFix-Sales.view_minimum_sales_margin_form`<br>`view BugFix-Sales.view_minimum_sales_margin_search` |
| `name` | Name | char | Name/description of the Minimum Sales Margin % configuration record; shown in its default list, form and search views. | stored |  | `view BugFix-Sales.view_minimum_sales_margin_list`<br>`view BugFix-Sales.view_minimum_sales_margin_form`<br>`view BugFix-Sales.view_minimum_sales_margin_search` |
| `accounting_active` | Active | boolean | Flag marking this Minimum Sales Margin % record as the single active configuration; set to True by the 'SLS - Minimum Sales Margin % - in Setup Page' action, which blocks creating a second active record. | stored |  | `server action BugFix-Sales.action_minimum_sales_margin_sls_minimum_sales_margin_in_setup_page`<br>`server action BugFix-Sales.action_sls_minimum_sales_margin_in_setup_page`<br>`view BugFix-Sales.view_default_list_view_for_minimum_sales_margin_inherit` |
| `advance_payment_` | Advance Payment % | float | Advance payment percentage configured for sales; entered on the Minimum Sales Margin % form. Legacy store now superseded by per-company Settings values in ir.config_parameter. | stored |  | `view BugFix-Sales.view_default_form_view_for_minimum_sales_margin_inherit` |
| `accounting_company_id` | Company | many2one → `res.company` | Company the margin configuration row belongs to; used by the multi-company record rule to restrict visibility and shown in the form and list views. | stored | `model res.company` (base) | `record rule BugFix-Sales.rule_jin_multi_company_minimum_sales_margin`<br>`view BugFix-Sales.view_default_form_view_for_minimum_sales_margin_inherit`<br>`view BugFix-Sales.view_default_list_view_for_minimum_sales_margin_inherit` |
| `last_purchase_price_validity_days` | Last Purchase Price Validity (Days) | integer | Number of days a product's last purchase price is considered valid (has a default); entered on the Minimum Sales Margin % form. Legacy store superseded by per-company Settings values. | stored |  | `default BugFix-Sales.default_581_x_minimum_sales_margin_x_studio_last_purchase_pr`<br>`view BugFix-Sales.view_default_form_view_for_minimum_sales_margin_inherit` |
| `minimum_sales_margin_` | Minimum Sales Margin % | float | Minimum allowed sales margin percentage used as the threshold for margin checks on sales order lines; entered on the configuration form and list. Legacy store superseded by per-company Settings values. | stored |  | `view BugFix-Sales.view_default_form_view_for_minimum_sales_margin_inherit`<br>`view BugFix-Sales.view_default_list_view_for_minimum_sales_margin_inherit` |
| `sales_order_validity` | Sales Order Validity (Days) | integer | Number of days a sales order/quotation stays valid (has a default); entered on the Minimum Sales Margin % form. Legacy store superseded by per-company Settings values. | stored |  | `default BugFix-Sales.default_minimum_sales_margin_sales_order_vali`<br>`view BugFix-Sales.view_default_form_view_for_minimum_sales_margin_inherit` |
| `sequence` | Sequence | integer | Integer sort order for Minimum Sales Margin % records (has a default); used in the default list view. | stored |  | `default BugFix-Sales.default_minimum_sales_margin_sequence`<br>`view BugFix-Sales.view_minimum_sales_margin_list` |

**Server actions (2):**

- **Execute Code** (`action_sls_minimum_sales_margin_in_setup_page`, type `code`)
  - Function: Run by an automation on the Minimum Sales Margin setup record: raises 'Only one Minimum Sales Margin % can exist.' if an active record already exists, otherwise marks this record active.
  - Depends on: `model minimum_sales_margin`, `minimum_sales_margin.accounting_active`
  - Used by: `automation BugFix-Sales.automation_sls_minimum_sales_margin_in_setup_page`
  <details><summary>code (7 lines)</summary>

```python
if record.id:
    update = env["minimum_sales_margin"].search(
        [("accounting_active", "=", True)], limit=1
    )
    if update:
        raise UserError("Only one Minimum Sales Margin % can exist.")
    else:
        record["accounting_active"] = True
```
  </details>
- **SLS - Minimum Sales Margin % - in Setup Page** (`action_minimum_sales_margin_sls_minimum_sales_margin_in_setup_page`, type `code`)
  - Function: On a Minimum Sales Margin % record, raises an error if another active record already exists ('Only one Minimum Sales Margin % can exist'); otherwise marks this record active.
  - Depends on: `model minimum_sales_margin`, `minimum_sales_margin.accounting_active`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (6 lines)</summary>

```python
if record.id:
    update = env["minimum_sales_margin"].search(
        [("accounting_active", "=", True)], limit=1
    )
    if update:
        raise UserError("Only one Minimum Sales Margin % can exist.")
    else:
        record["accounting_active"] = True
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| SLS - Minimum Sales Margin % - in Setup Page | `automation_sls_minimum_sales_margin_in_setup_page` |  | When a record is created or updated on Minimum Sales Margin %, runs _Execute Code_. | `model minimum_sales_margin`<br>`server action BugFix-Sales.action_sls_minimum_sales_margin_in_setup_page` |  |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Configurations | `action_sales_configurations` | Opens **Minimum Sales Margin %** records (tree,form). | `model minimum_sales_margin` | `menu BugFix-Sales.menu_sales_configurations`<br>`menu BugFix-Studio-Misc.menu_sales_configuration_sales_configurations` (BugFix-Studio-Misc) |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for minimum_sales_margin | `view_minimum_sales_margin_form` | form | full form layout with 5 fields | Base form view for the Minimum Sales Margin setup record: name, Archived ribbon and chatter; fields are added by a child customization view. | `minimum_sales_margin.activity_ids`<br>`minimum_sales_margin.message_follower_ids`<br>`minimum_sales_margin.message_ids`<br>`minimum_sales_margin.active`<br>`minimum_sales_margin.name` | `view BugFix-Sales.view_default_form_view_for_minimum_sales_margin_inherit` |
| Default list view for minimum_sales_margin | `view_minimum_sales_margin_list` | tree | full tree layout with 2 fields | Base list view for Minimum Sales Margin setup records with a drag handle and name. | `minimum_sales_margin.name`<br>`minimum_sales_margin.sequence` | `view BugFix-Sales.view_default_list_view_for_minimum_sales_margin_inherit` |
| Default search view for minimum_sales_margin | `view_minimum_sales_margin_search` | search | full search layout with 1 fields | Search view for Minimum Sales Margin records: search by name and an Archived filter. | `minimum_sales_margin.active`<br>`minimum_sales_margin.name` |  |
| Odoo Studio: Default form view for minimum_sales_margin customization | `view_default_form_view_for_minimum_sales_margin_inherit` | form | inside `//group[@name='studio_group_457e75_left']`: add field minimum_sales_margin_, field advance_payment_; inside `//group[@name='studio_group_457e75_right']`: add field sales_order_validity, field last_purchase_price_validity_days, field accounting_company_id | Minimum Sales Margin form: adds Minimum Sales Margin %, Advance Payment %, Sales Order Validity (Days), Last Purchase Price Validity (Days) and Company. | `view BugFix-Sales.view_minimum_sales_margin_form`<br>`minimum_sales_margin.advance_payment_`<br>`minimum_sales_margin.accounting_company_id`<br>`minimum_sales_margin.last_purchase_price_validity_days`<br>`minimum_sales_margin.minimum_sales_margin_`<details><summary>+1 more</summary>`minimum_sales_margin.sales_order_validity`</details> |  |
| Odoo Studio: Default list view for minimum_sales_margin customization | `view_default_list_view_for_minimum_sales_margin_inherit` | tree | set create=false, delete=false on `//tree[1]`; set column_invisible=1 on `//field[@name='sequence']`; after `//field[@name='name']`: add field accounting_company_id, field id, field minimum_sales_margin_, field accounting_active | Minimum Sales Margin list: disables create and delete, hides the sequence handle and adds Company and ID columns (margin and active as hidden columns). | `view BugFix-Sales.view_minimum_sales_margin_list`<br>`minimum_sales_margin.accounting_active`<br>`minimum_sales_margin.accounting_company_id`<br>`minimum_sales_margin.minimum_sales_margin_` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Minimum Sales Margin % group_system | `access_minimum_sales_margin_group_system` | Gives **Administration / Settings** read/write/create/delete access to Minimum Sales Margin % records. | `group base.group_system` (base)<br>`model minimum_sales_margin` |  |
| Minimum Sales Margin % group_user | `access_minimum_sales_margin_group_user` | Gives **User types / Internal User** read access to Minimum Sales Margin % records. | `group base.group_user` (base)<br>`model minimum_sales_margin` |  |
| minimum_sales_margin admin | `access_minimum_sales_margin_admin` | Gives **Administration / Settings** read/write/create/delete access to Minimum Sales Margin % records. | `group base.group_system` (base)<br>`model minimum_sales_margin` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Minimum Sales Margin % | `rule_jin_multi_company_minimum_sales_margin` | For everyone (global rule): read/write/create/delete on Minimum Sales Margin % only where `['|', ('accounting_company_id', 'in', company_ids), ('accounting_company_id', '=', False)]`. | `model minimum_sales_margin`<br>`minimum_sales_margin.accounting_company_id` |  |
