# -*- coding: utf-8 -*-
{
    'name': "Importar productos desde BC3",

    'summary': """""",

    'description': """
        Dentro de la vista de los productos
        añade un botón para importar los mismos
        desde un fichero bc3.
    """,

    'author': "Nacho y Marcus",
    'website': "http://www.ignacioragamiguel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'views/import_products_bc3.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
