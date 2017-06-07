# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdvansysEmployee(models.Model):
    _name = 'advansys.employee'

    @api.depends('gender')
    def _computed_salary(self):
        for record in self:
            if self.gender=='m':
                 self.salary=5000
            else:
                self.salary=8000

    @api.onchange('gender')
    def onChange_gender(self):
        domain = [('id', 'in', [])]
        if self.gender == 'm':
            domain = []
            return {
                'domain': {'departmen_id': domain}
            }

    name = fields.Char(string="Employee Name", required=True)
    age = fields.Integer()
    email = fields.Char()
    title = fields.Char()
    salary = fields.Float(compute=_computed_salary)
    image = fields.Binary()
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
    ], default='m')
    # desc = fields.Text(default='Default Description')
    join_data = fields.Datetime(required=True)
    date_of_birth = fields.Date(default=fields.Date.context_today)
    is_accepted = fields.Boolean()
    bio = fields.Html()
    state = fields.Selection([
        ('apply', 'Applied'),
        ('iq', 'Passed IQ'),
        ('tech', 'Passed Technical'),
        ('refused', 'Refused'),
        ('accepted', 'Accepted'),
    ], default='apply')

    # Relations btw Employee & Department
    # ================Many2one
    departmen_id = fields.Many2one('advansys.department')
    departmen_desc=fields.Text(related='departmen_id.desc',store=True,readonly=True)



    # Relation btw Employee & project
    #==================Many2many
    project_ids = fields.Many2many('advansys.project')
    employee_skill_level_id = fields.One2many('advansys.employee.skill.level', 'employee_id')
