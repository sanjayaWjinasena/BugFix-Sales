# -*- coding: utf-8 -*-
from odoo import api, fields, models


# Header fields hidden on Sales-type quotations. Project quotations
# keep them (Project genuinely uses Recurring Plan + Main Project No
# etc.). Repair quotations are independently handled by Fix-repair's
# own _get_view override; the OR-merge in our _get_view below plays
# nicely with that — both hides stack when both apply.
_HIDE_ON_SALES_TYPE_FIELDS = (
    'x_studio_service_item_available',
    'x_studio_main_project_no',
    'x_studio_re_estimate_request_count',      # boolean
    'x_studio_re_estimate_request_count_1',    # integer counter
    'x_studio_re_estimate_count',
    'plan_id',                                  # Recurring Plan (core)
)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Selected template — for reference / re-loading. The salesperson
    # picks one from the header; the corresponding description is
    # copied into the *_text field below, which is the field actually
    # printed on the quotation.
    bugfix_sales_intro_id = fields.Many2one(
        'bugfix_sales.doc_intro',
        string='Document Introduction',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
    bugfix_sales_conclusion_id = fields.Many2one(
        'bugfix_sales.doc_conclusion',
        string='Document Conclusion',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )

    # Editable copies of the template text. Storing them per-SO means
    # the salesperson can tweak wording for a specific customer without
    # touching the shared library entry.
    bugfix_sales_intro_text = fields.Text(string='Introduction')
    bugfix_sales_conclusion_text = fields.Text(string='Conclusion')

    # ------------------------------------------------------------------
    # Studio → BugFix-Sales port of Sales-workflow credit / bank-guarantee
    # / margin / overdue gate fields.
    #
    # These were created in Studio (state='manual', owned by
    # studio_customization). The Jul 2026 migration flipped them to
    # state='base' and repinned ir.model.data ownership to Fix-repair
    # via raw SQL — but no Python declaration existed. Consumed by
    # code in Fix-repair (Confirm gates) and BugFix-Sales (config
    # setters, view arch inheriting these attrs).
    #
    # Declaring them here means:
    #  - Current DB: ownership takes over cleanly on next upgrade
    #  - Fresh DB install of BugFix-Sales: the fields are actually
    #    created by the ORM instead of relying on Studio DB state
    # ------------------------------------------------------------------

    # --- Credit-limit gate --------------------------------------------------
    x_studio_credit_limit_approved = fields.Boolean(
        string='Credit Limit Approved',
    )
    # --- Bank guarantee -----------------------------------------------------
    x_studio_bank_guarantee_approved = fields.Boolean(
        string='Bank Guarantee Approved',
    )
    x_studio_over_bank_guarantee = fields.Boolean(
        string='Over Bank Guarantee',
    )
    x_studio_over_bank_guarantee_amount = fields.Float(
        string='Over Bank Guarantee Amount',
    )
    x_studio_valid_bank_guarantee = fields.Boolean(
        string='Valid Bank Guarantee',
        related='partner_id.x_studio_valid_bank_guarantee',
        store=True,
    )
    # --- Over-credit --------------------------------------------------------
    x_studio_over_credit = fields.Boolean(
        string='Over Credit',
    )
    x_studio_over_credit_amount = fields.Float(
        string='Over Credit Amount',
    )
    # --- Over-commission ----------------------------------------------------
    x_studio_over_commission = fields.Boolean(
        string='Over Commission',
    )
    x_studio_over_commission_approved = fields.Boolean(
        string='Over Commission Approved',
    )
    # --- Overdue ------------------------------------------------------------
    x_studio_overdue = fields.Boolean(
        string='Overdue',
    )
    x_studio_overdue_approved = fields.Boolean(
        string='Overdue Approved',
    )
    # --- Margin -------------------------------------------------------------
    x_studio_margin_approved = fields.Boolean(
        string='Margin Approved',
    )
    x_studio_margin_exceed = fields.Boolean(
        string='Margin Exceed',
    )
    # --- Order-payment / lock / expiry --------------------------------------
    x_studio_order_payment_method = fields.Selection(
        [('Cash', 'Cash'), ('Credit', 'Credit')],
        string='Order Payment Type',
    )
    x_studio_locked = fields.Boolean(string='Locked')
    x_studio_unlocked = fields.Boolean(string='Unlocked')
    x_studio_expired = fields.Boolean(string='Expired')
    x_studio_expiry_date = fields.Date(
        string='Bank Guarantee Expiration Date',
        related='partner_id.x_studio_expiry_date',
        store=True,
    )
    # --- Confirm-time gates -------------------------------------------------
    x_studio_price_not_confirmed = fields.Boolean(
        string='Price Not Confirmed',
    )
    x_studio_valid_order_lines = fields.Boolean(
        string='Valid Order Lines',
    )
    x_studio_sales_order_validity = fields.Integer(
        string='Sales Order Validity',
    )
    # --- Re-estimate request tracker ---------------------------------------
    x_studio_re_estimate_request_count = fields.Boolean(
        string='Re-estimate Request Count (bool)',
    )
    x_studio_re_estimate_request_count_1 = fields.Integer(
        string='Re-estimate Request Count',
    )
    x_studio_re_estimate_request_sent = fields.Boolean(
        string='Re-estimate Request Sent',
    )
    # --- Misc SO gates ------------------------------------------------------
    x_studio_account_mandatory = fields.Boolean(
        string='Account Mandatory',
    )
    x_studio_new_item_from_project = fields.Boolean(
        string='New Item from Project',
    )
    x_studio_guarantee_status = fields.Char(
        string='Guarantee Status',
    )
    x_studio_inventory_short = fields.Boolean(
        string='Inventory Short',
    )
    # --- Project link -------------------------------------------------------
    x_studio_project_no = fields.Many2one(
        'project.project',
        string='Project No',
        related='task_id.project_id',
        store=True,
    )
    x_studio_main_project_no = fields.Many2one(
        'project.project',
        string='Main Project No',
    )
    # --- v33 additions ------------------------------------------------------
    # Junk-named Studio artefact — a boolean literally named "x_studio_"
    # (with a trailing underscore). Kept verbatim to preserve any data
    # on live records.
    x_studio_ = fields.Boolean(
        string='Test Field',
    )
    x_studio_approval_request_sent = fields.Boolean(
        string='Approval Request Sent',
    )
    x_studio_authorized_repair_user = fields.Boolean(
        string='Authorized Repair User',
        readonly=True,
    )

    @api.onchange('bugfix_sales_intro_id')
    def _onchange_bugfix_sales_intro_id(self):
        for order in self:
            if order.bugfix_sales_intro_id:
                order.bugfix_sales_intro_text = order.bugfix_sales_intro_id.description

    @api.onchange('bugfix_sales_conclusion_id')
    def _onchange_bugfix_sales_conclusion_id(self):
        for order in self:
            if order.bugfix_sales_conclusion_id:
                order.bugfix_sales_conclusion_text = order.bugfix_sales_conclusion_id.description

    @api.model
    def _get_view(self, view_id=None, view_type='form', **options):
        """Hide the header fields listed in _HIDE_ON_SALES_TYPE_FIELDS
        on Sales-type quotations. Runs on the merged arch (post all
        inherits), so Studio-added fields are addressable by xpath.

        Merges with any existing `invisible` expression instead of
        overwriting it — e.g. Fix-repair sets
        invisible="x_studio_quotation_type == 'Repair'" on the same
        fields; our OR keeps both conditions in place so a field is
        hidden on Sales OR Repair, visible on Project.
        """
        arch, view = super()._get_view(view_id, view_type, **options)
        if view_type == 'form':
            # `not x_studio_quotation_type` also covers a brand-new SO
            # where the type hasn't been picked yet — we want the fields
            # gone from form open, not to flash into view before the
            # user selects a type.
            sales_only = (
                "not x_studio_quotation_type or "
                "x_studio_quotation_type == 'Sales'"
            )
            for fname in _HIDE_ON_SALES_TYPE_FIELDS:
                # The responsive SO header renders labels and fields as
                # sibling elements — <label for="fname"/> sits in one
                # cell, <field name="fname"/> in the next. Setting
                # invisible on the field alone leaves the label
                # dangling with no value beside it. Hide both.
                elements = (
                    arch.xpath(f"//field[@name='{fname}']")
                    + arch.xpath(f"//label[@for='{fname}']")
                )
                for el in elements:
                    existing = el.get('invisible', '')
                    if existing and existing not in ('0', 'False'):
                        el.set(
                            'invisible',
                            f"({existing}) or ({sales_only})",
                        )
                    else:
                        el.set('invisible', sales_only)
        return arch, view
