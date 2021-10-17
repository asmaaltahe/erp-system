import datetime
from odoo import models, fields, api, exceptions,_


class LapPatient(models.Model):
    _name = 'education.physical'
    _description = 'physical'
    _order = "id desc"


    Photo= fields.Binary(string='Photo')
    patient_id = fields.Char(string='Student Number', readonly=True)
    student_ids = fields.Char(string="student_ids")
    name = fields.Char(string="full name", readonly=True)
    first = fields.Char(string="First Name", readonly=True)
    second = fields.Char(string="   Second Name", readonly=True)
    third = fields.Char(string="Third Name", readonly=True)
    last = fields.Char(string="Last Name", readonly=True)
    gender = fields.Char(string="Gender", readonly=True)
    dob = fields.Date(string='Date Of Birth', readonly=True)
    age = fields.Integer(string='Age')
    date = fields.Char(string='Date', default=lambda self: datetime.datetime.today().strftime('%Y-%m-%d'),  readonly=True)
    phone = fields.Char(string="Phone", readonly=True)
    email = fields.Char(string="Email", readonly=True)
    nationality = fields.Char(string='Nationality', readonly=True)
    religion = fields.Char(string='Religion', readonly=True)
    program = fields.Char(string='Program', readonly=True)
    hom = fields.Char(string="Home", readonly=True)
    # The End Personal Information

    general = fields.Char(string='General')
    appearance = fields.Char(string='Appearance')
    constitution = fields.Char(string='Constitution')
    normal = fields.Char(string="Normal")
    abnormal = fields.Char(string="Abnormality")
    normal_one = fields.Char(string='Normal')
    enlarge = fields.Char(string='Enlarged')
    normal_two = fields.Char(string='Normal')
    external = fields.Char(string='Otitis External') 
    media = fields.Char(string='Otitis Media')
    hearing = fields.Char(string='Hearing') 
    nose = fields.Char(string='Nose')
    general_one = fields.Char(string='General')
    clear = fields.Char(string='Clear')
    abnormality = fields.Char(string='Abnormality') 
    normal_th = fields.Char(string='Normal')
    abnormal_th = fields.Char(string='Abnormality') 
    general_fo = fields.Char(string='General') 
    normal_fo = fields.Char(string='Normal')
    paipable = fields.Char(string='Paipable Finger b.c.m')
    normal_no = fields.Char(string='Normal')
    paip = fields.Char(string='Paipable Finger')
    other = fields.Char(string='Other Massas') 
    fluid = fields.Char(string='Fluid')
    hernia = fields.Char(string='Hernia')
    genitalia = fields.Char(string='Genitalia')
    lower = fields.Char(string='Lower Limbs')
    intell = fields.Char(string='Intelligence')
    speech = fields.Char(string='Speech')
    fungi = fields.Char(string='Fungi') 
    cranial = fields.Char(string='Cranial Nerves')
    motor = fields.Char(string='Motor System')
    sensory = fields.Char(string='Sensory System')
    reflexes = fields.Char(string='Reflexes')
    skin = fields.Char(string='Skin')
    comment = fields.Char(string='Comment On Examination')
    upper = fields.Char(string='Upper Limps')
    thyroid = fields.Char(string='Thyroid')
    central = fields.Char(string='Central')
    deviated = fields.Char(string='Deviated to Rt/Left')
    
    assessment = fields.Text(string="Assessment")
    diagonis = fields.Text(string='Diagonis')
    doctor_name = fields.Char(string='Doctor name', readonly=True, default=lambda self: self.env.user.name)
    result = fields.Char(string="Result")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)

    userid = fields.Char("User ID", default=lambda self: self.env.user.name)

    def get_student_name(self):
        for re in self:
            re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)




