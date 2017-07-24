# -*- coding: utf-8 -*-
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource
import re


class AdvansysEmployee(models.Model):
    # private attributes
    _name = 'advansys.employee'

    # Default Methods
    @api.model
    def _default_image(self):
        image_path = get_module_resource('advansys', 'static/src/img')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    @api.depends('gender')
    def _computed_salary(self):
        for record in self:
            if self.gender == 'm':
                self.salary = 5000
            else:
                self.salary = 8000




    # compute and search fields
    # To compute Age Automatically
    @api.depends('date_of_birth')
    def _computed_age(self):
        for rec in self:
            if rec.date_of_birth:
                dt = rec.date_of_birth
        d1 = datetime.strptime(dt, "%Y-%m-%d").date()
        d2 = date.today()
        rd = relativedelta(d2, d1)
        # if rd.years< 20:
        #     raise ValidationError("Your record is too old: %s" ,rd.years)
        # else:
        #     print '************',str(rd.years)
        rec.age = str(rd.years) + ' years\t' + str(rd.months) + 'months'



    @api.depends('join_data')
    def _computed_years(self):
        for rec in self:
            dt = rec.join_data
            d1 = datetime.strptime(dt, "%Y-%m-%d").date()
            d2 = date.today()
            rd = relativedelta(d2, d1)
            rec.no_years_at_company = str(rd.years) + ' years\t' + str(rd.months) + 'months'



            # Fields declaration
    name = fields.Char(string="Employee Name", required=True)
    salary = fields.Float(compute=_computed_salary)
    age = fields.Char(compute=_computed_age, readonly=True)
    email = fields.Char()
    title = fields.Char()
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
    ], default='m')
    join_data = fields.Date(required=True)
    no_years_at_company = fields.Char(compute=_computed_years)
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
    phone = fields.Char()
    address = fields.Char()
    # Relations
    departmen_id = fields.Many2one('advansys.department')
    departmen_desc = fields.Text(related='departmen_id.desc', store=True, readonly=True)

    project_ids = fields.Many2many('advansys.project')
    employee_skill_level_ids = fields.One2many('advansys.employee.skill.level', 'employee_id')

    # Constraints and onchanges
    @api.onchange('gender')
    def onChange_gender(self):
        print 'On Onchage method'
        domain = [('desc', '!=', False)]
        if self.gender == 'm':
            domain = []  # no condition  show all
        return {
            'domain': {'departmen_id': domain}
        }

    @api.constrains('email')
    def _validate_Email(self):
        match = re.search(r"(^[a-zA-Z0-9_.+-]+@[advansys]+-esc+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", self.email)
        #match=re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",self.email)
        if match:
            return 'Valid email.'
        else:
            raise ValidationError("Email must fit this Template :  name@advansys-esc.com")

    # CRUD methods (and name_get, name_search, ...) overrides
    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(AdvansysEmployee, self).create(vals)

    # Action methods
    # Business methods
    # context is an object used in environment and we can access its var during code
    """"def change_state(self):
        new_state=self.env.context['state']
        self.state=new_state"""

    def change_state(self):
        new_state = self.env.context['state']
        self.write({'state': new_state})

    # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary("Photo", attachment=True,
                          help="This field holds the image used as photo for the employee, limited to 1024x1024px.")
    image_medium = fields.Binary("Medium-sized photo", attachment=True,
                                 help="Medium-sized photo of the employee. It is automatically "
                                      "resized as a 128x128px image, with aspect ratio preserved. "
                                      "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized photo", attachment=True,
                                help="Small-sized photo of the employee. It is automatically "
                                     "resized as a 64x64px image, with aspect ratio preserved. "
                                     "Use this field anywhere a small image is required.")
