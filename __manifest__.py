# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Sales',
    'version': '17.0.1.0.54',
    'summary': 'Bug fixes and enhancements for the Sales workflow',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Sales',
    'license': 'LGPL-3',
    # v0.1.0.54: cross-repo companion fix for BugFix-Purchase v0.1.0.33.
    # Both this module and BugFix-Purchase declare x_delivery_terms via
    # _name (not _inherit). Odoo merges the declarations, but the
    # LATER-loaded module's field list REPLACES the earlier one's --
    # so Purchase's x_studio_delivery_terms_id O2M (shipped v0.1.0.33)
    # got shadowed and became invisible at runtime ("Invalid field ...
    # on model x_delivery_terms" error at read time).
    # Fix: mirror Purchase's declaration in Sales - add the O2M
    # declaration + default=True on x_active. Now field sets match
    # regardless of merge order. NEW DEP BugFix-Purchase (needed for
    # x_delivery_term_charge comodel to resolve).
    'depends': ['base_setup', 'sale', 'sale_stock', 'industry_fsm_sale', 'studio_usermodel_migration', 'BugFix-Purchase'],
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
        'views/x_delivery_terms_studio_ported.xml',
        'views/res_partner_studio_ported.xml',
        'views/sale_order_studio_ported.xml',
        'views/product_pricelist_studio_ported.xml',
        'views/sale_report_studio_ported.xml',
        'views/res_company_studio_ported.xml',
        'views/sale_order_line_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
