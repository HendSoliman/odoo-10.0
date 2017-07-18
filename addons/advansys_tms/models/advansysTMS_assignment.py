# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysTMSassignment(models.Model):
     _name = 'advansystms.assignment'

     # course_id=fields.Many2one('advansystms.course')
     # employee_type_id = fields.Many2one('advansystms.employee.type')
     # department_id = fields.Many2one('advansystms.department')
     # course_version_id=fields.One2many('advansystms.course.version')

#      retraining_frequency=fields.selection(
#          [('one', 'One'),
#           ('two', 'Two')],
#          'Syllabus'),
#
#
# XML
# Code:
#
# < field
# name = "syllabus"
# widget = "radio" / >




     # departmen_desc = fields.Text(related='departmen_id.desc', store=True, readonly=True)



     #     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100