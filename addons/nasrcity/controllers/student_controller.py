from odoo import http
import json


class StudentController(http.Controller):
    @http.route('/students', type='http', auth='none', methods=['GET'])
    def get_students(self, **kw):
        student_model = http.request.env['iti.student']
        students = student_model.sudo().search([])
        json_students = [{'name': student.name} for student in students]
        return json.dumps(json_students)

    @http.route('/student',
                type='http',
                auth='none',
                methods=['POST'],
                csrf=False
                )
    def create_student(self, **kw):
        student_model = http.request.env['iti.student'].sudo()
        print kw
        student_model.create({
            'name': kw.get('name'),
            'age': kw.get('age'),
        })
        response = http.request.make_response({'success': True})
        return response

    @http.route('/student/<student_id>', auth='none', methods=['GET'])
    def view_students(self, student_id, **kw):
        student_id = int(student_id)
        student = http.request.env['iti.student'].sudo().browse(student_id)
        student_data = {
            'obj': student
        }
        return http.request.render('nasrcity.student_template', student_data)
