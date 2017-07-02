# -*- coding: utf-8 -*-
{
    'name': "advansys",

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
    'depends': [],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'views/views.xml',
        'views/advansys_basic_view.xml',
        'views/advansys_employee_view.xml',
        'views/advansys_department_view.xml',
        'views/advansys_project_view.xml',
        'views/advansys_student_view.xml',
        'report/advansys_employee_report.xml',
        'report/employee_reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
