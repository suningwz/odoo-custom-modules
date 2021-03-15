# -*- coding: utf-8 -*-
from odoo import api, models, fields


class AccountInvoice(models.Model):

    _inherit = 'product.template'

    x_old_price_1_supplier = fields.Many2one('res.partner', string="Proveedor", stored=True, ondelete='set null')
    x_old_price_1_price = fields.Float(string="Precio", stored=True)
    x_old_price_1_date = fields.Date(string="Fecha", stored=True)

    x_old_price_2_supplier = fields.Many2one('res.partner', string="Proveedor", stored=True, ondelete='set null')
    x_old_price_2_price = fields.Float(string="Precio", stored=True)
    x_old_price_2_date = fields.Date(string="Fecha", stored=True)

    x_old_price_3_supplier = fields.Many2one('res.partner', string="Proveedor", stored=True, ondelete='set null')
    x_old_price_3_price = fields.Float(string="Precio", stored=True)
    x_old_price_3_date = fields.Date(string="Fecha", stored=True)
