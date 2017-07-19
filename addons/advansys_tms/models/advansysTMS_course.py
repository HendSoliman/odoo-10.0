# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysTMSCourse(models.Model):
     _name = 'advansystms.course'

     _rec_name = 'title'
     title = fields.Char(required=True)
     description =fields.Text()
     number=fields.Char()
     status = fields.Selection([
          ('active', 'Active'),
          ('Inactive', 'Inactive'),
     ], default='active')

     fixed_cost=fields.Float()
     per_student_cost=fields.Float()
     notes=fields.Text()
     pass_threshold=fields.Float()
     notes=fields.Text()
     # attachment = fields.Binary()

     category_id=fields.Many2one('advansystms.cat' ,required=True)

     # departmen_desc = fields.Text(related='departmen_id.desc', store=True, readonly=True)



     #     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100