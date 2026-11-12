# -*- coding: utf-8 -*-
"""x_sales_report_type is owned by Jinasena_Masterdata_Reporting.

All fields (x_active, x_name, x_studio_report_code, x_studio_sequence,
and all One2many navigations) are declared there. BugFix-Sales has no
additional fields to contribute.

v53: converted from _name (sentinel) to _inherit so that
Jinasena_Masterdata_Reporting's canonical declaration — which includes
x_studio_journal_items_id and the other O2M fields — is always resolved
first. Having two _name = 'x_sales_report_type' declarations without an
explicit dep chain caused Odoo to pick whichever class was registered last
during topological load, leaving x_studio_journal_items_id absent from the
model's _fields at setup_models() time. That caused a KeyError on every
related-field setup in x_sales_report_model and brought down the registry.
"""
from odoo import models


class XSalesReportType(models.Model):
    _inherit = 'x_sales_report_type'
