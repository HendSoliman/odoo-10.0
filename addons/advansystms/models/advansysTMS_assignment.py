# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdvansysTMSassignment(models.Model):
    _name = 'advansystms.assignment'

    dueDate = fields.Selection([
        ('immediately', 'Immediately'),
        ('on_date', 'Onspecificdate'),
    ], default='immediately')
    course_id = fields.Many2one('advansystms.course')
    course_version_id = fields.One2many('advansystms.course.version','course_version_id')
    employee_type_id = fields.Many2one('advansystms.employee.type')
    department_id = fields.Many2one('advansystms.department')
    status = fields.Selection([
        ('active', 'Active'),
        ('Inactive', 'Inactive'),
    ], default='active')


    due =fields.Datetime()





# retraining_frequency=fields.selection(
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
