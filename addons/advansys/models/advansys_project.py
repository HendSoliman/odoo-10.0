# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AdvansysProject(models.Model):
     _name = 'advansys.project'

     name = fields.Char( required=True)
     desc=fields.Text()
     technology_used=fields.Text()

     employee_ids = fields.Many2many('advansys.employee')
     # , 'project_ids'
     employee_contact = fields.Char(related='employee_ids.phone', store=True, readonly=True)

     #     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100