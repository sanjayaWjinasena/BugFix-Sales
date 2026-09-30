# -*- coding: utf-8 -*-
"""Post-install cleanup hook for BugFix-Sales.

Once the 34 x_studio_* fields ported in v30-v31 have Python declarations
here, the `studio_customization` ir.model.data (xmlid) rows that used to
own them are pure duplicate metadata. This hook removes those redundant
xmlids so `ir.model.fields.modules` no longer reads
"BugFix-Sales, studio_customization" for the ported fields.

Scope: only the 34 fields listed below, only their ir.model.data rows
where module='studio_customization'. The field records themselves and
their column data are left alone.

Idempotent: search+unlink is a no-op the second time.
"""
import logging

_logger = logging.getLogger(__name__)

# Kept in sync with models/sale_order.py (v30 + v33 ports).
_PORTED_SALE_FIELDS = (
    'x_studio_credit_limit_approved',
    'x_studio_bank_guarantee_approved',
    'x_studio_over_bank_guarantee',
    'x_studio_over_bank_guarantee_amount',
    'x_studio_valid_bank_guarantee',
    'x_studio_over_credit',
    'x_studio_over_credit_amount',
    'x_studio_over_commission',
    'x_studio_over_commission_approved',
    'x_studio_overdue',
    'x_studio_overdue_approved',
    'x_studio_margin_approved',
    'x_studio_margin_exceed',
    'x_studio_order_payment_method',
    'x_studio_locked',
    'x_studio_unlocked',
    'x_studio_expired',
    'x_studio_expiry_date',
    'x_studio_price_not_confirmed',
    'x_studio_valid_order_lines',
    'x_studio_sales_order_validity',
    'x_studio_re_estimate_request_count',
    'x_studio_re_estimate_request_count_1',
    'x_studio_re_estimate_request_sent',
    'x_studio_account_mandatory',
    'x_studio_new_item_from_project',
    'x_studio_guarantee_status',
    'x_studio_inventory_short',
    'x_studio_project_no',
    'x_studio_main_project_no',
    # v33
    'x_studio_',                          # boolean, funky name kept verbatim
    'x_studio_approval_request_sent',
    'x_studio_authorized_repair_user',
    # v37 — needed by Fix-repair's related= chain on project.task
    'x_studio_quotation_type',
    # v38 — RUG-flow gates + re-estimate counter read by Fix-repair
    'x_studio_rug_approved',
    'x_studio_rug_rejected',
    'x_studio_re_estimate_count',
)
# Kept in sync with models/res_partner.py (v30 port).
_PORTED_PARTNER_FIELDS = (
    'x_studio_bank_guarantee_amount',
    'x_studio_expiry_date',
    'x_studio_payment_method',
    'x_studio_valid_bank_guarantee',
)
# Kept in sync with models/sale_order_line.py (v33 port).
_PORTED_SALE_LINE_FIELDS = (
    'x_studio_account_mandatory',
)


def strip_studio_xmlids_for_ported_fields(env):
    """Delete studio_customization ir.model.data rows for the 34 ported fields.

    Called from two places:
      - post_init_hook (fresh install)
      - migrations/17.0.1.0.32/post-migration.py (existing DB upgrade)
    """
    Fields = env['ir.model.fields'].sudo()
    IMD = env['ir.model.data'].sudo()

    sale_ids = Fields.search([
        ('model', '=', 'sale.order'),
        ('name', 'in', list(_PORTED_SALE_FIELDS)),
    ]).ids
    partner_ids = Fields.search([
        ('model', '=', 'res.partner'),
        ('name', 'in', list(_PORTED_PARTNER_FIELDS)),
    ]).ids
    sale_line_ids = Fields.search([
        ('model', '=', 'sale.order.line'),
        ('name', 'in', list(_PORTED_SALE_LINE_FIELDS)),
    ]).ids

    field_ids = sale_ids + partner_ids + sale_line_ids
    if not field_ids:
        return

    stale = IMD.search([
        ('module', '=', 'studio_customization'),
        ('model', '=', 'ir.model.fields'),
        ('res_id', 'in', field_ids),
    ])
    if not stale:
        return

    _logger.info(
        "BugFix-Sales: unlinking %d studio_customization xmlids for the "
        "x_studio_* fields now owned by BugFix-Sales.",
        len(stale),
    )
    stale.unlink()


