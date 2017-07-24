# -*- coding: utf-8 -*-
from odoo import http

# class AdvansysTms(http.Controller):
#     @http.route('/advansystms/advansystms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advansystms/advansystms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('advansys_tms.listing', {
#             'root': '/advansystms/advansystms',
#             'objects': http.request.env['advansystms.advansystms'].search([]),
#         })

#     @http.route('/advansystms/advansystms/objects/<model("advansystms.advansystms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advansys_tms.object', {
#             'object': obj
#         })