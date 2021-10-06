# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class MethodInvoice(models.TransientModel):
    _name = "payment.method"
    _rec_name = "money_type"
    _description = "Membership Invoice"
    student_id = fields.Many2one(
        'education.accounting', string='Student Name')
    money_type = fields.Selection([
        ('cash', 'Cash'),
        ('bank', 'Bank check'),
    ], string='Method Of Payment')

    # action for print account wizard report
    def create_accounting_wizard_report(self):
        result = self.env['education.accounting'].browse(self.student_id.ids)
        result.update(
             {
                 'money_type': self.money_type,
                  'state': 'confirm',
                  'admission_ids': self.env.user.name

             }
        )