# Studio server action 2336 ("SLS - Validate Mobile") is only present on
# the Jinasena production DB. The v25-era studio_action_patches.xml assumed
# it exists — on a fresh Odoo install the xmlid resolves to no record, then
# the <record> upsert tries to CREATE with only `code` supplied (no name,
# no model_id), and psycopg raises NotNullViolation on ir_act_server.name.
# Skip the whole patch on stand-alone DBs.
_STUDIO_ACTION_ID_MOBILE_VALIDATE = 2336
_MOBILE_VALIDATE_CODE = (
    "if record.mobile:\n"
    "    stripped = ''.join(c for c in str(record.mobile) if c.isdigit())\n"
    "    # Blank / all-non-digit strings are allowed through — either a\n"
    "    # legitimate empty field or a data-cleanup task, not our concern\n"
    "    # here. Only enforce when the user has typed actual digits.\n"
    "    if stripped and len(stripped) not in (10, 11, 12):\n"
    "        raise UserError(\n"
    "            'Invalid mobile number. Enter a valid mobile '\n"
    "            '(10 digits, optionally with country code).')\n"
)


def patch_sls_validate_mobile_action(env):
    """Rewire Studio server action 2336's code to the digit-strip
    mobile-number validation. Skipped when action 2336 doesn't exist
    (stand-alone install with no Jinasena Studio state)."""
    action = env['ir.actions.server'].sudo().browse(
        _STUDIO_ACTION_ID_MOBILE_VALIDATE
    ).exists()
    if not action:
        _logger.info(
            "BugFix-Sales: skipping SLS-Validate-Mobile patch — action %d "
            "not present on this DB (stand-alone install).",
            _STUDIO_ACTION_ID_MOBILE_VALIDATE,
        )
        return

    # Ensure the ir.model.data link exists so subsequent upgrades can
    # find the action via the BugFix-Sales.action_sls_validate_mobile
    # external ID.
    IMD = env['ir.model.data'].sudo()
    imd = IMD.search([
        ('module', '=', 'BugFix-Sales'),
        ('name', '=', 'action_sls_validate_mobile'),
    ], limit=1)
    if not imd:
        IMD.create({
            'module': 'BugFix-Sales',
            'name': 'action_sls_validate_mobile',
            'model': 'ir.actions.server',
            'res_id': action.id,
            'noupdate': False,
        })

    if (action.code or '').strip() != _MOBILE_VALIDATE_CODE.strip():
        action.write({'code': _MOBILE_VALIDATE_CODE})




# --- Field selection seeds (via Odoo _update_selection framework API) ---
# Studio-15 populated ir.model.fields.selection rows for these fields in CDB;
# Odoo 17 doesn't recreate them on install. ORM.create() is blocked for
# state='base' fields ("Properties of base fields cannot be altered..."),
# but Odoo's own _update_selection helper (used by
# ir.model.fields._compute_selection in core, see
# odoo/addons/base/models/ir_model.py:600) bypasses that guard. Uses
# framework query_insert / query_update — no cr.execute in our code.
# (model, field, value, label, sequence)
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


def _seed_field_selections(env, entries):
    """Add missing ir.model.fields.selection rows via Odoo's
    _update_selection helper. Groups by (model, field), reads current
    selection, appends missing CDB values, calls _update_selection with
    the merged list — Odoo inserts only the new rows and keeps existing."""
    Sel = env['ir.model.fields.selection'].sudo()
    Fld = env['ir.model.fields'].sudo()
    grouped = {}
    for model, fname, value, label, seq in entries:
        grouped.setdefault((model, fname), []).append((value, label, seq))
    for (model, fname), values in grouped.items():
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            _logger.info(
                "BugFix-Sales: skip %s.%s (field absent).", model, fname,
            )
            continue
        existing_recs = Sel.search(
            [('field_id', '=', fld.id)], order='sequence',
        )
        existing_pairs = [(r.value, r.name) for r in existing_recs]
        existing_values = {v for v, _ in existing_pairs}
        added = []
        for v, l, _seq in sorted(values, key=lambda t: t[2]):
            if v in existing_values:
                continue
            existing_pairs.append((v, l))
            existing_values.add(v)
            added.append(v)
        if not added:
            continue
        try:
            with env.cr.savepoint():
                Sel._update_selection(model, fname, existing_pairs)
                _logger.info(
                    "BugFix-Sales: seeded %s.%s += %s.", model, fname, added,
                )
        except Exception as e:
            _logger.warning(
                "BugFix-Sales: seed failed %s.%s (%s).", model, fname, e,
            )

def post_init_hook(env):
    """Odoo 17 post-install hook signature: (env)."""
    strip_studio_xmlids_for_ported_fields(env)
    patch_sls_validate_mobile_action(env)
    _seed_field_selections(env, _FIELD_SELECTIONS)
