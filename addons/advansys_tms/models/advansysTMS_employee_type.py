# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysTMSEmployeeType(models.TransientModel):
     _name = 'advansystms.employee.type'

     _rec_name = 'type_code'
     type_code=fields.Char()
     type_title=fields.Char()
     description =fields.Char()


