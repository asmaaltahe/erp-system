import datetime
from odoo import models, fields, api, exceptions



class ClinicReportWizard(models.TransientModel):
    _name = 'clinic.wizard'
    _description = "Create Medical Report"

    patient_id = fields.Char(string='Student Number', readonly=True)

    name = fields.Char(string='full name')

    student_ids = fields.Many2one(
        'education.physical', string='Student Name')

    gender = fields.Char(string="Gender")

    dob = fields.Date(string='Date Of Birth')
    age = fields.Char(string='Age')
    date = fields.Date(string='Date Requested')
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")

    nationality = fields.Char(string='nationality')

    religion = fields.Char(string='religion')
    program = fields.Char(string='program')
    result = fields.Selection([
        ('لائق طبيا', 'لائق طبيا'),
        ('غير لائق طبيا', 'غير لائق طبيا'),
        ('أسباب أخرى', 'أسباب أخرى'),
    ], string="Result")

    result_date = fields.Char(string="Result Date", default=lambda self: datetime.datetime.today().strftime('%Y-%m-%d'))



    diagonis = fields.Text(string="Medical Report")
    doctor_name = fields.Char(string="Doctor Name", readonly=True, default=lambda self: self.env.user.name)

    #Function Wizards

    @api.onchange('student_ids')
    def create_wizard(self):
        filtered_b_ids = self.env['education.physical'].search([('id', '=', int(self.student_ids.id))])
        if filtered_b_ids:
            self.dob = filtered_b_ids.dob
            self.nationality = filtered_b_ids.nationality
            self.patient_id = filtered_b_ids.patient_id
            self.religion = filtered_b_ids.religion
            self.program = filtered_b_ids.program
            self.gender = filtered_b_ids.gender



    # Func send to registeration

    def create_medical_report(self):
        if (self.result and self.diagonis):
            pass
        else:
            raise exceptions.UserError(_('All Data must be completed'))

        result = self.env['student.registrar'].search([('form_number', '=', self.patient_id)])
        if result:
            for rec in result:
                rec.update(
                    {
                        'result': self.result,
                        'doctor_comment': self.diagonis,
                        'result_data': self.result_date,
                        'doctor_name': self.doctor_name,

                    }
                )
        else:

            self.env['student.registrar'].create({
                'result_data': self.result_date,
                'result': self.result,
                'doctor_comment': self.diagonis,
                'doctor_name': self.doctor_name,
            })


    # Pending
    # def lanch_physical_wizard(self):
    #     self.env['napata.physical'].create({
    #
    #         'name': self.student_ids.name,
    #         'gender': self.gender,
    #         'dob': self.dob,
    #         'program': self.program,
    #         'nationality': self.nationality,
    #         'religion': self.religion,
    #
    #              })





