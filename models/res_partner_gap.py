from odoo import fields, models


class ResPartnerGap(models.Model):
    _inherit = 'res.partner'

    x_vendor_id__purchase_requisition_count = fields.Integer(string='Vendor count')
