# -*- coding: utf-8 -*-
from datetime import datetime, date

import dateutil
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class AdvansysEmployee(models.Model):
    _name = 'advansys.employee'

    @api.depends('gender')
    def _computed_salary(self):
        for record in self:
            if self.gender == 'm':
                self.salary = 5000
            else:
                self.salary = 8000

                # To compute Age Automatically

    @api.depends('date_of_birth')
    def _computed_age(self):
        for rec in self:
            if rec.date_of_birth:
                dt = rec.date_of_birth
        d1 = datetime.strptime(dt, "%Y-%m-%d").date()
        d2 = date.today()
        rd = relativedelta(d2, d1)
        rec.age = str(rd.years) + ' years\t' + str(rd.months) + 'months'

    @api.onchange('gender')
    def onChange_gender(self):
        print 'On Onchage method'
        domain = [('desc', '!=', False)]
        if self.gender == 'm':
            domain = []  # no condition  show all
        return {
            'domain': {'departmen_id': domain}
        }



    name = fields.Char(string="Employee Name", required=True)
    salary = fields.Float(compute=_computed_salary)
    age = fields.Char(compute=_computed_age, readonly=True)
    email = fields.Char()
    title = fields.Char()
    image = fields.Binary()
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
    ], default='m')
    # desc = fields.Text(default='Default Description')
    join_data = fields.Date(required=True)
    date_of_birth = fields.Date(default=fields.Date.context_today)
    is_accepted = fields.Boolean()
    bio = fields.Html()
    state = fields.Selection([
        ('apply', 'Applied'),
        ('iq', 'Passed IQ'),
        ('tech', 'Passed Technical'),
        ('rejected', 'rejected'),
        ('accepted', 'Accepted'),
    ], default='apply')
    military_status = fields.Char()

    # Relations btw Employee & Department
    # ================Many2one
    departmen_id = fields.Many2one('advansys.department')
    departmen_desc = fields.Text(related='departmen_id.desc', store=True, readonly=True)

    # Relation btw Employee & project
    # ==================Many2many
    project_ids = fields.Many2many('advansys.project')
    employee_skill_level_id = fields.One2many('advansys.employee.skill.level', 'employee_id')

    # context is an object used in environment and we can access its var during code
    """"def change_state(self):
        new_state=self.env.context['state']
        self.state=new_state"""

    def change_state(self):
        new_state = self.env.context['state']
        self.write({'state':new_state})
