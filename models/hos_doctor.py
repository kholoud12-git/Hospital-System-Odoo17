from email.policy import default

from odoo import fields, models,api,_
from odoo.odoo.exceptions import ValidationError


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Date'
    _rec_name = 'name'


    name = fields.Char(required= True )
    license_number = fields.Char(string='License Number', required=True, tracking=True)
    specialization = fields.Selection([
        ('doctor','Doctor'),
        ('pharmacist','Pharmacist'),
        ('nurse','Nurse'),
        ('medical laboratory technician','Medical Laboratory Technician'),
        ('receptionist','Receptionist'),
    ],required= True, tracking=True)
    ref = fields.Char(readonly=True, default="NEW")
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    department_id = fields.Many2one('hospital.department', required= True )
    comments = fields.Text()
    available_from = fields.Float(string='Available From (HH.MM)', help="Example: 9.5 means 9:30 AM")
    available_to = fields.Float(string='Available To (HH.MM)', help="Example: 17.0 means 5:00 PM")
    photo = fields.Binary(string="Doctor Image")


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'ref' not in vals or vals['ref'] == 'NEW':
                vals['ref'] = self.env['ir.sequence'].next_by_code('doctor_seq') or 'NEW'
        return super(HospitalDoctor, self).create(vals_list)





