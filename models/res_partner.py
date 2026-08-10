# -*- coding: utf-8 -*-
"""Customer-master Studio fields ported into BugFix-Sales.

These fields were originally created by Odoo Studio on res.partner
and were owned by the studio_customization module (state='manual').
The Jul 2026 migration flipped their state to 'base' and repinned
their ir.model.data rows to Fix-repair via raw SQL, but no Python
declaration existed anywhere — meaning a fresh module install on a
clean DB would not recreate them.

This file declares them under BugFix-Sales so that:
  1. On the current SH DB (where they already exist), the Python
     declaration takes over ownership on next module upgrade — same
     shape, same values.
  2. On a fresh DB install, the fields are actually created by
     Odoo's ORM at BugFix-Sales install time, not just left as
     dangling metadata.

These are all consumed by sale.order via `related=partner_id.x_...`
declarations in sale_order.py; declaring them here first guarantees
the related fields resolve.
"""
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_studio_bank_guarantee_amount = fields.Float(
        string='Bank Guarantee Amount',
    )
    x_studio_expiry_date = fields.Date(
        string='Bank Guarantee Expiration Date',
    )
    x_studio_payment_method = fields.Selection(
        [('Cash', 'Cash'), ('Credit', 'Credit')],
        string='Payment Type',
    )
    x_studio_valid_bank_guarantee = fields.Boolean(
        string='Valid Bank Guarantee',
        help=(
            "True when the partner has an active bank guarantee "
            "(x_studio_expiry_date in the future). Used by sale.order "
            "credit-limit gates via a related field."
        ),
    )
