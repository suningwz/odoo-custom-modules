# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class Warehouse(models.Model):
    _inherit = 'stock.warehouse'

    x_warehouse_or_work = fields.Selection([('almacen','Almacén'),('obra','Obra')], string="Tipo de ubicación")

    related_project_id = fields.Many2one('project.project',
        string="Nombre del proyecto", ondelete='set null')


    @api.model
    def create(self, vals):

        rec = {
            'name': vals['name'], ## Nombre del proyecto
            'alias_contact': 'employees',
            'privacy_visibility': 'employees',
            'allow_timesheets': 'True',
            'label_tasks': 'obra'
        }

        if vals['partner_id']: rec['partner_id'] = vals['partner_id']
        project_obj = self.env['project.project'].create(rec)

        vals['related_project_id'] = project_obj.id

        return super(Warehouse, self).create(vals)

class Project(models.Model):
    _inherit = 'project.project'

    related_stock_warehouse = fields.One2many('stock.warehouse',
        'related_project_id', string="Ubicación asociada")


        # 'alias_defaults': ,
        # 'alias_id': ,
        # 'alias_model_id': ,
        # 'analytic_account_id': ,
        # 'company_id': ,



    # @api.multi
    # def action_add_lines(self):
    #     invoice_line_obj = self.env['account.invoice.line']
    #     for each in self:
    #         for move in each.related_stock_moves:
    #             rec = {
    #                 'account_id': each.account_id.id,
    #                 'invoice_id': each.id,
    #                 'product_id': move.product_id.id,
    #                 'quantity': move.product_uom_qty,
    #                 'name': move.product_id.name,
    #                 'price_unit': '0.0'
    #             }
    #             if move.product_id.description: rec['name'] = move.product_id.description
    #             invoice_line_obj.create(rec)
    #     return True







#     invoice_line_ids = fields.One2many('account.invoice.line',
#         'invoice_id', string="Líneas de la factura", compute='_add_lines')
#
# ## Retrieve product_id and product_uom_qty
#     @api.depends('related_stock_moves')
#     @api.one
#     def _add_lines(self):
#         for move in self.related_stock_moves:
#             self.env['account.invoice.line'].create({
#                     'account_id': self.account_id.id,
#                     'invoice_id': self.id,
#                     'product_id': move.product_id.id,
#                     'quantity': move.product_uom_qty,
#                     'name': move.product_id.description,
#                     'price_unit': '0.0'
#             })
