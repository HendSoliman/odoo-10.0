# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdvansysSkillLevel(models.Model):
    _name = 'advansys.employee.skill.level'




    name = fields.Char()

    employee_id = fields.Many2one('advansys.employee')
    skill_id = fields.Many2one('advansys.skill')
    level = fields.Selection(
        [
            ('a', 'A'),
            ('b', 'B'),
            ('c', 'C'),
            ('d', 'D'),

        ]

    )


    # employee_project_ids = fields.Many2many('advansys.employee', 'project_ids')


    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100
