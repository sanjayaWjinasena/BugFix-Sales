# BugFix-Sales — `x_delivery_terms`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_delivery_terms` — Delivery Terms

*Created by this repo.* Python: `models/x_delivery_terms.py`.

Other repos that use this model: `access right BugFix-Purchase.access_1249_delivery_terms_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1250_delivery_terms_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_x_delivery_terms_user` (BugFix-Purchase)<br>`purchase.order.line.x_studio_delivery_term` (BugFix-Purchase)<br>`purchase.order.x_studio_delivery_term` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_568_jin_multi_company_delivery_terms` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_f7_x_delivery_terms_jin_multi_company_delivery_terms` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<details><summary>+10 more</summary>`server action BugFix-Purchase.server_action_2682_jin_company_id_in_delivery_terms` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase` (BugFix-Stock)<br>`window action BugFix-Purchase.action_1205_delivery_terms` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2060_delivery_terms` (BugFix-Purchase)<br>`x_con_consolidated_lin.x_studio_delivery_term` (BugFix-Purchase)<br>`x_consignment_header.x_studio_delivery_term` (BugFix-Purchase)<br>`x_delivery_term_charge.x_studio_delivery_terms_id` (BugFix-Purchase)<br>`x_temp_con_conso_line.x_studio_delivery_term` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_delivery_terms -->
A Delivery Term is a named shipping or delivery condition, with a description, sequence, company, Vendor Despatch flag and archive flag. Purchase orders and their lines in BugFix-Purchase use it. Buttons copy a charge line onto the term for every Misc Charge Code in the Charges group, or clear those charges, and an automation sets the term's company to the user's current company.
<!-- /SUMMARY -->

**Fields (37):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; warning=Alert; danger=Error; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_delivery_terms.activity_summary`<br>`x_delivery_terms.activity_type_icon`<br>`x_delivery_terms.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; overdue=Overdue; today=Today; today=Today; planned=Planned; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_delivery_terms.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_delivery_terms.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_delivery_terms.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  | `automation BugFix-Sales.base_automation_316_jin_company_id_in_delivery_terms` |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) |  |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) |  |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of a delivery term (default active); archived terms are hidden. | default `True`; stored |  | `default BugFix-Purchase.default_127_x_delivery_terms_x_active` (BugFix-Purchase)<br>`view BugFix-Purchase.ported_view_2714_customization_x_delivery_terms_form` (BugFix-Purchase)<br>`view BugFix-Sales.ported_default_form_view_fo_ccd4306a_1ac9_43c7_847f_965bdab82885`<br>`view BugFix-Sales.ported_default_search_view__f98a2314_f551_4142_ba32_a74bde2e40fe` |
| `x_name` | Delivery Term | char | Name of the delivery term (e.g. shipping term), shown in its views and used by the 'IMP Copy Charges to Delivery Terms' action. | stored; required |  | `server action BugFix-Sales.server_action_1207_imp_copy_charges_to_delivery_terms`<br>`view BugFix-Sales.ported_default_form_view_fo_ccd4306a_1ac9_43c7_847f_965bdab82885`<br>`view BugFix-Sales.ported_default_list_view_fo_35abcb0b_2581_4156_9e23_d75bfb8d6b5e`<br>`view BugFix-Sales.ported_default_search_view__f98a2314_f551_4142_ba32_a74bde2e40fe` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company owning the delivery term; set by the 'JIN company id in delivery terms' actions and used by multi-company record rules. | stored | `model res.company` (base) | `record rule BugFix-Purchase.rule_568_jin_multi_company_delivery_terms` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_f7_x_delivery_terms_jin_multi_company_delivery_terms` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2682_jin_company_id_in_delivery_terms` (BugFix-Purchase)<br>`server action BugFix-Sales.server_action_2682_jin_company_id_in_delivery_terms`<br>`view BugFix-Purchase.ported_view_2714_customization_x_delivery_terms_form` (BugFix-Purchase)<details><summary>+1 more</summary>`view BugFix-Purchase.ported_view_2719_customization_x_delivery_terms_tree` (BugFix-Purchase)</details> |
| `x_studio_copied` | Copied | boolean | Marks that charges have been copied to the delivery term; set and cleared by the IMP Copy/Clear Charges actions. | stored |  | `server action BugFix-Sales.server_action_1207_imp_copy_charges_to_delivery_terms`<br>`server action BugFix-Sales.server_action_1208_imp_clear_charges_from_delivery_terms`<br>`view BugFix-Purchase.ported_view_2714_customization_x_delivery_terms_form` (BugFix-Purchase) |
| `x_studio_description` | Description | char | Description of the delivery term; shown in its form and list and used by 'IMP Copy Charges to Delivery Terms'. | stored |  | `server action BugFix-Sales.server_action_1207_imp_copy_charges_to_delivery_terms`<br>`view BugFix-Purchase.ported_view_2714_customization_x_delivery_terms_form` (BugFix-Purchase)<br>`view BugFix-Purchase.ported_view_2719_customization_x_delivery_terms_tree` (BugFix-Purchase) |
| `x_studio_sequence` | Sequence | integer | Integer sort order for Delivery Terms records (has a default value); shown in the Delivery Terms form and the default list view used to order entries. | stored |  | `default BugFix-Purchase.default_128_x_delivery_terms_x_studio_sequence` (BugFix-Purchase)<br>`view BugFix-Sales.ported_default_list_view_fo_35abcb0b_2581_4156_9e23_d75bfb8d6b5e` |
| `x_studio_vendor_despatch` | Vendor Despatch | boolean | Checkbox on a Delivery Terms record marking it as a vendor-despatch term; entered by the user and shown on the Delivery Terms form and list views. | stored |  | `view BugFix-Purchase.ported_view_2714_customization_x_delivery_terms_form` (BugFix-Purchase)<br>`view BugFix-Purchase.ported_view_2719_customization_x_delivery_terms_tree` (BugFix-Purchase) |

