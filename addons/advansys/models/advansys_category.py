# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysCategory(models.Model):
     _name = 'advansys.category'

     name = fields.Char(required=True)
     desc=fields.Text()

     # Relation according to sub
     subcategory_ids = fields.One2many('advansys.subcategory', 'category_id')

     #     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100