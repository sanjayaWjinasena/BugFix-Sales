# -*- coding: utf-8 -*-
"""One-shot upgrade cleanup for v33.

Additional sale.order + sale.order.line fields ported in v33. Runs the
same strip function as v32; idempotent, so already-stripped v30-v31
xmlids are no-op'd and only the new v33 xmlids get unlinked.
"""
import importlib.util
import os

from odoo import api, SUPERUSER_ID
from odoo.modules.module import get_module_path


def migrate(cr, version):
    if not version:
        return

    hooks_path = os.path.join(get_module_path('BugFix-Sales'), 'hooks.py')
    spec = importlib.util.spec_from_file_location(
        'bugfix_sales_hooks', hooks_path,
    )
    hooks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hooks)

    env = api.Environment(cr, SUPERUSER_ID, {})
    hooks.strip_studio_xmlids_for_ported_fields(env)
