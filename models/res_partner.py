"""Customer-master Studio fields ported into BugFix-Sales.

These fields were originally created by Odoo Studio on res.partner
and were owned by the studio_customization module (state='manual').
The Jul 2026 migration flipped their state to 'base' and repinned
their ir.model.data rows to Fix-repair via raw SQL, but no Python
declaration existed anywhere — meaning a fresh module install on a
clean DB would not recreate them.

This file declares them under BugFix-Sales so that:
  1. On the current SH DB (where they already exist), the Python
     declaration takes over ownership on next module upgrade — same
     shape, same values.
  2. On a fresh DB install, the fields are actually created by
     Odoo's ORM at BugFix-Sales install time, not just left as
     dangling metadata.

These are all consumed by sale.order via `related=partner_id.x_...`
declarations in sale_order.py; declaring them here first guarantees
the related fields resolve.
"""

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    # v0.1.0.58: computed count for purchase.requisition records where
    # vendor_id equals this partner. Studio declared this store=False.
    # Purchase.requisition is in standard purchase_requisition module -
    # env.get() would be safer but env['purchase.requisition'] works
    # because purchase_requisition is guaranteed by Purchase deps.
    # Kept in BugFix-Sales because Studio pinned it here.
    vendor_id__purchase_requisition_count = fields.Integer(
        string="Vendor count", store=False, compute="_compute_x_vendor_id_pr_count"
    )

    @api.depends()
    def _compute_x_vendor_id_pr_count(self):
        PR = self.env.get("purchase.requisition")
        if PR is None:
            for r in self:
                r.vendor_id__purchase_requisition_count = 0
            return
        results = PR.read_group(
            [("vendor_id", "in", self.ids)], ["vendor_id"], ["vendor_id"]
        )
        dic = {
            x["vendor_id"][0]: x["vendor_id_count"]
            for x in results
            if x.get("vendor_id")
        }
        for r in self:
            r.vendor_id__purchase_requisition_count = dic.get(r.id, 0)

    bank_guarantee_amount = fields.Float()
    expiry_date = fields.Date(
        string="Bank Guarantee Expiration Date",
    )
    payment_method = fields.Selection(
        [("Cash", "Cash"), ("Credit", "Credit")],
        string="Payment Type",
    )
    valid_bank_guarantee = fields.Boolean(
        help=(
            "True when the partner has an active bank guarantee "
            "(expiry_date in the future). Used by sale.order "
            "credit-limit gates via a related field."
        ),
    )


class ResPartnerGap(models.Model):
    _inherit = "res.partner"

    vendor_id__purchase_requisition_count = fields.Integer(string="Vendor count")
