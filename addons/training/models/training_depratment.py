from odoo import models, fields


class TrainingDepartment(models.Model):
    # Name of the table
    _name = 'training.department'

    name = fields.Char()

    employee_ids=fields.One2many('training.employee','department_id')