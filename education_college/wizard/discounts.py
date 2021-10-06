from odoo import models, fields, api, _

class CreateDiscounts(models.TransientModel):
    _name = 'student.discounts.wizard'
    _description = "Create User for selected Student(s)"

    student_ids = fields.Many2one(
        'student.registrar', string='Student Name')
    college_id = fields.Many2one("college.college", ondelete="cascade", string="College")
    program_id = fields.Many2one("program.program", ondelete="cascade", string="Program")
    batch_id = fields.Many2one("batch.batch", ondelete="cascade", string="Batch")
    level_id = fields.Many2one("level.level", ondelete="cascade", string="Level")
    semester_id = fields.Many2one("semester.semester", ondelete="cascade", string="Semester")
    discount_type = fields.Selection([
        ('0', 'Select Discount Type'),
        ('1', 'Percentage'),
        ('2', 'amount'), ], string="Discount Type" ,default='0')
    form_number = fields.Char(straing='University ID')
    register_fees = fields.Float(straing='Register Fees')
    program_fees  = fields.Float(straing='Study Fees')
    certificate_type = fields.Char(string="Certificate type Fees")
    after_discount= fields.Float(string=" The Fees After Discount",comput="_comput_discount", store=True)
    discount_prcentage = fields.Selection([
        ('10', '10%'),
        ('20', '20%'),
        ('30', '30%'),
        ('40', '40%'),
    ], string="Discount Prcentage")

    @api.onchange('student_ids')
    def _get_studen_information(self):
        self.college_id= self.student_ids.college_id.id
        self.program_id= self.student_ids.program_id.id
        self.batch_id= self.student_ids.batch_id.id
        self.level_id= self.student_ids.level_id.id
        self.semester_id= self.student_ids.semester_id.id
        self.certificate_type= self.student_ids.type_acceptance.nationality
        self.program_fees= self.student_ids.study_fees

    @api.onchange('discount_prcentage')
    def _comput_discount(self):

        self.after_discount = self.program_fees - (self.program_fees*(int(self.discount_prcentage)/100))

    def Create_student_discounts(self):
        record = self.env['student.registrar'].browse(self.student_ids.id)
        des = str(self.discount_prcentage) + str("%")

        record.update({
            'discount_fees': des,
            'total_received': self.after_discount,

        })



