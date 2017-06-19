from odoo import models, fields


class ItiTrack(models.Model):
    _name = 'iti.track'
    _rec_name = 'track_name'

    track_name = fields.Char()
    desc = fields.Text()
    student_ids = fields.One2many(
        'iti.student',
        'track_id'
    )

    def open_students_action(self):
        ids = []
        for student in self.student_ids[0].track_id.name:
            if len(student.name) > 5:
                ids.append(student.id)

        return {
            'name': 'Students Action',
            'type': 'ir.actions.act_window',
            'res_model': 'iti.student',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', ids)]
        }
