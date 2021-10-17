import datetime
from odoo import models, fields, api, exceptions,_


class Lapcicology(models.Model):
    _name = 'education.assessment'
    _description = 'Psychological'
    _order = "id desc"


    patient_image = fields.Binary(string='Photo')
    patient_id = fields.Char(string='Student Number', readonly=True)
    date = fields.Char(string='Date', readonly=True, default=lambda self: datetime.datetime.today().strftime('%Y-%m-%d'))
    name = fields.Char(string="Student Name", readonly=True)
    first = fields.Char(string="First Name", readonly=True)
    second = fields.Char(string="Second Name", readonly=True)
    third = fields.Char(string="Third Name", readonly=True)
    last = fields.Char(string="Last Name", readonly=True)
    gender = fields.Char(string="Gender", readonly=True)
    nationality = fields.Char(string='Nationality', readonly=True)
    religion = fields.Char(string='Religion', readonly=True)
    program = fields.Char(string='Program', readonly=True)
    social = fields.Char(string='Social State', readonly=True)
    dob = fields.Date(string='Date Of Birth', readonly=True)

    desir = fields.Boolean(string="Did you College on your Own Wish?")
    reson = fields.Text(string="If Answer is no, State the Reason")

    father = fields.Boolean(string="Is The Father Alive?")
    old = fields.Text(string="If Answer is no,how old were you?")

    mother = fields.Boolean(string="Is The Mother Alive?")
    old2 = fields.Text(string="If Answer is no,how old were you?")



    internal_family = fields.Boolean(string='Do you have disagreement within your Family?')
    relation = fields.Boolean(string='Has there been a Divorce or Separation between the Father and Mother?')
    married = fields.Boolean(string='Is The Father Or Mother Married to Another?')

    father2 = fields.Boolean(string='Do you Live With The Father')
    mother2 = fields.Boolean(string='Do you Live With The Mother')
    friend = fields.Boolean(string='Do you Live With The Friend')

    number_brother = fields.Char(string='How Many Sibling do you Have?')
    number_family = fields.Char(string='Your Arrangement in the Family')
    number_brother2 = fields.Char(string='How Many non-Brother do you Have?')

    job_father = fields.Char(string='Guardians Profession')
    level_edu = fields.Char(string='Education Level')
    job_mother = fields.Char(string='Mother Profession')
    level_edu2 = fields.Char(string='Her Education Level')
    applicant = fields.Char(string='Parent Name', readonly=True)
    phone = fields.Char(string='Parent Phone', readonly=True)
# ************************ page 2
    sit = fields.Boolean(string='Are You Get Board And Unable To Sit IN One Please ?')
    dessition = fields.Boolean(string='Are You too Reluctant to Make a Decision?')
    feel = fields.Boolean(string='Are You Very Suspicious and Like to Repeat Actions?')
    agrasive = fields.Boolean(string='Are You Very Irritable and Nervous?')
    fried = fields.Boolean(string='Do You Feel Afraid of Something Specific?')
    
    died = fields.Boolean(string='Did You Happen To BE Thinking About Dying ?')
    any = fields.Boolean(string='Have You Ever Thought About Putting An End To Your Life ? ')
    arag = fields.Boolean(string='Is There Thinner ?')

    setting = fields.Boolean(string='Are You Tend To Sit Alone ?')
    magistion = fields.Boolean(string='Did You Happen To See Pictures Of People Around You ?')
    smale = fields.Boolean(string='Do You Smell That You Do not ? ')

    hear = fields.Boolean(string='Do You Hear Voices Calling For You That Other People Do not Hear ? ')
    foil = fields.Boolean(string=' Are You So Many Depressing Ideas Follow You All Day ? ')
    friends = fields.Boolean(string='If You Disagree With A Friend Or Colleague , You Deal Violent ? ')
    mode = fields.Boolean(string='Are You Mood Changer ?')

    hate = fields.Boolean(string='You Think Some People That You And Lurk TO Hurt You ?  ')
    oppressed = fields.Boolean(string='Do You Feel Oppressed In Society  ')
    magic2 = fields.Boolean(string='Do You Ever Feel Like Bites Put Magic Or Poison Into Eating Or Drinking ?')
    solve = fields.Boolean(string='Are You Seeking To Resolve Differences Between Others ?')
    mis_tack = fields.Boolean(string='Do You Have Any Kind Of Disable ?')
    sycologist = fields.Boolean(string='If Neceeary I Offered A Psychologist To Help You , Would You Accept It Or Not?')
    volnteer = fields.Boolean(string='Do You Like Voluntary Work ? ')


    # 
    look = fields.Char(string='General Look')
    behavior = fields.Char(string='General Behavior')

    place = fields.Char(string='Perception Of Time and Place')
    note = fields.Text(string='General Notes')
    dotor = fields.Char(string='Psychologist', readonly=True, default=lambda self: self.env.user.name)

    def get_student_name(self):
        for re in self:
            re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)




