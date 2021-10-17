# -*- coding: utf-8 -*-

from odoo import api, models, fields
import datetime

# Added For report
class MedicalReport(models.AbstractModel):
    _name = 'physical.report'
    _description = 'Medical Report'

    @api.model

    def _get_medical_report_values(self, docids):

        docs = self.env['education.physical'].browse(docids)

        return {
                'doc_ids': docs.ids,
                'doc_model': 'education.physical',
                'docs': docs,

            }

# Added For laboratory
class MedicalReport(models.AbstractModel):
    _name = 'laboratory.report'
    _description = 'Medical Report'

    @api.model

    def _get_medical_report_values(self, docids):

        docs = self.env['education.laboratory'].browse(docids)

        return {
                'doc_ids': docs.ids,
                'doc_model': 'education.laboratory',
                'docs': docs,

            }

# Added For Mouth
class MedicalReport(models.AbstractModel):
    _name = 'eye.report'
    _description = 'Medical Report'
    @api.model
    def _get_medical_report_values(self, docids):
        docs = self.env['education.eye'].browse(docids)

        return {
                'doc_ids': docs.ids,
                'doc_model': 'education.eye',
                'docs': docs,

            }









