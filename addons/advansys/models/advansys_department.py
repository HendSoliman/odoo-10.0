# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AdvansysDepartment(models.Model):
    _name = 'advansys.department'

    name = fields.Char(required=True)
    desc = fields.Text()

    # Relation according to employee
    employee_ids = fields.One2many('advansys.employee', 'departmen_id')

    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100

    # Get All Employees who are Idle state
    def show_accpeted_employees(self):
        idle_employees = self.env['advansys.employee'].search([('departmen_id', '=', self.id)])
        employess_Objects = []
        for emp in idle_employees:
            if len(emp.project_ids) ==False:
                employess_Objects.append(emp.id)
                print emp.name, len(emp.name)
        return {
            'name': ' Accpepted Employees',
            'type': 'ir.actions.act_window',
            'res_model': 'advansys.employee',
            'view_mode': 'tree, form',
            'domain': [('id', 'in', employess_Objects)]
        }
