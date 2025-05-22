from email.policy import default

from odoo import fields, models, api, _


class HospitalMonthlyReport(models.Model):
    _name = 'hospital.monthly.report'
    _description = 'Hospital Monthly Report Date'


    report_month = fields.Date(required=True)
    total_patient = fields.Integer()
    total_appointment = fields.Integer()
    total_income = fields.Integer()
    total_expenses = fields.Integer()
    most_common_disease = fields.Text()
    notes = fields.Text()
