# -*- coding: utf-8 -*-
from odoo import http


class Advansys(http.Controller):
    @http.route('/advansys/advansys/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/advansys/advansys/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('advansys.listing', {
            'root': '/advansys/advansys',
            'objects': http.request.env['advansys.advansys'].search([]),
        })

    @http.route('/advansys/advansys/objects/<model("advansys.advansys"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('advansys.object', {
            'object': obj
        })
