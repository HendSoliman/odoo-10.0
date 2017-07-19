# -*- coding: utf-8 -*-
from odoo import http

# class AdvansysTms(http.Controller):
#     @http.route('/advansys_tms/advansys_tms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advansys_tms/advansys_tms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('advansys_tms.listing', {
#             'root': '/advansys_tms/advansys_tms',
#             'objects': http.request.env['advansys_tms.advansys_tms'].search([]),
#         })

#     @http.route('/advansys_tms/advansys_tms/objects/<model("advansys_tms.advansys_tms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advansys_tms.object', {
#             'object': obj
#         })