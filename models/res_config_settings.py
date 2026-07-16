# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    """Expose the four x_minimum_sales_margin config values in the
    Sales settings page.

    x_minimum_sales_margin is a Studio-manual catalogue that carries
    exactly one active row per company (guarded by base.automation 146
    'SLS - Minimum Sales Margin % - in Setup Page'). The row's stored
    values are pure configuration:

      - x_studio_minimum_sales_margin_             (float, %)
      - x_studio_advance_payment_                  (float, %)
      - x_studio_sales_order_validity              (int, days)
      - x_studio_last_purchase_price_validity_days (int, days)

    Field names on this class mirror the model exactly so any Python
    or view expression that references either place uses the same
    identifier. get_values reads the row for self.env.company;
    set_values writes back via ORM (safe: automation 146 fires on
    create_date only) or via raw SQL when no row exists for the
    current company yet — bypassing the automation's cross-company
    'only one row' guard, same technique used in
    minimum_sales_margin_seed._seed_minimum_sales_margin_per_company.

    Fix-repair consumers that read env['x_minimum_sales_margin']
    scoped to company_id (advance-payment threshold on
    account.payment.register, delivery Validate gate on
    stock.picking) keep working with zero changes — same rows, same
    columns, just a nicer editor.
    """
    _inherit = 'res.config.settings'

    x_studio_minimum_sales_margin_ = fields.Float(
        string='Minimum Sales Margin %',
        help='Minimum margin percentage enforced on Sales / Project '
             'quotations at the Confirm gate.',
    )
    x_studio_advance_payment_ = fields.Float(
        string='Advance Payment %',
        help='Minimum advance-payment percentage required before '
             'deliveries can be validated on non-RUG repair sale '
             'orders. Enforced by Fix-repair on the payment-register '
             'wizard and on stock.picking button_validate.',
    )
    x_studio_sales_order_validity = fields.Integer(
        string='Sales Order Validity (Days)',
        help='How many days a quotation remains valid before it is '
             'flagged expired on the Confirm gate.',
    )
    x_studio_last_purchase_price_validity_days = fields.Integer(
        string='Last Purchase Price Validity (Days)',
        help="Age limit (days) before a product's last purchase price "
             "is considered stale.",
    )

    @api.model
    def get_values(self):
        res = super().get_values()
        row = self.env['x_minimum_sales_margin'].sudo().search(
            [('x_studio_company_id', '=', self.env.company.id)],
            limit=1,
        )
        if row:
            res.update({
                'x_studio_minimum_sales_margin_':
                    row.x_studio_minimum_sales_margin_ or 0.0,
                'x_studio_advance_payment_':
                    row.x_studio_advance_payment_ or 0.0,
                'x_studio_sales_order_validity':
                    row.x_studio_sales_order_validity or 0,
                'x_studio_last_purchase_price_validity_days':
                    row.x_studio_last_purchase_price_validity_days or 0,
            })
        return res

    def set_values(self):
        super().set_values()
        company = self.env.company
        MinMargin = self.env['x_minimum_sales_margin'].sudo()
        row = MinMargin.search(
            [('x_studio_company_id', '=', company.id)],
            limit=1,
        )
        vals = {
            'x_studio_minimum_sales_margin_':
                self.x_studio_minimum_sales_margin_ or 0.0,
            'x_studio_advance_payment_':
                self.x_studio_advance_payment_ or 0.0,
            'x_studio_sales_order_validity':
                self.x_studio_sales_order_validity or 0,
            'x_studio_last_purchase_price_validity_days':
                self.x_studio_last_purchase_price_validity_days or 0,
        }
        if row:
            # UPDATE path — automation 146 triggers on create_date
            # only, so writes to other fields don't fire the "only
            # one row allowed" guard. Safe to use ORM write.
            row.write(vals)
        else:
            # INSERT path — only reachable if a new company was added
            # AFTER v16 seeded the initial rows. ORM create() would
            # be blocked by automation 146 (searches every company
            # for any active row, raises "Only one Minimum Sales
            # Margin % can exist"). Bypass via raw SQL, same idiom
            # already used in minimum_sales_margin_seed
            # ._seed_minimum_sales_margin_per_company.
            self.env.cr.execute(
                """
                INSERT INTO x_minimum_sales_margin (
                    x_name,
                    x_studio_minimum_sales_margin_,
                    x_studio_advance_payment_,
                    x_studio_sales_order_validity,
                    x_studio_last_purchase_price_validity_days,
                    x_studio_company_id,
                    x_active,
                    x_studio_active,
                    create_uid,
                    create_date,
                    write_uid,
                    write_date
                )
                VALUES (%s, %s, %s, %s, %s, %s, TRUE, TRUE, %s, NOW(), %s, NOW())
                """,
                (
                    'Sales Configurations',
                    vals['x_studio_minimum_sales_margin_'],
                    vals['x_studio_advance_payment_'],
                    vals['x_studio_sales_order_validity'],
                    vals['x_studio_last_purchase_price_validity_days'],
                    company.id,
                    self.env.uid,
                    self.env.uid,
                ),
            )
