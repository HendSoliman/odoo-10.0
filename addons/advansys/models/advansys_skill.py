# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdvansysCourse(models.Model):
    _name = 'advansys.skill'

    name = fields.Char(required=True)
    desc = fields.Text()

    # course_season_id = fields.One2many('advansys.advansys.course.season')
    #


    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100
