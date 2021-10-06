from odoo import models, fields, api, exceptions
import datetime



class StudyFees(models.Model):
    _inherit = ['mail.thread']
    _name = 'study.fees'
    _rec_name = 'program_id'
    _description = 'add fees information'

    college_id = fields.Many2one('college.college', ondelete='cascade', string="Collage",
                                 default=lambda self: self.env['college.college'].search([]))
    program_id = fields.Many2one("program.program", ondelete="cascade", string="Program")
    sudaness_study = fields.Integer(string="Sudanes Study")
    foreigners_study = fields.Integer(string=" Foreig Study")
    sdn_register_fees = fields.Integer(string=" Sudanes Register")
    foriegn_register_fees = fields.Integer(string=" Foreig Register")
    study_year = fields.Char('Study Year', default=lambda self: str(datetime.datetime.now().year - 1) + " - " + str(
        datetime.datetime.now().year))
    year = fields.Char('Study Year', default=lambda self: datetime.datetime.now().year)
    user_id = fields.Many2one('res.users', 'Creant User ', default=lambda self: self.env.user)





class managementFees(models.Model):
        _inherit = ['mail.thread']
        _name = 'revenue.revenue'
        _description = 'add revenue fees'
        _rec_name = "revenue_type_id"

        revenue_type_id = fields.Many2one('other.revenue', string="Fees Type ",ondelete='cascade')
        for_sudanes = fields.Integer(string="Sudanes ", required=True)
        for_foreig = fields.Integer(string="Foreign ", required=True)
        year = fields.Char('Year', default=lambda self: datetime.datetime.now().year)
        study_year = fields.Char('Study Year', default=lambda self: str(datetime.datetime.now().year - 1) + " - " + str(
            datetime.datetime.now().year))
        user_id = fields.Many2one('res.users', 'Creant User ', default=lambda self: self.env.user)

