# -*- coding: utf-8 -*-
{
    'name': "Extended HR Employee",

    'summary': """""",

    'description': """
        Modifica la vista de la creacion de nominas
            para el usuario de RRHH.
    """,

    'author': "Nacho",
    'website': "http://www.ignacioragamiguel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_timesheet', 'hr_payroll', 'extend_hr_employee'],

    # always loaded
    'data': [
        'views/hr_payslip_extended_form.xml'
        # 'security/ir.model.access.csv',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
