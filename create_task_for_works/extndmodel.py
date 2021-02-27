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
            'name': vals['name'],
            'alias_contact': 'employees',
            'privacy_visibility': 'employees',
            'allow_timesheets': 'True',
            'label_tasks': 'obra'
        }

        if vals['partner_id']: rec['partner_id'] = vals['partner_id']
        project_obj = self.env['project.project'].sudo().create(rec)

        vals['related_project_id'] = project_obj.id

        return super(Warehouse, self).create(vals)

class Project(models.Model):
    _inherit = 'project.project'

    related_stock_warehouse = fields.One2many('stock.warehouse',
        'related_project_id', string="Ubicación asociada")
