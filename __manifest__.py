# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Sales',
    'version': '17.0.1.0.41',
    'summary': 'Bug fixes and enhancements for the Sales workflow',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base_setup', 'sale', 'sale_stock', 'industry_fsm_sale'],
    'post_init_hook': 'post_init_hook',
    # data/studio_action_patches.xml is loaded conditionally in
    # hooks.patch_sls_validate_mobile_action (Python) because it assumes
    # Studio server action 2336 already exists — true on Jinasena
    # production, false on stand-alone installs.
    'data': [
        'security/ir.model.access.csv',
        'data/bugfix_sales_data.xml',
        'views/doc_intro_views.xml',
        'views/doc_conclusion_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/sale_advance_payment_inv_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
