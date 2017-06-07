# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysDepartment(models.Model):
     _name = 'advansys.department'

     name = fields.Char(required=True)
     desc=fields.Text()

     # Relation according to employee
     employee_ids=fields.One2many('advansys.employee','departmen_id')

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100