from email.policy import default

from odoo import fields, models,api,_


class HospitalAdmission(models.Model):
    _name = 'hospital.admission'
    _description = 'Admission Date'
    _rec_name = 'patient_id'


    patient_id = fields.Many2one('hospital.patient', required= True )
    reason = fields.Text()
    admission_date = fields.Date(required= True)
    discharge_date = fields.Date(required= True)
    room_number = fields.Integer(required= True)




