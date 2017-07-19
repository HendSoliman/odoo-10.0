# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo import tools, _
from odoo.modules.module import get_module_resource



class AdvansysTMSDepartment(models.Model):
    _name = 'advansystms.department'

    _rec_name = 'department_name'
    department_name = fields.Char(required=True)
    department_code=fields.Char()

    description = fields.Text()
    # Default Methods

    # Relation according to employeedepartment_id
    employee_ids = fields.One2many('advansystms.employee', 'department_id')

    @api.multi
    def _computed_numbers(self):
        for rec in self:
            rec.no_employee = len(rec.employee_ids)
        print rec.no_employee

    no_employee= fields.Char(compute=_computed_numbers, readonly=True)
