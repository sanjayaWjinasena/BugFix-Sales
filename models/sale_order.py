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
            sales_only = "x_studio_quotation_type == 'Sales'"
            for fname in _HIDE_ON_SALES_TYPE_FIELDS:
                for field_el in arch.xpath(f"//field[@name='{fname}']"):
                    existing = field_el.get('invisible', '')
                    if existing and existing not in ('0', 'False'):
                        field_el.set(
                            'invisible',
                            f"({existing}) or ({sales_only})",
                        )
                    else:
                        field_el.set('invisible', sales_only)
        return arch, view
