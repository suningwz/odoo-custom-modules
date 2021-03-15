# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import re
#
class Lead(models.Model):
    _inherit = 'crm.lead'

    x_ba_iban = fields.Char(string="IBAN", store=True, required=True, size=4)
    x_ba_entity = fields.Char(string="C.C.C", store=True, required=True, size=4)
    x_ba_sucursal = fields.Char(string="C.C.C", store=True, required=True, size=4)
    x_ba_control = fields.Char(string="C.C.C", store=True, required=True, size=4)
    x_ba_number = fields.Char(string="C.C.C", store=True, required=True, size=4)
    x_ba_number_2 = fields.Char(string="C.C.C", store=True, required=True, size=4)



    x_ba_full = fields.Char(string="IBAN", store=True, size=29)

    def _check_iban(iban):
        pattern = '[A-Z]{2}[0-9]{22}'
        return re.match(pattern, iban.replace(' ',''))

    @api.model
    def create(self, vals):
        iban = '{} {} {} {} {} {}'.format(vals['x_ba_iban'].upper(), vals['x_ba_entity'], vals['x_ba_sucursal'], vals['x_ba_control'], vals['x_ba_number'], vals['x_ba_number_2'])
        if not self.check_iban(iban):
            raise ValidationError(_('El IBAN introducido no es válido.'))

        vals['x_ba_full'] = iban
        return super(Lead,self).create()

    def write(self, vals):
        iban = ''
        for elem in ['x_ba_iban' ,'x_ba_entity' ,'x_ba_sucursal' ,'x_ba_control' ,'x_ba_number' ,'x_ba_number_2']:
            if elem in vals:
                iban += vals[elem] + ' '
            else:
                iban += self[elem] + ' '
        iban = iban[:-1].upper()
        if not self.check_iban(iban):
            raise ValidationError(_('El IBAN introducido no es válido.'))

        vals['x_ba_full'] = iban

        return super(Lead, self).write(vals)

# PRO IBAN VALIDATION
# import string
# LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}
#
#
# def _number_iban(iban):
#     return (iban[4:] + iban[:4]).translate(LETTERS)
#
#
# def generate_iban_check_digits(iban):
#     number_iban = _number_iban(iban[:2] + '00' + iban[4:])
#     return '{:0>2}'.format(98 - (int(number_iban) % 97))
#
#
# def valid_iban(iban):
#     return int(_number_iban(iban)) % 97 == 1
#
#
# if __name__ == '__main__':
#     my_iban = 'RO13RZBR0000060007134800'
#     if generate_iban_check_digits(my_iban) == my_iban[2:4] and valid_iban(my_iban):
#         print('IBAN ok!\n')
#     else:
#         print('IBAN not ok!\n')
