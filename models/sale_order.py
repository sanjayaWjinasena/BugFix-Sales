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

    # --- Quotation type selector ------------------------------------------
    # Chooses which downstream workflow the SO drives: plain Sales,
    # Project-linked, or Repair (helpdesk ticket driven). Fix-repair's
    # project.task carries a stored related= that walks into this field,
    # so it must be Python-declared on sale.order or fresh installs of
    # Fix-repair blow up in setup_related. Kept as a Selection here to
    # match the Studio-manual shape and preserve stored values.
    x_studio_quotation_type = fields.Selection(
        [
            ('Sales', 'Sales'),
            ('Project', 'Project'),
            ('Repair', 'Repair'),
        ],
        string='Quotation Type',
    )
    # --- Repair-flow gate flags read by Fix-repair ------------------------
    # These three fields live on sale.order (Sales-owned by definition)
    # but drive Fix-repair's Repair-Under-Guarantee (RUG) workflow. Since
    # Fix-repair's @api.depends chains walk into them and rec['...'].write
    # calls assign them, they must exist at Python setup time on any DB
    # where Fix-repair is installed — hence Python declarations here
    # rather than leaving them state=manual on sale.order.
    x_studio_rug_approved = fields.Boolean(
        string='RUG Approved',
        help='Repair-Under-Guarantee approved on this SO — releases the '
             'downstream repair pickings and closes the RUG cycle.',
    )
    x_studio_rug_rejected = fields.Boolean(
        string='RUG Rejected',
        help='Repair-Under-Guarantee rejected — the repair falls through '
             'to customer-pays.',
    )
    # v40: RUG confirmed flag — read by Studio invisible expressions
    # in the sale.order form arch (Confirm-button gate references
    # x_studio_rug_confirmed together with x_studio_rug_rejected and
    # ticket_repair_stage_state). Missed in v38's RUG batch; landing
    # now so form-arch load stops raising Name 'x_studio_rug_confirmed'
    # is not defined.
    x_studio_rug_confirmed = fields.Boolean(
        string='RUG Confirmed',
        help='Repair-Under-Guarantee confirmed by the operator — one '
             'step before rug_approved; used by button-gate expressions '
             'to distinguish "in review" from final decision.',
    )
    x_studio_re_estimate_count = fields.Integer(
        string='Re-estimate Count',
        help='Counter incremented every time the repair is re-estimated '
             '(driven by Fix-repair). Ticket-side re-estimate status '
             'rolls up from this.',
    )
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

    # --- v39 additions ------------------------------------------------------
    # Chunk 1g-audit findings (2026-08-12): 5 sale.order Studio fields
    # referenced by Studio view arch but never declared. On Clear-DB
    # state='manual' owned by studio_customization. Ported to state=base
    # here so standalone form-arch load doesn't error with
    # `"sale.order"."x_studio_budget_created" field is undefined`.
    # Types + selection values verified verbatim vs Clear-DB
    # ir.model.fields (2026-08-12).
    x_studio_budget_created = fields.Boolean(
        string='Budget Created',
    )
    x_studio_current_tot_amount = fields.Float(
        string='Current Total Amount',
    )
    x_studio_current_tot_amount_1 = fields.Float(
        string='Current Total Amount (v2)',
    )
    x_studio_proj_budget_status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('cancel', 'Cancelled'),
            ('confirm', 'Confirmed'),
            ('validate', 'Validated'),
            ('done', 'Done'),
        ],
        string='Project Budget Status',
    )
    x_studio_service_item_available = fields.Boolean(
        string='Service Item Available',
        compute='_compute_x_studio_service_item_available',
        store=False,
    )

    @api.depends('order_line.product_id.service_tracking',
                 'order_line.product_type')
    def _compute_x_studio_service_item_available(self):
        """Port of Clear-DB Studio compute (v-earlier):
            for rec in self:
              val = False
              for line in rec.order_line:
                if line.product_type == 'service':
                  if line.product_id.service_tracking == 'project_only':
                    val = True
              rec['x_studio_service_item_available'] = val
        """
        for rec in self:
            val = False
            for line in rec.order_line:
                if line.product_type == 'service' and \
                   line.product_id.service_tracking == 'project_only':
                    val = True
                    break
            rec.x_studio_service_item_available = val

    # --- v41 bulk sale.order Studio field port ------------------------------
    # Second full pass of Chunk 1g-audit backlog. Declares every safe
    # state=manual sale.order Studio field on Clear-DB so standalone
    # form-arch load stops raising "field is undefined" for each in turn.
    #
    # Types verified verbatim vs Clear-DB `ir.model.fields` (2026-08-12).
    # Selection values likewise (see x_studio_customer_payment_method).
    #
    # Deliberately SKIPPED (relations to Studio models not yet ported —
    # port them later once the target models land as Python declarations):
    #   - x_studio_project_group (m2o x_project_groups)
    #   - x_studio_project_budget (m2o crossovered.budget — deprecated)
    #   - x_studio_many2one_field_KjdJ3 (m2o account.budget.post — deprecated)
    #   - x_studio_one2many_field_ERCBB (o2m subclass sale.order.line)
    #   - x_x_studio_created_from_sales_order_1_crossovered_budget_count (int, depends on above)
    #   - x_x_studio_created_from_so_x_purchase_request_count (int, depends on Purchase Request Studio)
    #   - x_x_studio_sales_order_account_payment_count (int, depends on above)
    #   - x_x_studio_subcontracting_so_purchase_order_count (int, depends on above)
    #
    # Booleans (27) --------------------------------------------------------
    x_studio_bank_guarantee_notification = fields.Boolean(string='BG Notification')
    x_studio_bank_guarantee_request_sent = fields.Boolean(string='BG Request Sent')
    x_studio_bank_guarantee_validation = fields.Boolean(string='BG Validation')
    x_studio_bg_sent = fields.Boolean(string='BG Sent')
    x_studio_cancelled = fields.Boolean(string='Cancelled')
    x_studio_clear_free_items = fields.Boolean(string='Clear Free Items')
    x_studio_credit_limit_validation = fields.Boolean(string='Credit Limit Validation')
    x_studio_fsm_done = fields.Boolean(string='FSM Done')
    x_studio_fully_paid = fields.Boolean(string='Fully Paid')
    x_studio_grant_temporary_credit = fields.Boolean(string='Grant Temporary Credit')
    x_studio_margin_approval_request_sent = fields.Boolean(string='Margin Approval Request Sent')
    x_studio_over_comm_approval_request_sent = fields.Boolean(string='Over Commission Approval Request Sent')
    x_studio_overdue_request_sent = fields.Boolean(string='Overdue Request Sent')
    x_studio_petty_cash_reimbursement = fields.Boolean(string='Petty Cash Reimbursement')
    x_studio_pr_cost_updated = fields.Boolean(string='PR Cost Updated')
    x_studio_pr_created = fields.Boolean(string='PR Created')
    x_studio_project_item_approved = fields.Boolean(string='Project Item Approved')
    x_studio_project_item_request_sent = fields.Boolean(string='Project Item Request Sent')
    x_studio_rug_request_sent = fields.Boolean(string='RUG Request Sent')
    x_studio_sell_and_win = fields.Boolean(string='Sell and Win')
    x_studio_sub_contract = fields.Boolean(string='Sub Contract')
    x_studio_tem_credit_approval_request_sent = fields.Boolean(string='Temporary Credit Approval Request Sent')
    x_studio_temporary_credit_approved = fields.Boolean(string='Temporary Credit Approved')
    x_studio_transfer_inventory_ok = fields.Boolean(string='Transfer Inventory OK')
    x_studio_valid_order_lines_for_projects = fields.Boolean(string='Valid Order Lines for Projects')
    x_studio_valid_order_lines_for_update_rfq_cost = fields.Boolean(string='Valid Order Lines for Update RFQ Cost')
    x_studio_valid_transfer = fields.Boolean(string='Valid Transfer')

    # Texts / Chars (5) ----------------------------------------------------
    x_studio_confirm_validation = fields.Text(string='Confirm Validation')
    x_studio_confirm_validation_1 = fields.Text(string='Confirm Validation (v2)')
    x_studio_reject_reason = fields.Text(string='Reject Reason')
    x_studio_repair_validation = fields.Char(string='Repair Validation')
    x_studio_total = fields.Char(string='Total')

    # Dates (2) ------------------------------------------------------------
    x_studio_project_end_date = fields.Date(string='Project End Date')
    x_studio_project_start_date = fields.Date(string='Project Start Date')

    # Floats (2) -----------------------------------------------------------
    x_studio_customer_bank_guarantee = fields.Float(string='Customer BG Amount')
    x_studio_customer_credit_limit = fields.Float(string='Customer Credit Limit')

    # Monetary (3) — currency_field defaults to currency_id on sale.order --
    x_studio_cust_total_receivable = fields.Monetary(
        string='Customer Total Receivable',
        currency_field='currency_id',
    )
    x_studio_cust_total_receivable_1 = fields.Monetary(
        string='Customer Total Receivable (v2)',
        currency_field='currency_id',
    )
    x_studio_total_overdue = fields.Monetary(
        string='Total Overdue',
        currency_field='currency_id',
    )

    # Binary (9) — documents + images + warranty + related info -----------
    x_studio_document_1 = fields.Binary(string='Document 1')
    x_studio_document_2 = fields.Binary(string='Document 2')
    x_studio_document_3 = fields.Binary(string='Document 3')
    x_studio_image_1 = fields.Binary(string='Image 1')
    x_studio_image_2 = fields.Binary(string='Image 2')
    x_studio_image_3 = fields.Binary(string='Image 3')
    x_studio_related_information = fields.Binary(string='Related Information')
    x_studio_repair_image_01 = fields.Binary(string='Repair Image 01')
    x_studio_repair_image_02 = fields.Binary(string='Repair Image 02')
    x_studio_warranty_card = fields.Binary(string='Warranty Card')

    # Selection (1) — values verified vs Clear-DB ir.model.fields.selection
    x_studio_customer_payment_method = fields.Selection(
        selection=[('Cash', 'Cash'), ('Credit', 'Credit')],
        string='Customer Payment Method',
    )

    # Many2one to safe (already-existing) target (1) ----------------------
    x_studio_main_project_2 = fields.Many2one(
        'project.project',
        string='Main Project 2',
        ondelete='set null',
    )

    # Many2many to Chunk-1a-ported catalogue (1) --------------------------
    x_studio_repair_reason = fields.Many2many(
        'x_repair_reason',
        string='Repair Reason (m2m)',
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
