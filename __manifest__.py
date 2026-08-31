# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Sales',
    'version': '17.0.1.0.54',
    'summary': 'Bug fixes and enhancements for the Sales workflow',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Sales',
    'license': 'LGPL-3',
    # v54: added Jinasena_Masterdata_Reporting to depends.
    # BugFix-Sales/models/x_sales_report_type.py was _name='x_sales_report_type'
    # (a competing "owner" declaration without dep on the real owner). With two
    # _name= declarations and no dep chain, Odoo's topological sort could pick
    # BugFix-Sales's class as the live model, leaving x_studio_journal_items_id
    # absent from x_sales_report_type._fields at setup_models() time. That
    # caused KeyError on x_sales_report_model.x_studio_journal_item_ids
    # (related='x_studio_report_type.x_studio_journal_items_id') and broke the
    # registry on every startup. Fix: x_sales_report_type.py converted to
    # _inherit; Jinasena_Masterdata_Reporting (the canonical owner) added here.
    # studio_usermodel_migration removed in v52 (no load-time dep, cycle risk).
    'depends': ['base_setup', 'sale', 'sale_stock', 'industry_fsm_sale',
                'Jinasena_Masterdata_Reporting'],
    'post_init_hook': 'post_init_hook',
    # v47: bulk-port of remaining Studio artifacts via
    # scripts/scaffold_bugfix_module.py (adds 8 sale.order fields,
    # 36 sale.order.line fields, sale.order.alert model, 3 custom
    # models: x_customer_group / x_vendor_group / x_delivery_terms).
    # ir_model_pins.xml MUST load before ir.model.access.csv so the
    # ACL rows can resolve the model_x_* xmlids for the custom
    # models.
    # v52: removed studio_usermodel_migration from depends. This module
    # uses no models or fields from studio_usermodel_migration at
    # schema/model-load time (confirmed: no code or view references).
    # The dep was added in v0.47 to anchor load order when fixing the
    # previous cycle, but it created a new 3-way cycle:
    #   BugFix-Sales -> studio_usermodel_migration
    #     -> studio_migrations -> BugFix-Sales
    # Removed alongside dropping studio_migrations from
    # studio_usermodel_migration's depends (v0.0.9 of that module).
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
