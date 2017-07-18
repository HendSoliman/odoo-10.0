# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysTMSCategory(models.Model):
     _name = 'advansystms.category'


     @api.one
     def active_category(self):
          new_state = 'active'
          self.write({'status': new_state})

     @api.one
     def Inactive_category(self):
          new_state = 'Inactive'
          self.write({'status': new_state})

     def show_active_courses_action(self):
          active_courses = self.env['advansystms.course'].search([('category_id', '=', self.id)])
          courses_Objects = []
          for emp in active_courses:
               if emp.status =='active':
                    courses_Objects.append(emp.id)
                    print emp.title, "************"
          return {
               'name': 'Active courses',
               'type': 'ir.actions.act_window',
               'res_model': 'advansystms.course',
               'view_mode': 'tree, form',
               'domain': [('id', 'in', courses_Objects)]
          }




     name = fields.Char(required=True)
     # active = fields.Boolean('Active')
     # status = fields.Char(compute=_computed_stauts);
     status = fields.Selection([
          ('active', 'Active'),
          ('Inactive', 'Inactive'),
     ], default='active')

     # Relation according to  course
     course_ids = fields.One2many('advansystms.course', 'category_id')

