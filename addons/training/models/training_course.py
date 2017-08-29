from odoo import models, fields


class TrainingCourse(models.Model):
    # Name of the table
    _name = 'training.course'
    _rec_name = 'course_title'

    course_title = fields.Char()
    course_version = fields.Integer()
