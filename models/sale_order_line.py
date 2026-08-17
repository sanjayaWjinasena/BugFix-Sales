# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Ported from Studio (v33). Consumed by BugFix-Sales' account-mandatory
    # gate on the parent sale.order (mirrored per-line).
    x_studio_account_mandatory = fields.Boolean(
        string='Account Mandatory',
    )
    # v43: original line price captured by Fix-repair's RUG-repricing
    # logic (sale_order_line.py's create/write override on Fix-repair
    # v279+). Studio also uses this field to restore the customer-facing
    # price if RUG is later rejected. Declared here so BugFix-Sales
    # owns the schema (single home for sale.order.line Studio fields);
    # Fix-repair reads/writes via the same field name.
    x_studio_price_unit_original = fields.Float(
        string='Price Unit Original',
    )
    # v44: per-line re-estimation marker + instance counter.
    # Written by Fix-repair v283's port of Studio automation 204
    # (RR - Track Lock Status - 3): when a Repair SO is currently
    # unlocked (parent x_studio_unlocked=True) and the user edits a
    # line in the form, x_studio_re_estimated flips to True and
    # x_studio_count_1 is set to (parent.x_studio_re_estimate_count + 1).
    # sale.order-side automations 202/203 read the max x_studio_count_1
    # of re-estimated lines to know the target re-estimate count for
    # the header. Declared here (BugFix-Sales owns line-level Studio
    # schema) so Fix-repair only carries the automation logic.
    x_studio_re_estimated = fields.Boolean(
        string='Re-estimated',
    )
    x_studio_count_1 = fields.Integer(
        string='Re-estimate Instance',
    )
