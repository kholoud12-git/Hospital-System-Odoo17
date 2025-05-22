from email.policy import default

from odoo import fields, models,api,_
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Data'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required= True )
    ref = fields.Char(readonly= True , default="NEW")
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True)
    photo = fields.Binary(string="Picture")
    date_of_birth = fields.Date(required= True)
    marital_status = fields.Selection([
        ('married','Married'),
        ('unmarried','Unmarried'),
        ('single','Single'),
    ],required= True)

    patient_age = fields.Char(compute='_compute_age', store=True)
    address = fields.Char(required= True)
    email = fields.Char()
    phone = fields.Char(string='Phone Number')
    national_id = fields.Char(string='National ID')
    patient_critical_information = fields.Text()
    insurance_policy_number = fields.Char(string='Insurance Policy Number')
    blood_type = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string='Blood Type')
    rh_type = fields.Selection([('+', '+'),('-', '-')], string ="RH")
    extra_information = fields.Text(string="Patient Extra Information")
    deceased = fields.Boolean(default=False)
    deceased_date = fields.Date( string="Date of Death")
    cause_death = fields.Char(string="Cause of Death?")
    medication_id = fields.One2many('hospital.medication', 'medication_patient_id')
    nurse_id = fields.Many2one('hospital.nurse')


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('patient_seq') or 'NEW'
        return super(HospitalPatient, self).create(vals_list)

    def print_patient(self):
        return self.env.ref('hospital_management.patient_report').report_action(self)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                age = today.year - record.date_of_birth.year - (
                        (today.month, today.day) < (record.date_of_birth.month, record.date_of_birth.day)
                )
                record.patient_age = f"{age} years"
            else:
                record.patient_age = "No DOB"


    @api.model
    def add_action_for_patient(self):
        action = self.env.ref('hospital_management.hospital_patient_action')
        if self.env.user.has_group('hospital_management.group_hospital_male_patient'):
            action['domain'] = [('sex', '=', 'female')]
        return action




