# BugFix-Sales — `sale.advance.payment.inv`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `sale.advance.payment.inv` — Sales Advance Payment Invoice

*Extends a model created by `sale`.* Python: `models/sale_advance_payment_inv.py`.

**Summary:**

<!-- SUMMARY:model:sale.advance.payment.inv -->
This repo adds a computed flag to the Create Invoice wizard that is true when every selected order has Quotation Type Sales. For such orders the wizard defaults to a regular invoice and the invoicing method is read-only, so down-payment invoices cannot be created for plain sales orders.
<!-- /SUMMARY -->

**Fields (1):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `bugfix_sales_only_regular` | Bugfix Sales Only Regular | boolean | On the Create Invoice wizard: computed True when all selected orders are plain 'Sales' quotations; used by the wizard view to adapt the invoicing options. | computed by `_compute_bugfix_sales_only_regular`; not stored | `sale.advance.payment.inv._compute_bugfix_sales_only_regular()` | `view BugFix-Sales.view_sale_advance_payment_inv_bugfix_sales` |

**Python methods (2):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_bugfix_sales_only_regular` | Computes the wizard flag 'only regular' which is True when every selected sales order has quotation type 'Sales'; used to lock the Create Invoice wizard to Regular invoice. | api.depends('sale_order_ids') |  | `sale.advance.payment.inv.sale_order_ids` (sale) | `sale.advance.payment.inv.bugfix_sales_only_regular` | `models/sale_advance_payment_inv.py:37` |
| `default_get` | Override of the Create Invoice wizard defaults: when all selected sales orders are of quotation type 'Sales', forces the invoice method to Regular invoice ('delivered'), overriding any down-payment default passed in context. | api.model | yes | `model sale.order` (sale) |  | `models/sale_advance_payment_inv.py:46` |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| sale.advance.payment.inv.form.bugfix_sales | `view_sale_advance_payment_inv_bugfix_sales` | form | before `//field[@name='advance_payment_method']`: add field bugfix_sales_only_regular; set readonly=bugfix_sales_only_regular on `//field[@name='advance_payment_method']` | Create Invoice wizard: makes the invoicing method (regular / down payment) read-only when the hidden flag `bugfix_sales_only_regular` is set, forcing a regular invoice. | `sale.advance.payment.inv.bugfix_sales_only_regular`<br>`view sale.view_sale_advance_payment_inv` (sale) |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| sale.advance.payment.inv | `access_6864_sale_advance_payment_inv` | Gives **Sales / Jin - Sales - POS Users** read/write/create access to Sales Advance Payment Invoice records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model sale.advance.payment.inv` (sale) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Advance Payment Invoice Rule | `rule_179_sales_advance_payment_invoice_rule` | For everyone (global rule): read/write/create/delete on Sales Advance Payment Invoice only where `[('create_uid', '=', user.id)]`. | `model sale.advance.payment.inv` (sale) |  |
