# -*- coding: utf-8 -*-
from odoo import fields, models

class WokerHolidays(models.Model):

    _name = 'custom.worker_holidays'

    related_employee = fields.Many2one('hr.employee', string='Empleado asociado', ondelete='set null', stored=True)
    start_date = fields.Date(string='Fecha de inicio', stored=True)
    end_date = fields.Date(string='Fecha de fin', stored=True)


class Partner(models.Model):
    _inherit = 'hr.employee'

#DIRECCION
    hr_employee_private_address = fields.Char(string="Dirección Personal", placeholder="Calle...", store=True)
    hr_employee_private_address_2 = fields.Char(string="Calle 2...", store=True)
    hr_employee_private_address_localidad = fields.Char(string="Localidad", store=True)
    hr_employee_private_address_provincia = fields.Char(string="Provincia", store=True)
    hr_employee_private_address_zip = fields.Char(string="C.P.", size=5, store=True)
#NIF
    hr_employee_nif = fields.Char(string='NIF', size=9, store=True)
#NSS
    hr_employee_nss = fields.Char(string='Número de Seguridad Social', store=True)
#PHONE
    hr_employee_private_phone_1 = fields.Char(string='1º Teléfono particular', store=True)
    hr_employee_private_phone_2 = fields.Char(string='2º Teléfono particular', store=True)
    hr_employee_private_email = fields.Char(string='Email personal', store=True)
# PERSONA DE CONTACTO
    hr_employee_contact_name = fields.Char(string='Persona de contacto', store=True)
    hr_employee_contact_phone = fields.Char(string='Teléfono contacto', store=True)
#IBAN
    hr_employee_iban = fields.Char(string='IBAN', size=24, store=True)
#CATEGORIA
    hr_employee_category = fields.Char(string='Categoría laboral', store=True)
    hr_employee_expertise = fields.Char(string='Especialidad laboral', store=True)
    hr_employee_formation = fields.Char(string='Formación PRL', store=True)
#CONTRATO
    hr_employee_last_contract_date = fields.Date(string='Fecha del último contrato', store=True)
    hr_employee_contract_type = fields.Char(string='Tipo de contrato en vigor', store=True)
#ROPA
    hr_employee_clothes_size = fields.Char(string='Tallas de ropa laboral', store=True)
    hr_employee_date_trousers = fields.Date(string='Fecha de entrega pantalón', store=True)
    hr_employee_date_jacket = fields.Date(string='Fecha de entrega forro', store=True)
    hr_employee_date_shirt_ml = fields.Date(string='Fecha de entrega camiseta M/L', store=True)
    hr_employee_date_shirt_mc = fields.Date(string='Fecha de entrega camiseta M/C', store=True)
    hr_employee_date_shoes = fields.Date(string='Fecha de entrega calzado seguridad', store=True)
#RECONOCIMIENTO
    hr_employee_date_recon = fields.Date(string='Fecha de último reconocimiento', store=True)
#SUELDO
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))
    # timesheet_cost = fields.Monetary(string="Precio por Hora", store=True)
    hr_employee_salary_extra = fields.Monetary(string="Precio por Hora extra", store=True)
    hr_employee_salary_special = fields.Monetary(string="Precio por Hora especial", store=True)
    hr_employee_salary_festive = fields.Monetary(string="Precio por Hora festiva", store=True)
    hr_employee_salary_saturday = fields.Monetary(string="Precio por Hora sábado", store=True)
    hr_employee_salary_fix_plus = fields.Monetary(string="Incentivo fijo", store=True)
    hr_employee_salary_holidays = fields.Char(string="Pagas de vacaciones", store=True)
    # hr_employee_salary_ss = fields.Monetary(string="Impuesto seguridad social", store=True)
    hr_employee_salary_extra_payments = fields.Monetary(string="Pagas extra", store=True)

#HORAS EXTRA
    # hr_employee_extra_hours = fields.(string="Número de horas extra", store=True)

    hr_employee_holidays = fields.One2many('custom.worker_holidays', 'related_employee', string="Vacaciones", store=True)
