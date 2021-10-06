import datetime
from num2words import num2words
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CreatePayment(models.TransientModel):
    _name = 'create.payment'
    _description = "Create Make a payment"

    student_id = fields.Many2one('student.registrar', string='Student Name', )
    program_id = fields.Many2one("program.program", ondelete="cascade", string="Brogram")
    college_id = fields.Many2one('college.college', string='College', ondelete='cascade')
    level_id = fields.Many2one('level.level', string='Level', ondelete='cascade' )
    semester_id = fields.Many2one('semester.semester', string='Semester', ondelete='cascade')
    batch_id = fields.Many2one("batch.batch", ondelete="cascade", string="Batch")
    certificate_type = fields.Selection([('sudanese', 'Sudanese'), ('foreigner', 'Foreigners')], string="Certificate")
    currency_type = fields.Selection([('usd', 'Dollar'), ('sd', 'Sudanese Bound')], string="Currency Type")
    revenue_id = fields.Many2one("revenue.revenue", ondelete="cascade", string="Other Revenue")
    register_fees = fields.Float(string="Register  Fees")
    installment = fields.Selection([('one', '100%'), ('two', '50%'), ], string="Installment")
    total_received = fields.Float(string="Total Received Fees")
    paying = fields.Float(string="paying off")
    other_fees = fields.Float(string="Other Revenue ")
    about = fields.Char(string="about")


    @api.onchange('student_id')
    def create_appointment(self):
        student_id = self.env['student.registrar'].search([('id', '=', self.student_id.id)])
        if student_id:
            self.program_id = student_id.program_id.id
            self.college_id = student_id.college_id.id
            self.level_id = student_id.level_id.id
            self.semester_id = student_id.semester_id.id
            self.batch_id = student_id.batch_id.id
            self.certificate_type = student_id.type_acceptance.nationality
            self.register_fees = student_id.register_fees
            self.total_received = student_id.total_received

    @api.onchange('installment')
    def create_installment(self):
        self.other_fees = 0.0
        self.about = " "
        if self.installment:
            if self.installment == 'one':
                if self.student_id.is_first_installment == True:
                    self.paying = self.total_received + self.register_fees
                    self.about = "رسوم تسجيل + رسوم دراسية "
                else:
                    self.paying = self.total_received
                    self.about = "رسوم دراسية "
            elif self.installment == 'two':
                if self.student_id.is_first_installment == True:
                    self.paying = self.register_fees +(self.total_received / 2)
                    self.about = "رسوم تسجيل + رسوم دراسية "
                else:
                    self.paying = self.total_received / 2
                    self.about = "رسوم دراسية "


    @api.onchange('revenue_id')
    def create_other_revenue(self):
        revenue = self.env['revenue.revenue'].search([('id', '=', self.revenue_id.id)])
        self.paying = 0.0
        self.about = " "
        if self.revenue_id:
            if self.certificate_type:
                if self.certificate_type == 'sudanese':
                    self.other_fees = revenue.for_sudanes
                    self.about = revenue.revenue_type_id.name
                    self.currency_type = 'sd'
                if self.certificate_type == 'foreigner':
                    self.other_fees = revenue.for_foreig
                    self.about = revenue.revenue_type_id.name
                    self.currency_type = 'usd'

    def create_payment(self):
        the_fees = 0.0
        if self.paying > 1:
            the_fees =self.paying
        elif self.other_fees > 1:
            the_fees =self.other_fees
        if self.certificate_type == 'sudanese':
            currency_type = 'sd'
        else:
            currency_type = 'usd'
        self.env['education.accounting'].create({
            'student_id': self.student_id.id,
            'program_id': self.program_id.id,
            'level_id': self.level_id.id,
            'semester_id': self.semester_id.id,
            'the_fees': the_fees,
            'currency_type': currency_type,
            'about': self.about,

        })

    # form_number = fields.Char(straing='University ID')
    # register_fees = fields.Float(straing='Register Fees')
    # the_amount  = fields.Float(straing='the amount')
    # inser_amount  = fields.Float(straing='Specified amount')
    # program_fees = fields.Float(string="Study Fees")
    # certificate_type = fields.Char(string="Certificate type Fees")
    # other_fees = fields.Float(string="Other Fees")
    # firest_installment_fees = fields.Selection([
    #     ('1', '100%'),
    #     ('2', '50%'), ],string="First installment")
    #
    # discount_fees= fields.Float(string=" The Discount")
    # fina_flees=fields.Float(string="Final Fees")
    # total_received = fields.Float(string="Total Received Fees")
    # is_pay_sd = fields.Boolean(string="Pay in Sudanese", required=True)
    # is_first_installment= fields.Boolean()
    # student_managemanent_fees = fields.Float(string="managemanent Fees")
    # the_register_amount = fields.Char(string="the  student Amount ")
    # the_abut = fields.Char(string="the  Managemanent Amount ")
    # is_managemanent = fields.Boolean( default=False )
    #
    # @api.onchange('managemanent_fees')
    # def get_student_management_fees(self):
    #     curr_year = datetime.datetime.now().year
    #     managemanentfees = self.env['napata.managemanentfees'].search([('year', '=', curr_year)])
    #     if managemanentfees:
    #         self.the_register_amount=" "
    #         self.total_received=0.0
    #         for rec in managemanentfees:
    #             if rec == self.managemanent_fees:
    #                 if self.certificate_type !='قبول الوافدين':
    #                     self.student_managemanent_fees = self.managemanent_fees.sudanes_managemanentfees
    #                     self.the_abut = " فقط " + str(
    #                             "\t " + num2words(self.student_managemanent_fees, lang='ar')) + " \t    جنية سوداني لا  غير"
    #                     print(self.student_managemanent_fees)
    #                 elif self.certificate_type == 'قبول الوافدين':
    #
    #                        if self.is_pay_sd:
    #                            self.student_managemanent_fees = self.managemanent_fees.sudanes_managemanentfees
    #                            self.the_abut = " فقط " + str(
    #                                "\t " + num2words(self.student_managemanent_fees,
    #                                                  lang='ar')) + " \t    جنية سوداني لا  غير"
    #                        else:
    #                            self.student_managemanent_fees = self.managemanent_fees.foreig_managemanentfees
    #                            self.the_abut = " فقط " + str(
    #                                "\t " + num2words(self.student_managemanent_fees, lang='ar')) + " \t     دولار  امريكي لا  غير"
    #
    #             # else:
    #             #         self.student_managemanent_fees = 0.0
    #
    #
    #
    # @api.onchange('student_ids')
    # def create_appointment(self):
    #     filtered_register_ids = self.env['napata.register'].search([('id', '=', int(self.student_ids.id))])
    #     if filtered_register_ids:
    #         self.main_desires = filtered_register_ids.program.id
    #         self.certificate_type=filtered_register_ids.accept_type.name
    #         self.register_fees=filtered_register_ids.register_fees
    #         self.discount_fees=filtered_register_ids.discount_fees
    #         self.college=filtered_register_ids.college_id
    #         self.level = filtered_register_ids.level
    #         self.semester = filtered_register_ids.semester
    #         self.form_number = filtered_register_ids.form_number
    #         self.program_fees=filtered_register_ids.Remaining_amount
    #         self.is_first_installment=filtered_register_ids.is_first_installment
    #
    #
    #
    #
    #
    #
    # @api.onchange('firest_installment_fees')
    # def _get_total_fees(self):
    #
    #     if self.firest_installment_fees:
    #         self.the_abut = " "
    #         self.student_managemanent_fees = 0.0
    #         if self.certificate_type == 'منحة دراسية':
    #             self.total_received = self.program_fees
    #             self.the_register_amount = " فقط " + str(
    #                 "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"
    #
    #         elif self.certificate_type == 'قبول الوافدين':
    #             if self.firest_installment_fees == '1':
    #                 if self.is_first_installment:
    #                     self.total_received = self.program_fees + self.register_fees
    #                     self.the_register_amount = " فقط " + str(
    #                             "\t " + num2words(self.total_received, lang='ar')) + " \t     دولار  امريكي لا  غير"
    #                 else:
    #                     self.total_received = self.program_fees
    #                     self.the_register_amount = " فقط " + str(
    #                         "\t " + num2words(self.total_received, lang='ar')) + " \t     دولار  امريكي لا  غير"
    #             elif self.firest_installment_fees == '2':
    #                 if self.is_first_installment:
    #                     self.total_received = (self.program_fees / 2) + self.register_fees
    #                     self.the_register_amount = " فقط " + str(
    #                         "\t " + num2words(self.total_received, lang='ar')) + " \t     دولار  امريكي لا  غير"
    #                 else:
    #                     self.total_received = (self.program_fees / 2)
    #                     self.the_register_amount = " فقط " + str(
    #                         "\t " + num2words(self.total_received, lang='ar')) + " \t     دولار  امريكي لا  غير"
    #
    #         else:
    #                 if self.firest_installment_fees == '1':
    #                     if self.is_first_installment:
    #
    #                         self.total_received = self.program_fees + self.register_fees
    #                         self.the_register_amount = " فقط " + str(
    #                             "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"
    #
    #
    #                     else:
    #                         self.total_received = self.program_fees
    #                         self.the_register_amount = " فقط " + str(
    #                             "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"
    #
    #                 elif self.firest_installment_fees == '2':
    #                     if self.is_first_installment:
    #                         self.total_received = (self.program_fees / 2) + self.register_fees
    #                         self.the_register_amount = " فقط " + str(
    #                             "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"
    #                     else:
    #                         self.total_received = (self.program_fees / 2)
    #                         self.the_register_amount = " فقط " + str(
    #                             "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"
    #     else:
    #         self.total_received=0.0
    #         self.the_register_amount= ""
    #
    # def create_payment(self):
    #     program=self.main_desires.id
    #     the_amount=self.the_register_amount
    #     the_fees=0.0
    #     if  self.total_received >  1:
    #         the_fees= self.total_received
    #         the_about="رسوم دراسية"
    #         result = self.env['napata.register'].browse(self.student_ids.ids)
    #         result.update(
    #             {'state': 'confirm'}
    #         )
    #
    #
    #
    #     elif self.student_managemanent_fees > 1:
    #      the_about=self.managemanent_fees.name.name
    #      the_fees=self.student_managemanent_fees
    #      the_amount=self.the_abut
    #      self.is_managemanent = True
    #
    #     if the_fees == 0.0 :
    #         raise UserError(_('The value of student name must only letters'))
    #
    #     else:
    #         self.env['napata.accounting'].create({
    #                 'name': self.student_ids.name,
    #                 'first': self.student_ids.first_name,
    #                 'second': self.student_ids.second_name,
    #                 'third': self.student_ids.third_name,
    #                 'last': self.student_ids.forth_name,
    #                 'college': self.college.id,
    #                 'level': self.level.id,
    #                 'semester': self.semester.id,
    #                 'form_number': self.form_number,
    #                 'program': program,
    #                 'presentation': True,
    #                 'register_office': True,
    #                 'type_of_fees': self.is_managemanent,
    #                 'the_fees': the_fees,
    #                 'the_amount': the_amount,
    #                  'about': the_about,
    #             })
