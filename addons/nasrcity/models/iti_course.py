from odoo import models, fields


class ItiCourse(models.Model):
    _name = 'iti.course'
    name = fields.Char()
