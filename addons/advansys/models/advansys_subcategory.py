# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysSubCategory(models.Model):
     _name = 'advansys.subcategory'

     name = fields.Char(required=True)
     desc=fields.Text()

     # Relation according to employee
     category_id=fields.Many2one('advansys.category')



#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100