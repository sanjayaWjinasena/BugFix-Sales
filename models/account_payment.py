# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    # v45: two Studio fields ported from Clear-DB. Required by
    # Fix-repair v284's port of Studio automation 241 (RR - Validate
    # Payment %), which reads the SO link + quotation type off the
    # payment record to gate its advance-threshold check.
    #
    # x_studio_sales_order: stamped by the accounts team (or a future
    # automation) when creating an advance payment against a specific
    # SO. Left as a plain m2o -- no ondelete cascade because a payment
    # outliving its SO shouldn't be blindly deleted.
    x_studio_sales_order = fields.Many2one(
        'sale.order',
        string='Sales Order',
    )
    # Selection kept in sync with sale.order.x_studio_quotation_type
    # (Sales / Project / Repair). Same three values so the payment's
    # type mirrors its parent SO's classification.
    x_studio_quotation_type = fields.Selection(
        selection=[
            ('Sales', 'Sales'),
            ('Project', 'Project'),
            ('Repair', 'Repair'),
        ],
        string='Quotation Type',
    )
