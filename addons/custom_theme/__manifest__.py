# -*- coding: utf-8 -*-
{
    'name': "custom_theme",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
     This is Module used as theme tutorail for odoo 10.
    """,

    'author': "Hend Soliman",
    'website': "http://www.advansys-ESC.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Theme/Creative',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/layout.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/pages.xml',
        'views/assets.xml',
        'views/snippets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
