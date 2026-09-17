# -*- coding: utf-8 -*-
"""Studio field ports for sale.order.alert (auto-ported from CDB)."""
from odoo import fields, models


class XSaleOrderAlertExt(models.Model):
    _inherit = 'sale.order.alert'

    x_studio_char_field_dpQHc = fields.Char(string='New Text', related='automation_id.x_studio_char_field_dpQHc', store=False)
    x_studio_comments = fields.Char(string='Comments', related='automation_id.x_studio_comments', store=False)
    x_studio_selection_field_ogQSe = fields.Selection([], string='New Selection', related='automation_id.x_studio_selection_field_ogQSe', store=False)
    x_studio_status = fields.Selection([], string='Status', related='automation_id.x_studio_status', store=False)
