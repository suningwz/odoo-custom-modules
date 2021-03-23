# -*- coding: utf-8 -*-
from odoo import api, fields, models
import logging
#
_logger = logging.getLogger(__name__)


class Move(models.Model):
    _inherit = 'stock.move'


    x_invoice_id = fields.Many2one('account.invoice',
        string="Factura de referencia", ondelete='set null')

    x_invoice_line = fields.Many2one('account.invoice.line',
        string='Linea de factura', ondelete='set null')
    # x_invoiced = fields.Boolean(string='Facturado', store=True, compute='_compute_x_invoiced')
    #
    # def _compute_x_invoiced(self):
    #     for rec in self:
    #         _logger.warning('\n\n{} {} {}\n\n'.format(rec, rec.x_invoice_id, rec.x_invoice_id.state))
    #         if not rec.x_invoice_id or rec.x_invoice_id.state == 'cancel':
    #             rec.x_invoiced = False
    # @api.onchange('x_invoice_id', 'x_invoice_id.state')
    # def onchange_x_invoice_id(self):
    #     if not self.x_invoice_id or self.x_invoice_id.state == 'cancel':
    #         self.x_invoiced = False
    #     return self

class Invoice(models.Model):
    _inherit = 'account.invoice'

    related_stock_moves = fields.One2many('stock.move',
        'x_invoice_id', string="Movimiento asociado")


    @api.multi
    def action_add_lines(self):
        invoice_line_obj = self.env['account.invoice.line']
        for each in self:
            for move in each.related_stock_moves:
                # _logger.warning('\n\n{} {}\n\n'.format(move, move.x_invoice_line))
                if not move.x_invoice_line:
                    rec = {
                        'account_id': each.account_id.id,
                        'invoice_id': each.id,
                        'product_id': move.product_id.id,
                        'quantity': move.product_uom_qty,
                        'name': move.product_id.name,
                        'price_unit': '0.0'
                    }
                    if move.product_id.description: rec['name'] = move.product_id.description
                    move.x_invoice_line = invoice_line_obj.create(rec)
                    # move.sudo().update({'x_invoiced': True})

        return True


class InvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    related_stock_move = fields.One2many('stock.move',
        'x_invoice_line', string="Movimiento asociado")


    @api.multi
    def unlink(self):
        for line in self:
            if line.related_stock_move:


        return models.Model.unlink(self)





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
