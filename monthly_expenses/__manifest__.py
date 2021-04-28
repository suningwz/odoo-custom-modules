# -*- coding: utf-8 -*-
{
    'name': "Modificacion flujo venta",

    'summary': """""",

    'description': """
        Modificacion flujo venta
            El grupo de validadores no podra editar
            los formularios de venta que no ha creado.
    """,

    'author': "Nacho",
    'website': "http://www.ignacioragamiguel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
        'views/hr_expense_extended.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
