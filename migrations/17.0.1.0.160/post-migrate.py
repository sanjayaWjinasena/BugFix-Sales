# -*- coding: utf-8 -*-
"""BugFix-Sales v17.0.1.0.160: seed ir.model.fields.selection rows via ORM.

Same content as post_init_hook in ../hooks.py; this covers the version-upgrade
path (post-migrate runs on upgrade; hooks.py runs on fresh install). Uses the
ORM (no direct SQL) per the project's no-direct-SQL rule.

Idempotent: skips rows whose (field_id, value) already exists.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

_FIELD_SELECTIONS = [
    ('sale.order.line', 'x_studio_quotation_type', 'Sales', 'Sales', 10),
    ('sale.order.line', 'x_studio_product_status', 'Blank', 'Blank', 10),
    ('sale.order.line', 'x_studio_purch_type', 'Local', 'Local', 10),
    ('sale.order.line', 'x_studio_quotation_type', 'Project', 'Project', 1),
    ('sale.order.line', 'x_studio_product_status', 'New Item', 'New Item', 1),
    ('sale.order.line', 'x_studio_purch_type', 'Import', 'Import', 1),
    ('sale.order.line', 'x_studio_quotation_type', 'Repair', 'Repair', 2),
    ('sale.order.line', 'x_studio_product_status', 'Existing Item', 'Existing Item', 2),
]


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Fld = env['ir.model.fields']
    Sel = env['ir.model.fields.selection']
    for model, fname, value, label, seq in _FIELD_SELECTIONS:
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            continue
        exists = Sel.search(
            [('field_id', '=', fld.id), ('value', '=', value)], limit=1,
        )
        if exists:
            continue
        try:
            with cr.savepoint():
                Sel.create({
                    'field_id': fld.id, 'value': value,
                    'name': label, 'sequence': seq,
                })
        except Exception as e:
            _logger.warning(
                "BugFix-Sales v17.0.1.0.160: seed failed %s.%s=%r (%s).",
                model, fname, value, e,
            )
