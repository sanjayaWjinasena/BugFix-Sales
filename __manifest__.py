# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Sales',
    'version': '17.0.1.0.0',
    'summary': 'Bug fixes and enhancements for the Sales workflow',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base_setup', 'sale', 'sale_stock'],
    'data': [
        'data/bugfix_sales_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
