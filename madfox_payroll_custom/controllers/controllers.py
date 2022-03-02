# -*- coding: utf-8 -*-
# from odoo import http


# class MadfoxPayrollCustom(http.Controller):
#     @http.route('/madfox_payroll_custom/madfox_payroll_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/madfox_payroll_custom/madfox_payroll_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('madfox_payroll_custom.listing', {
#             'root': '/madfox_payroll_custom/madfox_payroll_custom',
#             'objects': http.request.env['madfox_payroll_custom.madfox_payroll_custom'].search([]),
#         })

#     @http.route('/madfox_payroll_custom/madfox_payroll_custom/objects/<model("madfox_payroll_custom.madfox_payroll_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('madfox_payroll_custom.object', {
#             'object': obj
#         })
