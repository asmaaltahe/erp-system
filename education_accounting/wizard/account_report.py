
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
class accountReport(models.TransientModel):
    _name = "account.report"
    _description = "account Report"
    pram =[('general','General'),('program','program'),('studant','Studant')
           ,('program_level','program&level'),
    ('program_level_semester','program&level&semester')]
    student_ids = fields.Many2one(
        'napata.accounting', string='Student Name')
    college = fields.Many2one('napata.collage', string='the level',
                            ondelete='cascade',
                            default=lambda self: self.env['napata.collage'].search([]))
    program=fields.Many2one("napata.program",ondelete="cascade",string="program")
    semester = fields.Many2one('napata.semester', string='Semester',
                               ondelete='cascade')

    level = fields.Many2one('napata.level', string='the level',
                            ondelete='cascade')
    date  = fields.Date(string="date")
    params=fields.Selection(pram,string="parameters",default='general')



    def print_accunt_report(self):
        data = {
            'ids':self.ids,
             'model':self._name,
             'form':{
                 'student_id': self.student_ids.id,
                 'student_name': self.student_ids.name,
                 'program_id':self.program.id,
                 'program_name':self.program.name,
                 'semester_id':self.semester.id,
                 'semeste_name':self.semester.name,
                 'level_id':self.level.id,
                 'level_name':self.level.name,
                 'params':self.params

             }

        }

        return self.env.ref('napata_accounting.account_wizerd_report').report_action(self, data=data)


class AccountReport(models.AbstractModel):
    _name = 'report.napata_accounting.accountwizerd_report_templet'

    def _get_report_values(self, docids, data=None):

        student_id = data ['form']['student_id']
        student_name = data ['form']['student_name']
        program_id = data['form']['program_id']
        program_name = data['form']['program_name']

        semester_id = data['form']['semester_id']
        semeste_name = data['form']['semeste_name']

        level_id = data['form']['level_id']
        level_name = data['form']['level_name']

        params = data['form']['params']
        domain = []

        if params == 'general':
            docs = self.env['napata.accounting'].search([])
        elif params =='program':
            domain.append(('program','=',program_id))

        elif params =='studant':
            domain.append(('student_ids','=',student_id))
        elif params =='program_level':
            domain.append(('level','=',level_id))
            domain.append(('program','=',program_id))

        else:
            domain.append(('program', '=', program_id))
            domain.append(('level', '=', level_id))
            domain.append(('semester', '=', semester_id))
        docs = self.env['napata.accounting'].search(domain)

        return {
                'doc_ids': data['ids'],
                'model': data['model'],
                'student_name': student_name,
                'program_name': program_name,
                'semeste_name': semeste_name,
                'level_name': level_name,
                'params': params,
                'docs': docs,
            }


        
        

