# -*- coding: utf-8 -*-
from odoo import api, fields, models
#
# import logging
# _logger = logging.getLogger(__name__)
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
        string="NIF del autorizado", store=True, size=24)

    x_charge_code = fields.Char(
        string="Código de carga", store=True)
    x_cif = fields.Char(
        string="CIF", store=True)
    x_client_name = fields.Char(
        string="Nombre del cliente", store=True, required=True)
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
    x_contract_file = fields.Binary(
        string="Contrato de referencia", store=True)
    x_contract_type = fields.Selection(
        [('autonomo','Autónomo'), ('empresa', 'Empresa'), ('particular', 'Particular')],
        string="Tipo de contrato", store=True, required=True)
    x_is_new = fields.Selection(
        [('fibra','Solo Fibra'), ('portabilidad', 'Portabilidad'), ('nueva', 'Alta Nueva')],
        string="Tipo de número", store=True)



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

    x_one_pro = fields.Many2one(
        'custom.one_pro',
        string="Productos ONE Profesional",
        ondelete="set null",
        store=True)

    x_tv = fields.Many2one(
        'custom.vf_tv',
        string="Vodafone TV",
        ondelete="set null",
        store=True)

    x_lines_phone = fields.One2many(
        'custom.phone_line',
        'x_lead_id',
        string="Líneas Adicionales",
        store=True)



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

    x_name = fields.Char(string='Nombre', store=True)


class VFTV(models.Model):
    _name = 'custom.vf_tv'

    x_name = fields.Char(string='Nombre', store=True)


class OperatorTramit(models.Model):
    _name = 'custom.operator_tramit'

    x_name = fields.Char(string='Nombre', store=True)


class InternetSpeed(models.Model):
    _name = 'custom.internet_speed'

    x_name = fields.Char(string='Nombre', store=True)
    x_code = fields.Char(string='Código Interno', store=True)
