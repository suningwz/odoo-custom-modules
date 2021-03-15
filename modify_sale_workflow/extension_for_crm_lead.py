# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import re
import logging
#
_logger = logging.getLogger(__name__)
#
class Lead(models.Model):
    _inherit = 'crm.lead'

    x_address_id = fields.Char(
        string="ID Dirección", store=True)
    x_aut_name = fields.Char(
        string="Nombre del autorizado", store=True)
    x_aut_nif = fields.Char(
        string="NIF del autorizado", store=True)

    # B A requires validation (IBAN + ACC)
    x_bank_account = fields.Char(
        string="IBAN", store=True, size=24)

    x_charge_code = fields.Char(
        string="Código de carga", store=True)
    x_charge_zone = fields.Selection(
        [('SUR','SUR'), ('LEVANTE','LEVANTE'), ('CENTRO','CENTRO'), ('NORESTE','NORESTE'), ('NORTE','NORTE'), ('CANARIAS','CANARIAS')],
        string="Zona de carga", store=True)
    x_cif = fields.Char(
        string="CIF", store=True)
    x_client_name = fields.Char(
        string="Nombre del cliente", store=True)
    x_company_name = fields.Char(
        string="Nombre de la empresa", store=True)
    x_dni_back = fields.Char(
        string="Reverson del DNI", store=True)
    x_nif = fields.Char(
        string="NIF", store=True, size=9)
    x_nss = fields.Char(
        string="Número de Seguridad Social", store=True, size=12)
    x_phone_2 = fields.Char(
        string="Teléfono Secundario", store=True)
    x_port_name = fields.Char(
        string="Nombre completo del titular", store=True)
    x_port_nif = fields.Char(
        string="NIF del titular", store=True)
    x_port_number = fields.Char(
        string="Número a portar", store=True)
    x_port_operator = fields.Char(
        string="Oerador Donante", store=True)
    x_promo = fields.Text(
        string="Promociones / Descuentos", store=True)
    x_promo_price = fields.Float(
        string="Precio Ofertado", store=True)
    x_port_new = fields.Boolean(
        string="Diferente Titular", store=True,
        help="Marca esta casilla si el titular de la línea a portar es diferente")
    # x_contract_file = fields.Binary(
    #     string="Contrato de referencia", store=True)
    x_contract_type = fields.Selection([('hola','hola')])
    x_contract_type_2 = fields.Many2one(
            'custom.contract_types',
            string="Tipo de contrato",
            ondelete="set null",
            store=True,
            domain=[('name', '!=', 'Particular')])
    # x_contract_type_2 = fields.Selection(
    #     selection=_populate_choices,
    #     string="Tipo de contrato", store=True, required=True)
    x_is_new = fields.Selection(
        [('portabilidad', 'Portabilidad'), ('nueva', 'Alta Nueva')],
        string="Fijo a portar", store=True, required=True)


    x_is_new_mobile =  fields.Selection(
        [('portabilidad', 'Portabilidad'), ('nueva', 'Alta Nueva')],
        string="Móvil a portar", store=True)

    x_port_number_mobile = fields.Char(
        string="Número a portar", store=True)
    x_port_operator_mobile = fields.Char(
        string="Oerador Donante", store=True)
    x_port_new_mobile = fields.Boolean(
        string="Diferente Titular", store=True,
        help="Marca esta casilla si el titular de la línea a portar es diferente")
    x_port_name_mobile = fields.Char(
        string="Nombre completo del titular", store=True)
    x_port_nif_mobile = fields.Char(
        string="NIF del titular", store=True)



    x_ba_iban = fields.Char(string="IBAN", store=True, required=True, size=4)
    x_ba_entity = fields.Char(string="C.C.C", store=True, required=True, size=4)
    x_ba_sucursal = fields.Char(string="C.C.C", store=True, required=True, size=4)
    x_ba_control = fields.Char(string="C.C.C", store=True, required=True, size=4)
    x_ba_number = fields.Char(string="C.C.C", store=True, required=True, size=4)
    x_ba_number_2 = fields.Char(string="C.C.C", store=True, required=True, size=4)



    x_ba_full = fields.Char(string="IBAN", store=True, size=29)






    x_operator_tramit = fields.Many2one(
        'custom.operator_tramit',
        string="Operador a tramitar",
        ondelete="set null",
        store=True)

    x_internet_speed = fields.Many2one(
        'custom.internet_speed',
        string="Velocidad de internet",
        ondelete="set null",
        store=True)

    x_internet_speed_status = fields.Selection(
        [('CANCELACION', 'CANCELACION CLIENTE KO COMERCIAL'), ('FIANZA', 'FIANZA'), ('PROGRAMADO', 'PROGRAMADO'), ('ERROR', 'ERROR PORTABILIDAD FIJO'), ('PDTEPROGRAMAR', 'PDTE DE PROGRAMAR'), ('PDTEAPORTAR DOC PARA E7', 'PDTE DE APORTAR DOC PARA E7'), ('IUAE', 'FALTA IUAE'), ('ILOCALIZABLE', 'ILOCALIZABLE')],
        string="Estado", store=True)


    x_mobile_rate = fields.Selection(
        [('mini', 'Tarifa Mini'), ('extra', 'Tarifa Extra'), ('ilimitada', 'Tarifa Ilimitada'), ('super', 'Tarifa Ilimitada Super'), ('total', 'Tarifa Ilimitada Total')],
        string="Tarifa Móvil", store=True)

    x_one_pro = fields.Many2many(
        'custom.one_pro',
        string="Productos ONE Profesional",
        store=True)
    x_one_pro_status = fields.Selection(
        [('CANCELACION', 'CANCELACION CLIENTE KO COMERCIAL'), ('FIANZA', 'FIANZA'), ('PROGRAMADO', 'PROGRAMADO'), ('ERROR', 'ERROR PORTABILIDAD FIJO'), ('PDTEPROGRAMAR', 'PDTE DE PROGRAMAR'), ('PDTEAPORTAR DOC PARA E7', 'PDTE DE APORTAR DOC PARA E7'), ('IUAE', 'FALTA IUAE'), ('ILOCALIZABLE', 'ILOCALIZABLE')],
        string="Estado One Pro", store=True)

    x_tv = fields.Many2many(
        'custom.vf_tv',
        string="Vodafone TV",
        store=True)
    x_tv_status = fields.Selection(
        [('CANCELACION', 'CANCELACION CLIENTE KO COMERCIAL'), ('FIANZA', 'FIANZA'), ('PROGRAMADO', 'PROGRAMADO'), ('ERROR', 'ERROR PORTABILIDAD FIJO'), ('PDTEPROGRAMAR', 'PDTE DE PROGRAMAR'), ('PDTEAPORTAR DOC PARA E7', 'PDTE DE APORTAR DOC PARA E7'), ('IUAE', 'FALTA IUAE'), ('ILOCALIZABLE', 'ILOCALIZABLE')],
        string="Estado TV", store=True)
    x_lines_phone = fields.One2many(
        'custom.phone_line',
        'x_lead_id',
        string="Líneas Adicionales",
        store=True)


    x_virgin_phone = fields.Selection(
        [('conmigo', 'Fijo Conmigo'), ('ilimitado', 'Ilimitado'), ('sinllamada', 'Sin Llamadas')],
        string="Teléfono fijo",
        store=True)

    x_virgin_internet_speed = fields.Many2one(
        'custom.virgin_internet_speed',
        string="Velocidad de internet",
        ondelete="set null",
        store=True)

    x_virgin_mobile_phone = fields.Many2one(
        'custom.virgin_mobile_phone',
        string="Móvil",
        ondelete="set null",
        store=True)

    x_virgin_tv = fields.Many2one(
        'custom.virgin_tv',
        string="Televisión",
        ondelete="set null",
        store=True)





    x_assigned_to = fields.Many2one(
        'res.users',
        string="Asignado a",
        ondelete='set null',
        store=True)

    def _check_iban(self, iban):
        pattern = '[A-Z]{2}[0-9]{22}'
        return re.match(pattern, iban.replace(' ',''))


    def write(self, vals):
        iban = ''
        for elem in ['x_ba_iban' ,'x_ba_entity' ,'x_ba_sucursal' ,'x_ba_control' ,'x_ba_number' ,'x_ba_number_2']:
            if elem in vals:
                iban += vals[elem] + ' '
            else:
                iban += self[elem] + ' '
        iban = iban[:-1].upper()
        if not self._check_iban(iban):
            raise ValidationError(_('El IBAN introducido no es válido.'))

        vals['x_ba_full'] = iban

        return super(Lead, self).write(vals)


    def next_stage(self, stage):
        stages = {
            '1':[9,False],
            '9':[7,True],
            '7':[8,False],
            '8':[6,True],
            '6':[4,False],
        }
        return stages[str(stage)]

    def action_assign(self):
        if self.x_assigned_to:
            raise ValidationError(_('La carga ya ha sido asignada.'))

        if self.stage_id.id == 1:
            self.update({'x_assigned_to':self.env.user.id, 'stage_id':9})
        if self.stage_id.id != 1:
            self.update({'x_assigned_to':self.env.user.id})

        return True


    def action_next_step(self):
        if self.x_assigned_to != self.env.user:
            raise ValidationError(_('No se te ha asignado esta carga.'))
        stage, assignable = self.next_stage(self.stage_id.id)
        if assignable:
            self.sudo().update({'x_assigned_to':False, 'stage_id':stage})
        else:
            self.sudo().update({'stage_id':stage})

        tree_view_id = self.env.ref('crm.crm_case_tree_view_oppor').id
        return {
            'name': _('Cargas'),
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'views': [[False, "tree"], [False,"form"]]
            'view_id': tree_view_id,
            'target':'main'
        }


    @api.model
    def create(self, vals):
        iban = '{} {} {} {} {} {}'.format(vals['x_ba_iban'].upper(), vals['x_ba_entity'], vals['x_ba_sucursal'], vals['x_ba_control'], vals['x_ba_number'], vals['x_ba_number_2'])
        if not self._check_iban(iban):
            raise ValidationError(_('El IBAN introducido no es válido.'))

        vals['x_ba_full'] = iban
        return super(Lead, self).create(vals)


    @api.onchange('x_operator_tramit')
    def onchange_x_operator_tramit(self):
        b ={'domain': {'x_contract_type_2': []}}
        _logger.warning('\n\n{}\n\n'.format(self.x_operator_tramit.name))
        if self.x_operator_tramit.name == 'Vodafone Micro':
            b={'domain': {'x_contract_type_2': [('name', '!=', 'Particular')]}}
        return b
    # def _populate_choices(self):
    #     for record in self:
    #         choices = [('autonomo','Autónomo'), ('empresa', 'Empresa')]
    #         if record['x_operator_tramit'] != 'Vodafone Micro':
    #             choices += [('particular', 'Particular')]
    #
    #     return self

