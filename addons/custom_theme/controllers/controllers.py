# -*- coding: utf-8 -*-
from odoo import http

# class ThemeTutorial(http.Controller):
#     @http.route('/custom_theme/custom_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_theme/custom_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_theme.listing', {
#             'root': '/custom_theme/custom_theme',
#             'objects': http.request.env['custom_theme.custom_theme'].search([]),
#         })

#     @http.route('/custom_theme/custom_theme/objects/<model("custom_theme.custom_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_theme.object', {
#             'object': obj
#         })