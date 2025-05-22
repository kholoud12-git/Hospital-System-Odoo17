from email.policy import default

from odoo import fields, models, api, _


class HospitalLabAppointment(models.Model):
    _name = 'hospital.lab.appointment'
    _description = 'Hospital Lab Appointment Date'


    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    test_type = fields.Char(required=True)
    lab_technician_id = fields.Many2one('hospital.doctor', string="Technician", required=True)
    appointment_date = fields.Date(required=True)
    status = fields.Selection([
        ('done', 'Done'),
        ('draft', 'Draft'),
    ], required=True)
