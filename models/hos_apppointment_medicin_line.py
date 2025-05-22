from odoo import models, fields, api, _
from datetime import datetime, date, timedelta
from odoo.exceptions import ValidationError
from dateutil import relativedelta


class HospitalMedclineLines(models.Model):
    _name = 'hospital.appointment.medicine.line'
    _description = 'Medcline Lines'
    _log_access = True
    _inherit = ['mail.thread', 'mail.activity.mixin']

    medicine_id = fields.Many2one('hospital.medication', string = 'Medicine')
    quantity = fields.Float(string = 'quantity', digits =(20,2))
    doze_per_day = fields.Float(string = 'Doze Per Day', digits =(20,2))
    appointment_id = fields.Many2one('hospital.appointment', string='appointments')
    tax_ids = fields.Many2one('hospital.taxes',related='medicine_id.taxes_id', string='Taxes')


