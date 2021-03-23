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

    name = fields.Char(string="Comercial", store=True)


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

    x_lead_products = fields.One2many(
        'custom.user_products',
        'lead_id',
        string="Productos",
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

    x_virgin_tv = fields.Many2many(
        'custom.virgin_tv',
        string="Televisión",
        store=True)





    x_assigned_to = fields.Many2one(
        'res.users',
        string="Asignado a",
        ondelete='set null',
        store=True)

    def _check_iban(self, unchecked_iban):
        if iban == 'ES0000000000000000000000':
            return True
        unchecked_iban = unchecked_iban.replace(' ', '')
        LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}
        def _number_iban(iban):
           return (iban[4:] + iban[:4]).translate(LETTERS)
        def generate_iban_check_digits(iban):
           number_iban = _number_iban(iban[:2] + '00' + iban[4:])
           return '{:0>2}'.format(98 - (int(number_iban) % 97))
        def valid_iban(iban):
           return int(_number_iban(iban)) % 97 == 1
        return generate_iban_check_digits(unchecked_iban) == unchecked_iban[2:4] and valid_iban(unchecked_iban)



    def next_stage(self, stage):
        stages = {
            '1':[9,False], # NEW
            '9':[8,True], # CALIDAD
            '8':[6,True], # PDTE CARGA
            '6':[7,False], # CARGADO
            '7':[4,False], # PDTE FIRMA
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

        if self.stage_id.id == 6:
            self.create_products(self)

        tree_view_id = self.env.ref('crm.crm_case_tree_view_oppor').id
        return {
            'name': _('Cargas'),
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'views': [[False, "tree"], [False,"form"]],
            'view_id': tree_view_id,
            'target':'main'
        }


    def create_products(self):

        rec = {
            'lead_id': self.id,
            'operator': self.x_operator_tramit.id,
            # 'client_id': self.x_address_id,
            'nif': self.x_nif,
            'name': self.x_client_name,
            'address': '{} {}'.format(self.street, self.street2),
            'city': self.city
        }

        # x_virgin_internet_speed
        if self.x_virgin_internet_speed:
            rec['type_parent'] = 'x_virgin_internet_speed'
            rec['code'] = self.x_virgin_internet_speed.code
            rec['product'] = self.x_virgin_internet_speed.name
            rec['phone'] = ''
            self.env['custom.user_products'].sudo().create(rec)

        # x_virgin_tv
        for elem in self.x_virgin_tv:
            rec['type_parent'] = 'x_virgin_tv'
            rec['code'] = elem.code
            rec['product'] = elem.name
            rec['phone'] = ''
            self.env['custom.user_products'].sudo().create(rec)

        # x_virgin_phone
        if self.x_virgin_phone:
            rec['type_parent'] = 'x_virgin_phone'
            rec['code'] = ''
            rec['product'] = self.x_virgin_phone
            rec['phone'] = self.x_port_number
            self.env['custom.user_products'].sudo().create(rec)

        # x_virgin_mobile_phone
        if self.x_virgin_mobile_phone:
            rec['type_parent'] = 'x_virgin_mobile_phone'
            rec['code'] = self.x_virgin_mobile_phone.code
            rec['product'] = self.x_virgin_mobile_phone.name
            rec['phone'] = self.x_port_number_mobile
            self.env['custom.user_products'].sudo().create(rec)

        for line in self.x_lines_phone:
            rec['type_parent'] = 'x_virgin_mobile_phone_extra'
            rec['code'] = line.x_virgin_mobile_phone.code
            rec['product'] = line.x_virgin_mobile_phone.name
            rec['phone'] = line.x_name
            self.env['custom.user_products'].sudo().create(rec)



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


    @api.model
    def create(self, vals):

        _logger.warning('\n\n{}\n\n'.format(vals['x_files'][0][2]))
        _logger.warning('\n\n{}\n\n'.format(len(vals['x_files'])))
        if len(vals['x_files'][0][2]) < 1:
            raise ValidationError(_('Debes introducir al menos un documento adjunto.'))

        iban = '{} {} {} {} {} {}'.format(vals['x_ba_iban'].upper(), vals['x_ba_entity'], vals['x_ba_sucursal'], vals['x_ba_control'], vals['x_ba_number'], vals['x_ba_number_2'])
        if not self._check_iban(iban):
            raise ValidationError(_('El IBAN introducido no es válido.'))

        vals['x_ba_full'] = iban

        # lead = super(Lead, self).create(vals)

        # REPEATED VALUES
        # rec = {
        #     'lead_id': lead.id,
        #     'operator': lead.x_operator_tramit.id,
        #     # 'client_id': lead.x_address_id,
        #     'nif': lead.x_nif,
        #     'name': lead.x_client_name,
        #     'address': '{} {}'.format(lead.street, lead.street2),
        #     'city': lead.city
        # }
        #
        # # x_virgin_internet_speed
        # if lead.x_virgin_internet_speed:
        #     rec['type_parent'] = 'x_virgin_internet_speed'
        #     rec['code'] = lead.x_virgin_internet_speed.code
        #     rec['product'] = lead.x_virgin_internet_speed.name
        #     rec['phone'] = ''
        #     self.env['custom.user_products'].sudo().create(rec)
        #
        # # x_virgin_tv
        # for elem in lead.x_virgin_tv:
        #     rec['type_parent'] = 'x_virgin_tv'
        #     rec['code'] = elem.code
        #     rec['product'] = elem.name
        #     rec['phone'] = ''
        #     self.env['custom.user_products'].sudo().create(rec)
        #
        # # x_virgin_phone
        # if lead.x_virgin_phone:
        #     rec['type_parent'] = 'x_virgin_phone'
        #     rec['code'] = ''
        #     rec['product'] = lead.x_virgin_phone
        #     rec['phone'] = lead.x_port_number
        #     self.env['custom.user_products'].sudo().create(rec)
        #
        # # x_virgin_mobile_phone
        # if lead.x_virgin_mobile_phone:
        #     rec['type_parent'] = 'x_virgin_mobile_phone'
        #     rec['code'] = lead.x_virgin_mobile_phone.code
        #     rec['product'] = lead.x_virgin_mobile_phone.name
        #     rec['phone'] = lead.x_port_number_mobile
        #     self.env['custom.user_products'].sudo().create(rec)
        #
        # for line in lead.x_lines_phone:
        #     rec['type_parent'] = 'x_virgin_mobile_phone_extra'
        #     rec['code'] = line.x_virgin_mobile_phone.code
        #     rec['product'] = line.x_virgin_mobile_phone.name
        #     rec['phone'] = line.x_name
        #     self.env['custom.user_products'].sudo().create(rec)

        return super(Lead, self).create(vals)
        # return lead_id


    @api.onchange('x_operator_tramit')
    def onchange_x_operator_tramit(self):
        b ={'domain': {'x_contract_type_2': []}}
        # _logger.warning('\n\n{}\n\n'.format(self.x_operator_tramit.name))
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
        [('activa', 'ACTIVA'), ('ko', 'KO DUDA COMERCIAL'), ('error', 'RECHAZO - ERROR DE PORTABILIDAD'), ('nostock', 'SIN STOCK TERMINAL'), ('tramite', 'PORTABILIDAD EN TRÁMITE')],
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


class Statuses(models.Model):
    _name = "custom.statuses"
    _description = 'Estados de seguimiento'

    name = fields.Char(string="Nombre", store=True)


class UserProducts(models.Model):
    _name = 'custom.user_products'
    _description = "Productos"

    lead_id = fields.Many2one('crm.lead', string='Contrato de referencia', ondelete="cascade", store=True)
    operator = fields.Many2one('custom.operator_tramit', string="Operador a tramitar", ondelete='set null', store=True)
    type_parent = fields.Char(string="Campo padre", store=True)
    loaded = fields.Boolean(string="Cargado", store=True)
    code = fields.Char(string='Código Interno', store=True)

    recording_date = fields.Datetime(string="Fecha de grabación", store=True)
    # status_parent = fields.Char(string="Estado", store=True)
    status_parent = fields.Selection([('CARGADO', 'CARGADO'), ('ACTIVO', 'ACTIVO'), ('CANCELADO', 'CANCELADO')], string="Estado", store=True)
    status_comment = fields.Char(string="Comentario", store=True)
    # status = fields.Many2one('custom.statuses', string="Estado", store=True)
    effective_date = fields.Datetime(string="Fecha de activación", store=True)

    client_id = fields.Char(string="ID Cliente", store=True)
    nif = fields.Char(string='CIF/NIE/NIF', store=True)
    name = fields.Char(string="Cliente", store=True)

    address = fields.Char(string="Dirección", store=True)
    city = fields.Char(string="Población", store=True)

    product = fields.Char(string="Producto", store=True)
    phone = fields.Char(string="Porta/Nueva", store=True)


    # @api.onchange('parent_type')
    # def onchange_x_operator_tramit(self):
    #     b ={'domain': {'status': []}}
    #     if self.parent_type == 'x_internet_speed':
    #         b={'domain': {'status': [('name', 'in', [''])]}}
    #
    #     elif self.parent_type in ['x_virgin_internet_speed','x_virgin_tv']:
    #         b={'domain': {'status': [('name', 'in', [
    #         'CANCELACION CLIENTE KO COMERCIAL', 'FIANZA', 'PROGRAMADO', 'ERROR', 'PDTE DE PROGRAMAR', 'PDTE DE APORTAR DOC PARA E7', 'FALTA IUAE', 'ILOCALIZABLE'
    #         ])]}}
    #
    #     elif self.parent_type == 'x_virgin_mobile_phone':
    #         b={'domain': {'status': [('name', 'in', [
    #         'PORTABILIDAD EN TRÁMITE', 'KO DUDA COMERCIAL', 'RECHAZO-ERROR DE PORTABILIDAD', 'ACTIVA', 'SIN STOCK TERMINAL'
    #         ])]}}
    #
    #     elif self.parent_type == 'x_virgin_phone':
    #         b={'domain': {'status': [('name', 'in', [
    #         'PORTABILIDAD EN TRÁMITE', 'KO DUDA COMERCIAL', 'RECHAZO-ERROR DE PORTABILIDAD', 'ACTIVA'
    #         ])]}}
    #
    #
    #
    #     return b
