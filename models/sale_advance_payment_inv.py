# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleAdvancePaymentInv(models.TransientModel):
    """On Sales-type quotations, restrict the Create Invoice wizard to
    Regular Invoice only.

    Standard Odoo lets the salesperson pick between
      - Regular invoice
      - Down payment (percentage)
      - Down payment (fixed amount)

    User doesn't want Down-payment paths available on
    x_studio_quotation_type == 'Sales' SOs — Project and Repair SOs
    each have their own invoicing paths and this restriction is
    Sales-only.

    Two hooks:
      1. bugfix_sales_only_regular — computed boolean fed to the
         view as a readonly gate on advance_payment_method. When
         True, all radio options are disabled (Regular stays
         selected because default_get forced it).
      2. default_get override — even when the grey
         create_invoice_percentage button passes
         `default_advance_payment_method='percentage'` in context,
         a Sales-only wizard flips the default back to 'delivered'
         so the user sees Regular preselected and can't change it.
    """
    _inherit = 'sale.advance.payment.inv'

    bugfix_sales_only_regular = fields.Boolean(
        compute='_compute_bugfix_sales_only_regular',
    )

    @api.depends('sale_order_ids')
    def _compute_bugfix_sales_only_regular(self):
        for wizard in self:
            orders = wizard.sale_order_ids
            wizard.bugfix_sales_only_regular = bool(orders) and all(
                (o.x_studio_quotation_type or '') == 'Sales'
                for o in orders
            )

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if self.env.context.get('active_model') != 'sale.order':
            return res
        active_ids = self.env.context.get('active_ids') or []
        if not active_ids and self.env.context.get('active_id'):
            active_ids = [self.env.context['active_id']]
        if not active_ids:
            return res
        orders = self.env['sale.order'].sudo().browse(active_ids).exists()
        if not orders:
            return res
        if all((o.x_studio_quotation_type or '') == 'Sales' for o in orders):
            # Force Regular invoice — overrides
            # default_advance_payment_method='percentage' that the grey
            # create_invoice_percentage button passes in context, and
            # matches the readonly view gate below so the salesperson
            # can't switch to a down-payment option.
            res['advance_payment_method'] = 'delivered'
        return res
