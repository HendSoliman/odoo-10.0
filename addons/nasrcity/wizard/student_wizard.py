from odoo import fields, models


class StudentWizard(models.TransientModel):
    _name = 'student.wizard'

    from_date = fields.Date(default=fields.Date.context_today)
    to_date = fields.Integer(default=lambda self: self.from_date)


