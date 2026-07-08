# -*- coding: utf-8 -*-
from odoo import api, fields, models


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
