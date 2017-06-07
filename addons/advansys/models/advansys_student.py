from datetime import datetime

import parser

from odoo import models, fields, api


class AdvansysStudent(models.Model):
    # Table name
    _name = 'advansys.student'

    @api.onchange('name')
    def do_stuff(self):
        print('********************************')


    name = fields.Char(required=True)

    gender = fields.Selection(
        [
            ('m', 'Male'),
            ('f', 'Female')

        ], defult='m'

    )


