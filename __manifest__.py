# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Sales',
    'version': '17.0.1.0.52',
    'summary': 'Bug fixes and enhancements for the Sales workflow',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base_setup', 'sale', 'sale_stock', 'industry_fsm_sale', 'studio_usermodel_migration'],
    'post_init_hook': 'post_init_hook',
    # v47: bulk-port of remaining Studio artifacts via
    # scripts/scaffold_bugfix_module.py (adds 8 sale.order fields,
    # 36 sale.order.line fields, sale.order.alert model, 3 custom
    # models: x_customer_group / x_vendor_group / x_delivery_terms).
    # ir_model_pins.xml MUST load before ir.model.access.csv so the
    # ACL rows can resolve the model_x_* xmlids for the custom
    # models.
    'data': [
        'security/ir_model_pins.xml',
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
