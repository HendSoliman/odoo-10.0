from odoo import models, fields


class ItiCourseLine(models.Model):
    _name = 'iti.course.line'

    student_id = fields.Many2one('iti.student')
    course_id = fields.Many2one('iti.course')
    grade = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('e', 'E'),
    ])
