import datetime
from odoo import models, fields, api, _, exceptions
from odoo.exceptions import UserError
import re
class RegistrarOffices(models.Model):
    _inherit = ['mail.thread']
    _name = 'student.registrar'
    _description = 'student registrar office'

    name = fields.Char(string="Full Name")
    image_1920 = fields.Binary('image_1920')
    college_id = fields.Many2one("college.college", ondelete="cascade", string="College")
    program_id = fields.Many2one("program.program", ondelete="cascade", string="Program")
    batch_id = fields.Many2one("batch.batch", ondelete="cascade", string="Batch")
    level_id = fields.Many2one("level.level", ondelete="cascade", string="Level")
    semester_id = fields.Many2one("semester.semester", ondelete="cascade", string="Semester")
    year_stady = fields.Char('Study Year  :',  default=lambda self: str(datetime.datetime.now().year -1)+" - "+str(datetime.datetime.now().year))
    type_acceptance = fields.Many2one("type.admission",ondelete="cascade", straing='Type Of Acceptance')
    nationality_id = fields.Many2one('res.country', string="Nationality")
    type_of_id = fields.Selection([('national_number', 'National  Number'), ('national_card', 'National Card'), ('passport', 'Passport')], string="Personality Type")
    id_number = fields.Char(string="The National Number")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    religion = fields.Selection([('muslim', 'Muslim'), ('christian', 'Christian '), ('other', 'Other')], string="Religion")
    social_status = fields.Selection([('married', 'Married'), ('single', 'Single '), ('other', 'Other')], string="Social Status")
    brath_day = fields.Date(string="Barth Day")
    states = fields.Char(string="State")
    local = fields.Char(straing='Local')
    student_mobile = fields.Char(string="Mobile Number")
    whatsapp_phone = fields.Char(string="Whatsapp")
    email = fields.Char(string="Email")
    school_name = fields.Char(string='School Name ')
    sitting_number = fields.Char(string="Sitting Number")
    ratio = fields.Float(string="The Ratio")
    type_of_certificate = fields.Selection(
        [('sudanese', 'Sudanese'), ('arabic', 'Arabic'), ('other', 'Other')],
        string="Type Of Certificate")

    course = fields.Selection([('scientific', 'Scientific'), ('literary', 'Literary')], string="The course")
    previous_result = fields.Selection(
        [('scientific', 'طالب جديد'), ('literary', 'نجاح'), ('literary', 'اعادة'), ('literary', 'فصل  اكاديمي')
         ], string="Previous Result")
    form_number = fields.Char(string='Student Number')
    accept_year = fields.Char(string='Year Of Admission ')
    national_card = fields.Binary(string="National Card")
    school_certificate = fields.Binary(string="High School Certificate")
    applicant = fields.Char(string="applicant  Name")
    fother_address = fields.Char(string="Address")
    telephone = fields.Char(string="Telphone")
    job = fields.Char(string="Job")
    relative_relation = fields.Char(string="Relative Relation")
    data = fields.Char(string='Date ',  default=lambda self:datetime.datetime.today().strftime('%Y-%m-%d'))
    state = fields.Selection([('draft', 'Draft'), ('done', 'done')], string='Status', default="done")
    study_fees = fields.Float(string="Study  Fees" ,compute='_compute_fees', store=True)
    register_fees = fields.Float(string="Register  Fees" ,compute='_compute_fees', store=True)
    discount_fees = fields.Char(string="Discount")
    total_received = fields.Float(string="Total Received Fees")
    user_id = fields.Many2one('res.users', 'Creant User ',  default=lambda self: self.env.user)
    is_clinic = fields.Boolean(string="Is Clinic Book")
    is_first_installment = fields.Boolean(default=True)
    doctor_comment = fields.Text(string='Doctor Comment')
    result = fields.Char(string='Result ')
    result_data = fields.Date(string='Result Date ')
    doctor_name = fields.Many2one('res.users', 'Doctor Name ',  default=lambda self: self.env.user)

    @api.depends('type_acceptance')
    def _compute_fees(self):
        fees = self.env['study.fees'].search([('college_id', '=', self.college_id.id ), ('program_id', '=', self.program_id.id),('year', '=', datetime.datetime.now().year )])
        if fees:
            if self.type_acceptance.nationality:
                if self.type_acceptance.nationality == 'sudanese':
                    self.study_fees =fees.sudaness_study
                    self.total_received =fees.sudaness_study
                    self.register_fees =fees.sdn_register_fees
                else:
                    self.study_fees = fees.foreigners_study
                    self.total_received = fees.foreigners_study
                    self.register_fees = fees.foriegn_register_fees


    





    def create_student_user(self):
        pass







