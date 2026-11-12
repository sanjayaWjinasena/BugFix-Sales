# -*- coding: utf-8 -*-
"""v42 upgrade — force-recompute x_studio_valid_order_lines on every
sale.order after converting it from plain Boolean to stored compute.

Without this recompute, existing SOs keep their pre-v42 value (False
for every SO on dev env since no Studio automation ran there). Repair
SOs stayed unconfirmable because Fix-repair's Confirm invisible
expression fails on `x_studio_valid_order_lines == False`.

Runs the compute directly via ORM recompute for the whole table.
Idempotent.
"""
from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    all_sos = env['sale.order'].sudo().search([])
    all_sos.invalidate_recordset(['x_studio_valid_order_lines'])
    # Access triggers the compute + store.
    for so in all_sos:
        _ = so.x_studio_valid_order_lines