class ContractTypes(models.Model):
    _name = "custom.contract_types"

    name = fields.Char('Nombre', required=True, store=True)

class PhoneLines(models.Model):
    _name = 'custom.phone_line'

    x_aspod = fields.Boolean(string="Penalización ASPOD", store=True)
    x_different_partner = fields.Boolean(string="Diferente Titular", store=True)
    x_icc = fields.Char(string="ICC", store=True)
    x_is_prepaid = fields.Boolean(string="Prepago", store=True)
    x_name = fields.Char(string="Línea Móvil", store=True)
    x_nif = fields.Char(string="NIF del Titular", store=True, size=9)
    x_terminal = fields.Char(string="Terminal", store=True)
    x_titular = fields.Char(string="Nombre del Titular", store=True)
    x_rate = fields.Selection(
        [('mini', 'Tarifa Mini'), ('extra', 'Tarifa Extra'), ('ilimitada', 'Tarifa Ilimitada'), ('super', 'Tarifa Ilimitada Super'), ('total', 'Tarifa Ilimitada Total')],
        string="Tarifa", store=True)
    x_virgin_mobile_phone = fields.Many2one(
        'custom.virgin_mobile_phone',
        string="Tarifa",
        ondelete='set null',
        store=True)
    x_status = fields.Selection(
        [('activa', 'ACTIVA'), ('ko', 'KO DUDA COMERCIAL'), ('error', 'RECHAZO - ERROR DE PORTABILIDAD'), ('nostock', 'SIN STOCK TERMINAL'), ('tramite', 'PORTABILIDA EN TRÁMITE')],
        string="Estado", store=True)


    x_lead_id = fields.Many2one(
        'crm.lead',
        string="Referencia",
        ondelete="set null",
        store=True)