**Server actions (3):**

- **IMP - Clear Charges from Delivery Terms** (`server_action_1208_imp_clear_charges_from_delivery_terms`, type `code`)
  - Function: Deletes all charge lines linked to the Delivery Terms record and clears its Copied flag.
  - Depends on: `model x_delivery_term_charge` (BugFix-Purchase), `model x_delivery_terms`, `x_delivery_terms.x_studio_copied`, `x_delivery_terms.x_studio_delivery_terms_id` (BugFix-Purchase)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (7 lines)</summary>

```python
if record.id:
  temp_rec = env['x_delivery_term_charge'].search([('x_studio_delivery_terms_id', '=', record.id)])
  if temp_rec:
    for del_temp_rec in temp_rec:
      del_temp_rec.unlink()   

  record['x_studio_copied'] = False
```
  </details>
- **IMP - Copy Charges to Delivery Terms** (`server_action_1207_imp_copy_charges_to_delivery_terms`, type `code`)
  - Function: Creates a delivery-term charge line on the Delivery Terms record for every Misc Charge Code in group 'Charges', then sets Copied. Can create duplicates if run twice.
  - Depends on: `model x_delivery_term_charge` (BugFix-Purchase), `model x_delivery_terms`, `model x_misc_charge_codes` (BugFix-Stock), `x_delivery_terms.x_name`, `x_delivery_terms.x_studio_copied`<details><summary>+2 more</summary>`x_delivery_terms.x_studio_delivery_terms_id` (BugFix-Purchase), `x_delivery_terms.x_studio_description`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (6 lines)</summary>

```python
loop_misc_charge_codes_c = env['x_misc_charge_codes'].search([('x_studio_charge_group', '=', 'Charges')])
if loop_misc_charge_codes_c:
  for find_charges in loop_misc_charge_codes_c:
    create_delivery_charges = env['x_delivery_term_charge'].create({'x_studio_delivery_terms_id':record.id,'x_name':find_charges.x_name,'x_studio_description':find_charges.x_studio_description})
  
  record['x_studio_copied'] = True
```
  </details>
- **JIN - Company Id in Delivery Terms** (`server_action_2682_jin_company_id_in_delivery_terms`, type `code`)
  - Function: Sets the Delivery Terms record's Company to the user's currently selected company.
  - Depends on: `model res.company` (base), `model x_delivery_terms`, `x_delivery_terms.x_studio_company_id`
  - Used by: `automation BugFix-Sales.base_automation_316_jin_company_id_in_delivery_terms`
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Delivery Terms | `base_automation_316_jin_company_id_in_delivery_terms` |  | When a record is created or updated on Delivery Terms, runs _JIN - Company Id in Delivery Terms_. | `model x_delivery_terms`<br>`server action BugFix-Sales.server_action_2682_jin_company_id_in_delivery_terms`<br>`x_delivery_terms.create_date` |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Delivery Terms | `act_window_1205_delivery_terms` | Opens **Delivery Terms** records (tree,form). | `model x_delivery_terms` |  |
| Delivery Terms | `act_window_2060_delivery_terms` | Opens **Delivery Terms** records (tree,form). | `model x_delivery_terms` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_imports_configurations_delivery_terms` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_setups_delivery_terms` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_01_imports_configuration_delivery_terms` (BugFix-Studio-Misc) |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_delivery_terms | `ported_default_form_view_fo_ccd4306a_1ac9_43c7_847f_965bdab82885` | form | full form layout with 2 fields | Form view for Delivery Terms records: name and an Archived ribbon when the record is inactive. | `x_delivery_terms.x_active`<br>`x_delivery_terms.x_name` | `view BugFix-Purchase.ported_view_2714_customization_x_delivery_terms_form` (BugFix-Purchase) |
| Default list view for x_delivery_terms | `ported_default_list_view_fo_35abcb0b_2581_4156_9e23_d75bfb8d6b5e` | tree | full tree layout with 2 fields | List view for Delivery Terms with a drag handle for ordering and the name. | `x_delivery_terms.x_name`<br>`x_delivery_terms.x_studio_sequence` | `view BugFix-Purchase.ported_view_2719_customization_x_delivery_terms_tree` (BugFix-Purchase) |
| Default search view for x_delivery_terms | `ported_default_search_view__f98a2314_f551_4142_ba32_a74bde2e40fe` | search | full search layout with 1 fields | Search view for Delivery Terms: search by name and an Archived filter. | `x_delivery_terms.x_active`<br>`x_delivery_terms.x_name` |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_delivery_terms user access | `access_x_delivery_terms_user` | Gives **User types / Internal User** read/write/create/delete access to Delivery Terms records. | `group base.group_user` (base)<br>`model x_delivery_terms` |  |
