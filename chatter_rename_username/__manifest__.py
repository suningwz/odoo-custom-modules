# -*- coding: utf-8 -*-
{
    'name': "Facturas desde movimientos de inventario",

    'summary': """""",

    'description': """
        Facturas desde movimientos de inventario
            En las facturas con proveedor podemos
            seleccionar los movimientos asociados.
    """,

    'author': "Nacho",
    'website': "http://www.ignacioragamiguel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'res'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
        # 'views/invoice.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
