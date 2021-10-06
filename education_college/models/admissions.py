from odoo import models, fields, api, _
import datetime
import re

from odoo.exceptions import UserError


class EducatinAdmissions(models.Model):
    _inherit = ['mail.thread']
    _order = "id desc"
    _name = 'new.admission'
    _description = 'add admission'

    name = fields.Char(string="Full name", compute="get_student_name")
    first = fields.Char(string="First Name")
    second = fields.Char(string="Second Name")
    third = fields.Char(string="Third Name")
    last = fields.Char(string="Last Name")
    college_id = fields.Many2one('college.college', string='College', ondelete='cascade',
                                 default=lambda self: self.env['college.college'].search([]))
    program_id = fields.Many2one("program.program", ondelete="cascade", string="Program",
                                 domain="[('college_id', '=', college_id)]")
    batch_id = fields.Many2one('batch.batch', string='Batch', ondelete='cascade',
                               domain="[('program_id','=',program_id),('add_year','=',datetime.datetime.now().year)]")
    admission_type_id = fields.Many2one("type.admission", ondelete="cascade", string="Type Of Admission ")
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirmed'), ('waiting_approve', 'Waiting Approve'), ('done', 'done'),
         ('cancel', 'Cancel')], string='Status', default="draft", readonly=True)
    school_name = fields.Char(string="School Name ")
    studentNumber = fields.Char(string="Form Number", size=10)
    year_stady = fields.Char('Admission Year', default=lambda self: str(datetime.datetime.now().year - 1) + " - " + str(
        datetime.datetime.now().year))
    accept_year = fields.Char('Admission Year', default=lambda self: datetime.datetime.now().year)
    user_id = fields.Many2one('res.users', 'Creant User ', default=lambda self: self.env.user)


    @api.constrains('studentNumber')
    def check_studentNumber(self):
        for record in self:
            obj = self.search([('studentNumber', '=', record.studentNumber), ('id', '!=', record.id)])
            if obj:
                raise UserError('the number of student must be unique!')



    @api.onchange('first', 'second', 'third', 'last')
    def get_student_name(self):
        for re in self:
            re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)

    @api.constrains('first')
    def validate_student_full_name(self):
        if self.first:
            if not re.search(r'^(?:[^\W\d_]| )+$',
                             self.first + " " + self.second + " " + self.third + " " + self.last) != None:
                raise UserError(_('The value of student name must only letters'))

    @api.constrains('studentNumber')
    def validate_student_number(self):
        if self.studentNumber:
            if not re.match("^[0-9]*$", self.studentNumber) != None:
                raise UserError(_('The value of Form Number must be positive number'))


    def draft_action(self):
        self.state = 'confirm'

    def waiting_approve_action(self):
        self.state = 'waiting_approve'

    def done_action(self):
        val = {
            'name': self.name,
            'college_id': self.college_id.id,
            'program_id': self.program_id.id,
            'batch_id': self.batch_id.id,
            'type_acceptance': self.admission_type_id.id,
            'school_name': self.school_name,
            'form_number': self.studentNumber,
            'accept_year': self.accept_year,
            'year_stady': self.year_stady,
        }
        self.env['new.student'].create(val)

        self.state = 'done'

    def cancel_acrion(self):
        self.state = 'draft'

    def unlink(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError(
                    ('You cannot delete an admission which is not draft or cancelled. You should refund it instead.'))
        return super(EducatinAdmissions, self).unlink()


class EducatinDegreeHolder(models.Model):
    _inherit = ['new.admission']
    _order = "id desc"
    _name = 'degree.holder'
    _description = 'add degree holder'

    univercity_name = fields.Char(string="Univercity  Name ")
    nationality = fields.Selection([('sudanese', 'Sudanese'), ('foreigner', 'Foreigners')], string="Nationality",
                                   required=True)
    old_accept_type = fields.Selection([
        ('degree_holder', 'حملة الدرجات العلمية'),
        ('transfer', 'التحويل من جامعة الي اخري'),
        ('bridging', 'التجسير'),
        ('mature', 'ناضجين'),
    ], string="Admission After First Year")
    batch_id = fields.Many2one('batch.batch', string='Batch', ondelete='cascade',
                               domain="[('program_id', '=', program_id)]")

    def done_action(self):
        val = {
            'name': self.name,
            'college_id': self.college_id.id,
            'program_id': self.program_id.id,
            'batch_id': self.batch_id.id,
            'old_accept_type': self.old_accept_type,
            'school_name': self.school_name,
            'form_number': self.studentNumber,
            'accept_year': self.accept_year,
            'year_stady': self.year_stady,
        }
        self.env['old.student'].create(val)
        self.state = 'done'
