# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo import tools, _
from odoo.modules.module import get_module_resource



class AdvansysDepartment(models.Model):
    _name = 'advansys.department'

    _rec_name = 'department_name'
    department_name = fields.Char(required=True)
    desc = fields.Text()
    # Default Methods

    # Relation according to employee
    employee_ids = fields.One2many('advansys.employee', 'departmen_id')

    @api.multi
    def _computed_numbers(self):
        for rec in self:
            rec.no_employee = len(rec.employee_ids)
        print rec.no_employee

    no_employee= fields.Char(compute=_computed_numbers, readonly=True)

    # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary("Photo", attachment=True,
                                  help="This field holds the image used as photo for the test, limited to 1024x1024px.")
    image_medium = fields.Binary("Medium-sized photo", attachment=True,
                                         help="Medium-sized photo of the test. It is automatically " \
                                              "resized as a 128x128px image, with aspect ratio preserved. " \
                                              "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized photo", attachment=True,
                                        help="Small-sized photo of the test. It is automatically " \
                                             "resized as a 64x64px image, with aspect ratio preserved. " \
                                             "Use this field anywhere a small image is required.")

    def _get_default_image(self, cr, uid, context=None):
        image_path = get_module_resource('mymodule', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    defaults = {
        'active': 1,
        'image': _get_default_image,
        'color': 0,
    }

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(AdvansysDepartment, self).create(vals)
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
