# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdvansysCourse(models.Model):
    _name = 'advansys.skill'

    @api.depends('blue')
    def _computed_stauts(self):
        for rec in self:
            if rec.blue==True:
                rec.status = 'Active'  # so this is always executed, but it does nothing
            else:
                rec.status = 'Not Active'

    name = fields.Char(required=True)
    desc = fields.Text()

    blue = fields.Boolean('Blue')
    status=fields.Char(compute=_computed_stauts);


    # pink = fields.Boolean('Pink')
    #
    # yellow = fields.Boolean('Yellow')

    # course_season_id = fields.One2many('advansys.advansys.course.season')
    #


    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100
