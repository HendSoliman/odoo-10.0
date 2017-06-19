from odoo import models


class StudentReport(models.AbstractModel):
    _name = 'report.nasrcity.student_report'

    def render_html(self, docids, **kwargs):
        report_obj = self.env['report']

        students = self.env['iti.student'].browse(docids)


        new_args = {
            'new_var': students.name,
            'docs': students
        }
        return report_obj.render(
            'nasrcity.student_report',
            new_args)
