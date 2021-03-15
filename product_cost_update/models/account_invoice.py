# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017-TODAY Aurium Technologies(<http://www.auriumtechnologies.com>).
#    Author: Jalal ZAHID, Aurium Technologies (<http://www.auriumtechnologies.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import api, models, fields
from datetime import datetime


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.multi
    def invoice_validate(self):

        product_obj = self.env['product.product']
        # call the super methd here
        res = super(AccountInvoice, self).invoice_validate()
        for invoice in self:
            if invoice.type in ('in_invoice', 'in_refund'):
                for line in invoice.invoice_line_ids:
                    if line.product_id and line.price_unit:
                        pr_id = product_obj.browse(line.product_id.id)
                        pr_data = {
                        'x_old_price_1_supplier': self.partner_id.id,
                        'x_old_price_1_price': line.price_unit,
                        'x_old_price_1_date': datetime.today(),

                        'x_old_price_2_supplier': pr_id.x_old_price_1_supplier.id,
                        'x_old_price_2_price': pr_id.x_old_price_1_price,
                        'x_old_price_2_date': pr_id.x_old_price_1_date,

                        'x_old_price_3_supplier': pr_id.x_old_price_2_supplier.id,
                        'x_old_price_3_price': pr_id.x_old_price_2_price,
                        'x_old_price_3_date': pr_id.x_old_price_2_date,
                        }

                        lst_price = 0
                        vals = 0
                        for i in range(4):
                            if pr_data['x_old_price_{}_price'.format(i)]:
                                lst_price += pr_data['x_old_price_{}_price'.format(i)]
                                vals += 1

                        pr_data['standard_price'] = lst_price / vals

                        pr_id.write(pr_data)


        #return self.write({'state':'open'})
        return res
