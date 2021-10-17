import datetime
from odoo import models, fields, api, exceptions,_


class LapPatient(models.Model):
    _name = 'education.mouth'
    _description = 'Mouth'
    _order = "id desc"


    Photo= fields.Binary(string='Photo')
    patient_id = fields.Char(string='Student Number', readonly=True)
    name = fields.Char(string="full name", readonly=True)
    first = fields.Char(string="First Name", readonly=True)
    second = fields.Char(string="   Second Name", readonly=True)
    third = fields.Char(string="Third Name", readonly=True)
    last = fields.Char(string="Last Name", readonly=True)
    gender=fields.Char(string="gender", readonly=True)
    dob = fields.Date(string='Date Of Birth', readonly=True)
    age = fields.Integer(string='Age')
    date = fields.Char(string='Date', default=lambda self: datetime.datetime.today().strftime('%Y-%m-%d'),  readonly=True)
    phone = fields.Char(string="Phone", readonly=True)
    email = fields.Char(string="Email", readonly=True)
    hom = fields.Char(string="Home", readonly=True)
    nationality = fields.Char(string='Nationality', readonly=True)
    religion = fields.Char(string='Religion', readonly=True)
    program = fields.Char(string='Program', readonly=True)
    # The end personal information
    
    general = fields.Char(string="General Vision")
    withoutglss = fields.Char(string="With Out Glasses")
    withglasses = fields.Char(string='With  Glasses')
    color = fields.Char(string='Color Vision')
    near = fields.Char(string='Near Vision')
    normal = fields.Boolean(string='1.Normal')
    decayed = fields.Boolean(string='2.Decayed')
    missing = fields.Char(string='Missing')
    filled = fields.Char(string='Filled')
    othera = fields.Char(string='Other Abnormality')
    tongue = fields.Char(string='Tongue')
    
    assessment = fields.Text(string="Assessment")
    diagonis = fields.Text(string='Diagonis')

    is_assessment = fields.Boolean(string="Is assessment")
    dentist = fields.Char(string='Dentist', readonly=True, default=lambda self: self.env.user.name)




    def get_student_name(self):
        for re in self:
            re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)

            self.dentist = self.env.user.name





