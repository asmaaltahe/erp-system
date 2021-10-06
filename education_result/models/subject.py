import datetime

from odoo import models, fields, api
import datetime

class subject(models.Model):
    _inherit = ['mail.thread']
    _name = 'student.subject'
    _description = 'subject information '

    name = fields.Char(string="Subject")
    college_id = fields.Many2one('college.college', string='College')
    program_id = fields.Many2one('program.program', string='Program', domain="[('college_id','=',college_id)]")
    level_id = fields.Many2one('level.level', string=' Level')
    semester_id = fields.Many2one('semester.semester', string='Semester', domain="[('level_id','=',level_id)]")
    code = fields.Char(string="Code")
    hours = fields.Integer(string="hours")
    date = fields.Date(string="Date", default=lambda self: fields.Date.today())
    user_id = fields.Many2one('res.users', 'Creant User ', default=lambda self: self.env.user)




