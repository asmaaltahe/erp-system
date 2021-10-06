import datetime
import re


from num2words import num2words

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class EducationAccounting(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"
    _rec_name = "student_id"
    _name = 'education.accounting'
    _description = 'information accounting'

    student_id = fields.Many2one('student.registrar', string='Name')
    college_id = fields.Many2one("college.college", ondelete="cascade",string="College")
    program_id = fields.Many2one("program.program", ondelete="cascade",string="Program")
    level_id = fields.Many2one('level.level', string='Level',ondelete='cascade')
    semester_id = fields.Many2one('semester.semester', string='Semester', ondelete='cascade')
    form_number = fields.Char(string='University ID')
    money_type = fields.Selection([('cash', 'Cash'),('bank', 'Bank'),], string='Method Of Payment')
    currency_type = fields.Selection([('usd', 'Dollar'), ('sd', 'Sudanese Bound')], string="Currency Type")
    student_ids = fields.Char(string="student_ids")
    the_fees = fields.Float(string="Fees")
    receipt_code = fields.Char(string="Receipt Number", copy=False, readonly=True, index=True, default=lambda self: _('New'))
    the_amount = fields.Char(string="The Amount" , compute="_compute_amount" , store=True)
    about = fields.Char(string="About")
    year = fields.Char(string='Date ', default=lambda self: datetime.datetime.today().strftime('%Y-%m-%d'))
    presentation = fields.Boolean(string='yes ', default=False )
    register_office = fields.Boolean(string='register Office ', default=False )
    admission_ids = fields.Char(string="Accountant Name")
    state = fields.Selection([('draft', 'Draft'),('confirm', 'Confirm'), ('done', 'done')], string='Status', default="draft", readonly=True)
    register_office = fields.Boolean(string='register Office ', default=False )
    type_of_fees = fields.Boolean(string=" Type Of Fees",default=False)
    is_managemanent = fields.Boolean(string=" Type Of Fees")

    @api.model
    def create(self, vals):
        if vals.get('receipt_code', _('New')) == _('New'):
            vals['receipt_code'] = self.env['ir.sequence'].next_by_code('education_accounting.account_code.sequence') or _(
                'New')
            return super(EducationAccounting, self).create(vals)

    @api.depends('the_amount')
    def _compute_amount(self):
        self.the_amount = num2words(self.the_fees, lang='ar')

    def action_done(self):
        self.state = "done"

    def print_account_report(self):
        return self.env.ref('education_accounting.report_session').report_action(self)




