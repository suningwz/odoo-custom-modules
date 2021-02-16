# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class Move(models.Model):
    _inherit = 'stock.move'


    x_invoice_id = fields.Many2one('account.invoice',
        string="Factura de referencia", ondelete='set null')


class Invoice(models.Model):
    _inherit = 'account.invoice'

    related_stock_moves = fields.One2many('stock.move',
        'x_invoice_id', string="Movimiento asociado")


    @api.multi
    def action_add_lines(self):
        invoice_line_obj = self.env['account.invoice.line']
        for each in self:
            for move in each.related_stock_moves:
                rec = {
                    'account_id': each.account_id.id,
                    'invoice_id': each.id,
                    'product_id': move.product_id.id,
                    'quantity': move.product_uom_qty,
                    'name': move.product_id.name,
                    'price_unit': '0.0'
                }
                if move.product_id.description: rec['name'] = move.product_id.description
                invoice_line_obj.create(rec)
        return True







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
