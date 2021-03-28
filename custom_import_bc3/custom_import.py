# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)




## OP1: Sobreescribe la funcion import
class Import(models.TransistentModel):
    _inherit = 'base_import.import'

# Añade funcionalidades a la función import
    @api.multi
    def do(self, fields, options, dryrun=False):
        # res_import deberia tener los datos del BC3/CSV
        res_import = super(Import, self).do(fields, options, dryrun)
        if "product.template" == self.res_model: #product.product es otra opción
            if not dryrun:
                _logger.warning('\n{}\n'.format(res_import))
                _logger.warning('\n{}\n'.format(fields))
                # Ejecutar sentencia SQL
                # self._cr.execute("""
                #     Insert your query""")

                # Mejor que SQL deberiamos usar las funciones CREATE de los modelos existentes
                rec = {
                    # Precio de coste
                    'price': '',
                    # Nombre mostrado
                    'name': '',
                    # Unidad de medida ID
                    'uom_id': 1,
                    # Descripcion TEXTO PLANO
                    'description': '',
                    # Categria interna ID
                    'categ_id': 1,
                    # Lista de materiales ID (+ adelante)
                    'bom_ids': False,
                }
                created_product = self.env['product.template'].sudo().create(rec)
                _logger.warning('\ncreated \n{}\n'.format(created_product))

        return res_import

## OP2: Añade funcionalidades al modelo PRODUCTO
# class Product(models.Model):
    ##Modelo del que heredamos
    # _inherit = 'product.template' #product.product es otra opción


    ## Definir acción del botón
    # def import_products_bc3(self):
        # No sabría como llamar al import pero puede que sea tan facil como usar
        # res_import = super(Import, self).do(fields, options, dryrun)
        # pass


        #
        # rec = {
        #     'name': vals['name'],
        #     'alias_contact': 'employees',
        #     'privacy_visibility': 'employees',
        #     'allow_timesheets': 'True',
        #     'label_tasks': 'obra'
        # }
        #
        # if vals['partner_id']: rec['partner_id'] = vals['partner_id']
        # project_obj = self.env['project.project'].sudo().create(rec)
        #
        # vals['related_project_id'] = project_obj.id
        #
        # return super(Warehouse, self).create(vals)
