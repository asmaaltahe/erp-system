from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError, UserError
import re
from datetime import datetime

class EducationCollege(models.Model):
    _inherit = ['mail.thread']
    _name = 'college.college'
    _description = 'add college  '

    name = fields.Char(string="College Name", help="enter Name of Collage")

    @api.constrains('name')
    def validate_student_full_name(self):
        if self.name:
            if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                raise UserError(_('The value of college name must only letters'))

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The name of college must be unique"),
    ]

    class EducationProgram(models.Model):
        _inherit = ['mail.thread']
        _name = 'program.program'
        _description = ' program name '

        name = fields.Char(string="Program", help="enter name of program")
        college_id = fields.Many2one('college.college',
                                     ondelete='cascade', string="College Name",
                                     default=lambda self: self.env['college.college'].search([]))
        code = fields.Char(string="Code", size=12)

        @api.constrains('name')
        def validate_student_full_name(self):
            if self.name:
                if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                    raise UserError(_('The value of college name must only letters'))

        @api.constrains('code')
        def validate_college_code(self):
            if self.code:
                if self.code == None:
                    raise UserError(_('The value of college code must be positive number'))

        _sql_constraints = [
            ('name_unique',
             'UNIQUE(name)',
             "The name of program must be unique"),
            ('code_unique',
             'UNIQUE(code)',
             "The code  must be unique"),
        ]

    class EducationSpecialization(models.Model):
        _inherit = ['mail.thread']
        _name = 'specialization.specialization'
        _description = ' add specialization  '

        name = fields.Char(string="Specialization", help="enter Name of Specialization")
        college_id = fields.Many2one('college.college',ondelete='cascade', string="College",
                                     default=lambda self: self.env['college.college'].search([]))
        program_id = fields.Many2one('program.program',
                                     ondelete='cascade', string="Program")

        @api.onchange('college_id')
        def get_program(self):
            college = self.env['program.program'].search([('college_id', '=', self.college_id.id)]).mapped("id")
            if college:
                return {'domain': {'program_id': [('id', 'in', college)]}}

            @api.constrains('name')
            def validate_student_full_name(self):
                if self.name:
                    if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                        raise UserError(_('specialization  name must only letters'))

            _sql_constraints = [
                ('name_unique',
                 'UNIQUE(name)',
                 "Specialization name  must be unique"),
            ]


    class EducationTypeOfAdmissio(models.Model):
        _inherit = ['mail.thread']
        _name = 'type.admission'
        _description = 'type of admission '

        name = fields.Char(string="Type Of Admission", required=True)
        nationality = fields.Selection([('sudanese','Sudanese'),('foreigner','Foreigners')],string="Nationality", required=True)
        @api.constrains('name')
        def validate_type_of_admission(self):
            if self.name:
                if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                    raise UserError(_('type of admission  must only letters'))

        _sql_constraints = [
            ('name_unique',
             'UNIQUE(name)',
             "type of admission must be unique"),
        ]

    class EducationLevel(models.Model):
        _inherit = ['mail.thread']
        _name = 'level.level'
        _description = 'university name '

        name = fields.Char(string="Academic  Level")

        @api.constrains('name')
        def validate_type_of_admission(self):
            if self.name:
                if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                    raise UserError(_('academic  level  must only letters'))

        _sql_constraints = [
            ('name_unique',
             'UNIQUE(name)',
             "academic  levelmust be unique"),
        ]

    class EducationSemester(models.Model):
        _inherit = ['mail.thread']
        _name = 'semester.semester'
        _description = ' add semester '

        name = fields.Char(string="Semester")
        level_id = fields.Many2one('level.level', string='Academic level')

        @api.constrains('name')
        def validate_type_of_admission(self):
            if self.name:
                if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                    raise UserError(_('semester  must only letters'))

        _sql_constraints = [
            ('name_unique',
             'UNIQUE(name)',
             "semester must be unique"),
        ]

    class EducationBatch(models.Model):
        _inherit = ['mail.thread']
        _name = 'batch.batch'
        _order = "id desc"
        _description = 'add  batch  '

        college_id = fields.Many2one('college.college',ondelete='cascade', string="Collage Name",
                                     default=lambda self: self.env['college.college'].search([]))
        program_id = fields.Many2one('program.program', ondelete='cascade', string='Program')
        name = fields.Char(string="Batch Name")
        year = fields.Char(string='Study Year',default=str(datetime.today().year) + " - " + str(datetime.today().year + 1))
        add_year = fields.Char(default=datetime.today().year)

        @api.onchange('college_id')
        def get_program(self):
            college = self.env['program.program'].search([('college_id', '=', self.college_id.id)]).mapped("id")
            if college:
                return {'domain': {'program_id': [('id', 'in', college)]}}

        class OtherRevenue(models.Model):
            _inherit = ['mail.thread']
            _name = 'other.revenue'
            _description = ' add revenue type '

            name = fields.Char(string="Revenue Name")

            @api.constrains('name')
            def validate_type_of_admission(self):
                if self.name:
                    if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                        raise UserError(_('revenue name  must only letters'))

            _sql_constraints = [
                ('name_unique',
                 'UNIQUE(name)',
                 "Other revenue name  must be unique"),
            ]
