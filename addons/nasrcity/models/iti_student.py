from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ItiStudent(models.Model):
    _name = 'iti.student'

    @api.depends('gender')
    def _compute_salary(self):
        for record in self:
            if record.gender == 'm':
                record.salary = 5000
            else:
                record.salary = 2000

    @api.onchange('track_id')
    def onchange_track_id(self):
        self.name = 'Hamada'
        self.age = 22

    @api.onchange('gender')
    def onchange_gender(self):
        domain = [('desc', '!=', False)]
        if self.gender == 'f':
            domain = []
        return {
            'domain': {'track_id': domain}
        }

    @api.model
    def create(self, values):
        new_student = super(ItiStudent, self).create(values)
        track_values = {
            'track_name': new_student.name
        }
        new_track = self.env['iti.track'].create(track_values)
        return new_student

    def write(self, vals):
        return super(ItiStudent, self).write(vals)

    @api.constrains('age')
    def check_age(self):
        if self.age > 80:
            raise ValidationError('Hello')
        return True

    name = fields.Char(required=True)
    age = fields.Integer(required=True)
    email = fields.Char()
    image = fields.Binary()
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
    ])
    desc = fields.Text(default='Default Description')
    join_data = fields.Datetime()
    date_of_birth = fields.Date(default=fields.Date.context_today)
    is_accepted = fields.Boolean()
    bio = fields.Html()
    salary = fields.Float(compute=_compute_salary, store=True)
    track_id = fields.Many2one('iti.track', string='Student Track')
    track_desc = fields.Text(related='track_id.desc', store=True, readonly=True)
    skill_ids = fields.Many2many('iti.skill')
    course_line_ids = fields.One2many('iti.course.line', 'student_id')
    state = fields.Selection([
        ('apply', 'Applied'),
        ('iq', 'Passed IQ'),
        ('tech', 'Passed Technical'),
        ('refused', 'Refused'),
        ('accepted', 'Accepted'),
    ], default='apply')

    def change_state(self):
        new_state = self.env.context['state']
        self.write({'state': new_state})

    def tech_pass(self):
        self.state = 'tech'


