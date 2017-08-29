# -*- coding: utf-8 -*-
#auther : Hend Soliman
import base64
from random import choice
from string import digits

from odoo import models, fields, api, exceptions, _, SUPERUSER_ID

class AdvansysPerson(models.Model):
    _name = 'advansys.person'


    def _default_random_barcode(self):
        barcode = None
        while not barcode or self.env['advansys.person'].search([('barcode', '=', barcode)]):
            barcode = "".join(choice(digits) for i in range(8))
        return barcode

    name = fields.Char(required=True)
    barcode = fields.Char(string="Badge ID", help="ID used for employee identification.",
                          default=_default_random_barcode, copy=False)



