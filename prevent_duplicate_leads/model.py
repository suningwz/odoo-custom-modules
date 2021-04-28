# -*- coding: utf-8 -*-
from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)


class Lead(models.Model):
    _inherit = 'crm.lead'


    duplicated_nif = fields.Boolean("NIF Duplicado", default=False, store=True)
    duplicated_records = fields.One2many('crm.lead', 'duplicated_reference', string="Documentos relacionados", store=True)
    duplicated_reference = fields.Many2one('crm.lead')

    @api.model
    def create(self, vals):

        existing_nif = self.env['crm.lead'].sudo().search([('x_nif','=',vals['x_nif'])])
        _logger.warning('\n\n{}\n\n'.format(existing_nif))
        if existing_nif:
           vals['duplicated_nif'] = True
           vals['duplicated_records'] = [lead.id for lead in existing_nif]

        return super(Lead, self).create(vals)
        # return lead_id