class OnePro(models.Model):
    _name = 'custom.one_pro'
    _description = 'Productos One Pro'


    name = fields.Char(string='Nombre', store=True)
    code = fields.Char(string='Código Interno', store=True)


class VFTV(models.Model):
    _name = 'custom.vf_tv'
    _description = 'Productos Vodafone TV'

    name = fields.Char(string='Nombre', store=True)
    code = fields.Char(string='Código Interno', store=True)


class OperatorTramit(models.Model):
    _name = 'custom.operator_tramit'
    _description = 'Operadores tramitables'

    name = fields.Char(string='Nombre', store=True)
    code = fields.Char(string='Código Interno', store=True)


class InternetSpeed(models.Model):
    _name = 'custom.internet_speed'
    _description = 'Velocidades de Internet'

    name = fields.Char(string='Nombre', store=True)
    code = fields.Char(string='Código Interno', store=True)

# VIRGIN
class VirginInternetSpeed(models.Model):
    _name = 'custom.virgin_internet_speed'
    _description = 'Velocidades de Internet'

    name = fields.Char(string='Nombre', store=True)
    code = fields.Char(string='Código Interno', store=True)


class VirginMobilePhone(models.Model):
    _name = 'custom.virgin_mobile_phone'
    _description = 'Móvil'

    name = fields.Char(string='Nombre', store=True)
    code = fields.Char(string='Código Interno', store=True)


class VirginTV(models.Model):
    _name = 'custom.virgin_tv'
    _description = 'Televisión'

    name = fields.Char(string='Nombre', store=True)
    code = fields.Char(string='Código Interno', store=True)
