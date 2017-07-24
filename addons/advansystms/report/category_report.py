from odoo import api, models

class ParticularReport(models.AbstractModel):
    _name = 'report.advansystms.report_category'

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        # report = report_obj._get_report_from_name('module.report_name')
        categories = self.env['advansystms.cat'].browse(docids)
        docargs = {
            'new_var': categories.name,
            'docs': categories
        }
        return report_obj.render\
            ('advansystms.report_category', docargs)
          #ValueError: External ID not found in the system: advansystm.report_category
    # will be rais if this name does not match report name