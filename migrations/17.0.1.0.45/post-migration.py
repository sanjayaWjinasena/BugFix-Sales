# -*- coding: utf-8 -*-
"""v45 upgrade -- declare two Studio fields on account.payment
required by Fix-repair v284's port of Studio automation 241
(RR - Validate Payment %):

  * x_studio_sales_order   (Many2one -> sale.order)
  * x_studio_quotation_type (Selection: Sales / Project / Repair)

These live in BugFix-Sales as the semantic home for x_studio_
sales fields (already owns x_studio_quotation_type on sale.order
+ sale.order.line). No data migration required -- fresh columns.

Broader account.payment Studio schema (9 other fields on Clear-DB)
belongs to the deferred BugFix-Accounting module (task #197) and
is intentionally NOT ported here.
"""


def migrate(cr, version):
    if not version:
        return
    return
