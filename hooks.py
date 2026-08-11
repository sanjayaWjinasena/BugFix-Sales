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

# Kept in sync with models/sale_order.py (v30 port).
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
)
# Kept in sync with models/res_partner.py (v30 port).
_PORTED_PARTNER_FIELDS = (
    'x_studio_bank_guarantee_amount',
    'x_studio_expiry_date',
    'x_studio_payment_method',
    'x_studio_valid_bank_guarantee',
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

    field_ids = sale_ids + partner_ids
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


def post_init_hook(env):
    """Odoo 17 post-install hook signature: (env)."""
    strip_studio_xmlids_for_ported_fields(env)
