# -*- coding: utf-8 -*-
{
    'name': "Adapta la cuenta en el flujo venta",

    'summary': """""",

    'description': """
        Modificacion flujo venta
            Al crear una venta extendida se comprobará
            el número de cuenta y se adaptará para la
            vista de los validadores.
    """,

    'author': "Nacho",
    'website': "http://www.ignacioragamiguel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'modify_sale_workflow'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
        'views/lead_extended_bank_account.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
