"""delivery_terms - also declared in BugFix-Purchase (canonical owner).
Both modules use _name (not _inherit); Odoo merges declarations at runtime.

v0.1.0.57: removed delivery_terms_id O2M from this declaration.
The O2M points to delivery_term_charge which is only declared in
BugFix-Purchase. Declaring the O2M here would force BugFix-Sales to
depend on BugFix-Purchase to resolve the comodel at setup, which
created the 3-way cycle Sales -> Purchase -> Accounting -> Sales.

BugFix-Purchase's declaration keeps the O2M and loads AFTER Sales.
Since Purchase loads last for this model, its class definition wins
and the O2M is present on the merged delivery_terms model at
runtime. Field sets don't need to match for _name-mirror models."""

from odoo import fields, models


class XDeliveryTerms(models.Model):
    _name = "delivery_terms"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Delivery Terms"

    active = fields.Boolean(default=True)
    name = fields.Char(string="Delivery Term")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    copied = fields.Boolean()
    description = fields.Char()
    sequence = fields.Integer()
    vendor_despatch = fields.Boolean(string="Vendor Dispatch Voucher")
