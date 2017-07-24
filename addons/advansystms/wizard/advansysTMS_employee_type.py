# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysTMSEmployeeType(models.Model):
     _name = 'advansystms.employee.type'

     _rec_name = 'type_code'
     type_code=fields.Char(required=True)
     type_title=fields.Char(required=True)
     description =fields.Char()


