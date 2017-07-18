# -*- coding: utf-8 -*-
{
    'name': "advansysTMS",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Hend Soliman",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/advansys_root_view.xml',
        'views/advansys_category_view.xml',
        'views/advansys_course_view.xml',
        'views/advansys_employee_view.xml',
        'views/advansys_department_view.xml',
        'wizard/advansysTMS_employee_type_view.xml',
        # 'report/advansysTMS_category_report_views.xml',
        # 'report/category_reports.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
