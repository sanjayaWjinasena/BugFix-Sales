# -*- coding: utf-8 -*-
"""One-shot upgrade cleanup for v32.

post_init_hook only fires on install, never on upgrade. The 34 x_studio_*
fields ported in v30-v31 are already installed on every live DB, so the
cleanup needs to run at upgrade time too. This migration script does
exactly what the post_init_hook does — same function, same idempotent
behaviour.
"""
import importlib.util
import os

from odoo import api, SUPERUSER_ID
from odoo.modules.module import get_module_path


def migrate(cr, version):
    if not version:
        # Fresh install path — post_init_hook handles it.
        return

    # Dynamic-load hooks.py: the module name 'BugFix-Sales' has a dash,
    # which breaks `from odoo.addons.BugFix-Sales.hooks import ...`.
    hooks_path = os.path.join(get_module_path('BugFix-Sales'), 'hooks.py')
    spec = importlib.util.spec_from_file_location(
        'bugfix_sales_hooks', hooks_path,
    )
    hooks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hooks)

    env = api.Environment(cr, SUPERUSER_ID, {})
    hooks.strip_studio_xmlids_for_ported_fields(env)
