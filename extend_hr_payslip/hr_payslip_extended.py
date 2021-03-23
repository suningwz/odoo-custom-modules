# -*- coding: utf-8 -*-
from odoo import fields, models, api
import datetime
from datetime import timedelta
import logging
#
_logger = logging.getLogger(__name__)


class PaySlip(models.Model):
    _inherit = 'hr.payslip'


    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))
    x_brute = fields.Monetary(string="Bruto", store=True)
    x_ss = fields.Monetary(string="Seguridad Social", store=True)
    x_prorrate = fields.Monetary(string="Prorrateo", store=True)
    x_prorrate_vacations = fields.Monetary(string="Prorrateo Vacaciones", store=True)
    x_incentive = fields.Monetary(string="Incentivo fijo", store=True)


    x_worked_hours = fields.Float(string="Horas trabajadas totales", store=True)
    x_worked_extra = fields.Float(string="Horas extra", store=True)
    x_worked_special = fields.Float(string="Horas especiales", store=True)
    x_worked_holiday = fields.Float(string="Horas festivas", store=True)
    x_worked_saturday = fields.Float(string="Horas sabados", store=True)
    x_worked_extra_price = fields.Monetary(string="a", store=True)
    x_worked_special_price = fields.Monetary(string="a", store=True)
    x_worked_holiday_price = fields.Monetary(string="a", store=True)
    x_worked_saturday_price = fields.Monetary(string="a", store=True)
    x_worked_extra_total = fields.Monetary(string="=", store=True)
    x_worked_special_total = fields.Monetary(string="=", store=True)
    x_worked_holiday_total = fields.Monetary(string="=", store=True)
    x_worked_saturday_total = fields.Monetary(string="=", store=True)


    x_cost_per_hour = fields.Monetary(string="Coste por hora trabajada", store=True)


    x_payslip_total = fields.Monetary(string="Total", store=True)

    @api.onchange('employee_id')
    def onchange_employee_id(self):
        self.x_payslip_total = 0
        self.x_cost_per_hour = 0
        if self.employee_id:
            employee = self.env['hr.employee'].browse(self.employee_id.id)
            if employee:
                self.x_incentive = employee.hr_employee_salary_fix_plus
                self.x_prorrate = employee.hr_employee_salary_extra_payments / 12
                self.x_prorrate_vacations = employee.hr_employee_salary_holidays / 12

                self.x_worked_extra_price = employee.hr_employee_salary_extra
                self.x_worked_special_price = employee.hr_employee_salary_special
                self.x_worked_holiday_price = employee.hr_employee_salary_festive
                self.x_worked_saturday_price = employee.hr_employee_salary_saturday



    @api.onchange('employee_id', 'date_from', 'date_to')
    def onchange_employee_or_date(self):
        self.x_worked_hours = 0
        self.x_worked_extra = 0
        self.x_worked_special = 0
        self.x_worked_holiday = 0
        self.x_worked_saturday = 0
        self.x_worked_holiday_total = 0
        self.x_worked_extra_total = 0
        self.x_worked_special_total = 0
        self.x_worked_saturday_total = 0

        daily_hours = self.employee_id.hr_employee_daily_hours

        calendar = self.env['calendar.event'].search([('x_is_holiday','=','True'), ('start_date','>=',self.date_from), ('stop_date','<=',self.date_to)])
        festives = []
        fmt = '%Y-%m-%d'
        for evnt in calendar:
            d1 = datetime.datetime.strptime(evnt.start_date, fmt)
            d2 = datetime.datetime.strptime(evnt.stop_date, fmt)
            delta = d2 - d1
            for i in range(delta.days + 1):
                festives.append((d1 + timedelta(days=i)).strftime('%Y-%m-%d'))

        if self.employee_id and self.date_from and self.date_to:
            timesheets = self.env['account.analytic.line']
            timesheets_id = timesheets.search([('employee_id','=',self.employee_id.id), ('date','>=',self.date_from), ('date','<=',self.date_to)], order='date asc')
            if timesheets_id:
                currdate = timesheets_id[0].date
            worked_hours_day = 0

            for i, timesheet in enumerate(timesheets_id):
                ts = timesheets.browse(timesheet.id)
                _logger.warning('\n{}>{}\n'.format(currdate, ts.date))
                self.x_worked_hours += ts.unit_amount
                wkday = datetime.datetime.strptime(ts.date, '%Y-%m-%d').weekday()

                if ts.x_special_hour:
                    self.x_worked_special += ts.unit_amount
                    self.x_worked_special_total += ts.unit_amount * self.x_worked_special_price

                elif wkday == 6 or ts.date in festives:
                    self.x_worked_holiday += ts.unit_amount
                    self.x_worked_holiday_total += ts.unit_amount * self.x_worked_holiday_price

                elif wkday == 5:
                    self.x_worked_saturday += ts.unit_amount
                    self.x_worked_saturday_total += ts.unit_amount * self.x_worked_saturday_price

                elif currdate == ts.date:
                    worked_hours_day += ts.unit_amount
                else:
                    if worked_hours_day > daily_hours:
                        self.x_worked_extra += worked_hours_day - daily_hours
                        self.x_worked_extra_total += (worked_hours_day - daily_hours) * self.x_worked_extra_price
                    worked_hours_day = ts.unit_amount
                    currdate = ts.date

                if (i + 1) == len(timesheets_id):
                    if worked_hours_day > daily_hours:
                        self.x_worked_extra += worked_hours_day - daily_hours
                        self.x_worked_extra_total += (worked_hours_day - daily_hours) * self.x_worked_extra_price



    @api.onchange('x_brute', 'x_ss', 'x_prorrate', 'x_prorrate_vacations', 'x_incentive')
    def onchange_costs(self):
        self.x_payslip_total = self.x_brute + self.x_ss + self.x_prorrate + self.x_prorrate_vacations + self.x_incentive + self.x_worked_extra_total + self.x_worked_special_total + self.x_worked_holiday_total + self.x_worked_saturday_total
        if self.x_worked_hours:
            self.x_cost_per_hour = self.x_payslip_total / self.x_worked_hours
        else:
            self.x_cost_per_hour = 0
