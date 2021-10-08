from odoo import models, fields, api, exceptions, _
from odoo.exceptions import UserError, ValidationError
import datetime



class CalculationAverage(models.Model):
    _inherit = ['mail.thread']
    _name = 'calculation.average'
    _description = 'average calculation'
    college_id = fields.Many2one('college.college', string='College')
    program_id = fields.Many2one('program.program', string='program', domain="[('college_id','=',college_id)]")
    level_id = fields.Many2one('level.level', string=' level')
    semester_id = fields.Many2one('semester.semester', string='semester', domain="[('level_id','=',level_id)]")
    average_line = fields.One2many('line.average', 'average_id', string='Opportunities')
    state = fields.Selection([('draft', 'Drift'),('confirm', 'Confirm'),('waiting_approve', ' Waiting Approval'),('approve', 'Approval'), ('done', 'Done')], 'Status', default='draft')
    year = fields.Char('Study Year', default=lambda self: datetime.datetime.now().year)
    user_id = fields.Many2one('res.users', 'Creant User ', default=lambda self: self.env.user)

    def confirm_action(self):
        for record in self:
            record.state = 'confirm'

    def waiting_approve_action(self):
        for record in self:
            record.state = 'waiting_approve'

    def waiting_approve_action(self):
        for record in self:
            record.state = 'waiting_approve'

    def done_action(self):
        for record in self:
            record.state = 'done'

    def cancel_action(self):
        for record in self:
            record.state = 'draft'


    @api.onchange('semester_id')
    def get_subject_degree(self):
            self.average_line =[(5,0,0)]
            average = self.env['calculation.average'].search([('college_id', '=', self.college_id.id), ('program_id', '=', self.program_id.id),('level_id', '=', self.level_id.id), ('year', '=', self.year)], limit=1)
            subject_degree = self.env['subject.degree'].search([('program_id', '=', self.program_id.id),('level_id', '=', self.level_id.id),('semester_id', '=', self.semester_id.id)])
            subject_degree_line =subject_degree.mapped("degree_line")
            studant_id = subject_degree_line.mapped("student_id")
            mark = []
            hour= []
            total = []

            if average:
                    chack_date = self.env['calculation.average'].search(
                        [('college_id', '=', self.college_id.id), ('program_id', '=', self.program_id.id),
                         ('level_id', '=', self.level_id.id), ('semester_id', '=', self.semester_id.id),
                         ('year', '=', self.year)], limit=1)
                    if chack_date:
                        raise ValidationError(_('The result of this semester has already been entered.'))
                    else:
                                average_lin = average.mapped("average_line")
                                for rec in studant_id:
                                    semester_average = average_lin.filtered(lambda r: r.student_id  == rec)
                                    subject_degree=subject_degree_line.filtered(lambda r: r.student_id  == rec)
                                    for lin in subject_degree:
                                        total.append(lin.total)
                                        mark.append(lin.subject_id.hours * lin.total)
                                        hour.append(lin.subject_id.hours)
                                        cumulative_average =round((sum(mark) / sum(hour) / 25), 2)

                                    result= ((semester_average.semester_average * semester_average.hours) + (cumulative_average * sum(hour))) / (semester_average.hours + sum(hour))
                                    self.write({'average_line': [(0, 0, {
                                        'student_id': line.id,
                                        'semester_average': semester_average.semester_average,
                                        'cumulative_average': cumulative_average,
                                        'result': result,
                                        'decision': 'pass',

                                    }) for line in rec]})
                                    mark.clear()
                                    total.clear()
                                    hour.clear()
            else:
                for rec in studant_id:
                        subjects = subject_degree_line.filtered(lambda r: r.student_id  == rec)
                        for lin in subjects:
                           mark.append(lin.subject_id.hours *lin.total)
                           hour.append(lin.subject_id.hours)
                        self.write({'average_line': [(0, 0, {
                            'student_id': line.id,
                            'hours': sum(hour),
                            'semester_average': round((sum(mark)/sum(hour)/25),2),
                            'cumulative_average': 0,

                        }) for line in rec]})
                        mark.clear()
                        total.clear()
                        hour.clear()









class AverageLine(models.Model):
    _name = 'line.average'
    _description = 'average calculation Line'

    average_id = fields.Many2one('calculation.average', string='degree')
    student_id = fields.Many2one('student.registrar', string='Student Name')
    hours = fields.Float(string="number of hours")
    semester_average = fields.Float(string='S-GPA I',digits = (1,2))
    cumulative_average = fields.Float(string='S-GPA II' ,digits = (1,2))
    result = fields.Float(string='GPA' ,digits = (1,2))
    decision = fields.Selection([('pass', 'Pass'), ('second', 'Second Period')], string="Decision")









