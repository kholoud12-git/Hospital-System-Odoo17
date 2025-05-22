from email.policy import default

from odoo import fields, models, api, _


class HospitalMedicalRecord(models.Model):
    _name = 'hospital.medical.record'
    _description = 'Medical Record Date'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient')
    diagnosis = fields.Char(required=True)
    prescription = fields.Many2one('hospital.medication',string="Medication")
    doctor_id = fields.Many2one('hospital.doctor',string="Doctor")
    record_date = fields.Date(required=True)
