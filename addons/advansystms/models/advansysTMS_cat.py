# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysTMSCourse(models.Model):
     _name = 'advansystms.cat'

     name=fields.Char(required=True)
     status = fields.Selection([
          ('active', 'Active'),
          ('Inactive', 'Inactive'),
     ], default='active')


     notes=fields.Text()
     # Relation according to  course
     course_ids = fields.One2many('advansystms.course', 'category_id')

     @api.one
     def active_category(self):
          new_state = 'active'
          self.write({'status': new_state})

     @api.one
     def Inactive_category(self):
          new_state = 'Inactive'
          self.write({'status': new_state})

     @api.multi
     def _computed_numbers(self):
          for rec in self:
               rec.number_of_courses = len(rec.course_ids)
          print rec.number_of_courses

     number_of_courses = fields.Char(compute=_computed_numbers, readonly=True)
