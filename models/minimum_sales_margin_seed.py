# -*- coding: utf-8 -*-
from odoo import api, models


class MinimumSalesMarginSeed(models.AbstractModel):
    """Seed a default row on the Studio-manual x_minimum_sales_margin
    catalogue for every active res.company that doesn't already have
    one.

    Why this is needed
    ------------------
    x_minimum_sales_margin is a Studio catalogue holding one row per
    company with fields that other Studio logic reads at runtime:

      - x_studio_advance_payment_ (float, %) — minimum advance
        payment required on Repair sale orders
      - x_studio_minimum_sales_margin_ (float, %)
      - x_studio_sales_order_validity (int, days)
      - x_studio_last_purchase_price_validity_days (int, days)

    Three consumer sites read the row with
    `env['x_minimum_sales_margin'].search([], limit=1)` (no company
    filter — they rely on the model's record rule 638 to scope
    per-company at read time):

      - compute on account.payment.x_studio_payment_validation
      - server action 2427 'RR - Validate Payment %'
      - server action 2341 'SLS - Create Customer Payment'

    If a company has no row, all three degrade silently: the compute
    stays False (no warning banner), the validation action never
    raises, and the SO 'Create Customer Payment' button pre-fills
    Rs. 0.00. See MIGRATION notes for the full downstream trace.

    Why raw SQL, not create()
    -------------------------
    A Studio base.automation (id 146, server action 1776) runs on
    every ORM create() of this model and raises
        UserError('Only one Minimum Sales Margin % can exist.')
    whenever ANY x_studio_active=True row exists — regardless of
    company. That guard predates the multi-company setup and blocks
    any second row from being created via the ORM.

    Raw SQL INSERT bypasses ir.actions.server / base_automation
    entirely, so we can seed without touching the automation. The
    same idempotence-by-existence-check pattern used elsewhere in
    Fix-repair / BugFix-Sales applies: skip companies that already
    carry a row.
    """
    _name = 'bugfix_sales.minimum_sales_margin.seed'
    _description = 'Seed Minimum Sales Margin config per company'

    _DEFAULT_NAME = 'Sales Configurations'
    _DEFAULT_ADVANCE_PCT = 50.0
    _DEFAULT_MARGIN_PCT = 35.0
    _DEFAULT_SO_VALIDITY_DAYS = 1
    _DEFAULT_PURCHASE_VALIDITY_DAYS = 30

    @api.model
    def _seed_minimum_sales_margin_per_company(self):
        """Insert one x_minimum_sales_margin row for every active
        company that doesn't already have one. Idempotent — re-runs
        no-op when every company is already seeded.

        Defaults mirror the existing production row on company 1
        (Jinasena (Pvt) Ltd.) so the enforcement thresholds are
        consistent across the multi-company install. Individual
        companies can override their values later via the config
        form; the seed only touches rows it creates.
        """
        companies = self.env['res.company'].sudo().search([])
        if not companies:
            return

        self.env.cr.execute(
            "SELECT DISTINCT x_studio_company_id "
            "FROM x_minimum_sales_margin "
            "WHERE x_studio_company_id IS NOT NULL"
        )
        already = {row[0] for row in self.env.cr.fetchall()}
        missing = companies.filtered(lambda c: c.id not in already)
        if not missing:
            return

        uid = self.env.uid
        for company in missing:
            self.env.cr.execute(
                """
                INSERT INTO x_minimum_sales_margin (
                    x_name,
                    x_studio_advance_payment_,
                    x_studio_minimum_sales_margin_,
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
                    self._DEFAULT_NAME,
                    self._DEFAULT_ADVANCE_PCT,
                    self._DEFAULT_MARGIN_PCT,
                    self._DEFAULT_SO_VALIDITY_DAYS,
                    self._DEFAULT_PURCHASE_VALIDITY_DAYS,
                    company.id,
                    uid,
                    uid,
                ),
            )
