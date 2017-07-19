# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource


class AdvansysTMSEmployee(models.Model):
    _name = "advansystms.employee"
    _description = "Employee"

    name = fields.Char(string="Employee First Name" , required=True)
    middle_name = fields.Char(string="Employee middle Name")
    last_name = fields.Char(string="Employee Last Name")
    employee_number = fields.Char(string="Employee Number")
    employee_hiring_date = fields.Date()
    employee_termination_date = fields.Date()
    position_title = fields.Char()
    job_description = fields.Text()
    email = fields.Char('Work Email')
    notes = fields.Text()
    phone = fields.Char()

    # Relations  to Department
    department_id = fields.Many2one('advansystms.department', string='Department' ,required=True)

    supervisor_id = fields.Many2one('advansystms.employee', string='Supervisor')

    employee_type_id=fields.Many2one('advansystms.employee.type',String='Employee Type')
    employee_type_title=fields.Char(related='employee_type_id.type_title', store=True, readonly=True)

    _sql_constraints = [
        ('number_uniq', 'unique (employee_number)', "Tag Number already exists !"),
    ]

    @api.model
    def _default_image(self):
        image_path = get_module_resource('advansystms', 'static/src/img')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

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
