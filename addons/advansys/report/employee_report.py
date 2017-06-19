# -*- coding: utf-8 -*-
from datetime import datetime, date
import dateutil
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class AdvansysEmployee(models.AbstractModel):
    _name = 'report.advansys.employee_report'

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        # report = report_obj._get_report_from_name('module.report_name')
        employess = self.env['advansys.employee'].browse(docids)
        docargs = {
            'new_var': employess.name,
            'docs': employess
        }
        return report_obj.render('advansys.employee_report', docargs)