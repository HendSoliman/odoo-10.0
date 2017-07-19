# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysTMSCourseVersion(models.Model):
     _name = 'advansystms.course.version'

     _rec_name = 'version'
     version = fields.Integer()
     effective_date=fields.Date(default=fields.Date.context_today)

     course_version_id = fields.Many2one('advansystms.course')



     #     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100