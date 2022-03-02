# -*- coding: utf-8 -*-

from odoo import models, fields, api


class madfox_payroll_custom(models.Model):
    _inherit = 'hr.payslip'
    
    
    bank_loan = fields.Float(string='Bank Loan')
    Adv_salary = fields.Float(string='Advance Salary')
    cmp_loan = fields.Float(string='Company Loan')


   
