import datetime
from odoo import models, fields, api, exceptions,_


class Eyeclinic(models.Model):
    _name = 'education.eye'
    _description = 'Eye'
    _order = "id desc"
    patient_id = fields.Char(string='Student Number' )
    name = fields.Char(string="full name" )
    first = fields.Char(string="First Name" )
    second = fields.Char(string="Second Name" )
    third = fields.Char(string="Third Name" )
    last = fields.Char(string="Last Name" )
    gender=fields.Char(string="gender" )
    brath_day = fields.Date(string='Date Of Birth' )
    date = fields.Char(string='Date', default=lambda self: datetime.datetime.today().strftime('%Y-%m-%d'),  readonly=True)
    phone = fields.Char(string="Phone" )
    email = fields.Char(string="Email" )
    nationality = fields.Char(string='Nationality' )
    religion = fields.Char(string='Religion' )
    program = fields.Char(string='Program' )
    address = fields.Char(string="address")
    # The End Personal Information
    general = fields.Char(string="General Vision")
    withoutglss = fields.Char(string="With Out Glasses")
    withglasses = fields.Char(string='With  Glasses')
    color = fields.Char(string='Color Vision')
    near = fields.Char(string='Near Vision')
    opthahmologist = fields.Char(string='Opthahmologist', readonly=True, default=lambda self: self.env.user.name )
    assessment = fields.Text(string="Assessment")
    diagonis = fields.Text(string='Diagonis')
    is_assessment = fields.Boolean(string="Is assessment")

    def get_student_name(self):
        for re in self:
            re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)






