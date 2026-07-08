# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Sales',
    'version': '17.0.1.0.2',
    'summary': 'Bug fixes and enhancements for the Sales workflow',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base_setup', 'sale', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/bugfix_sales_data.xml',
        'views/doc_intro_views.xml',
        'views/doc_conclusion_views.xml',
        'views/sale_order_views.xml',
        'report/sale_report_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
