from email.policy import default

from odoo import fields, models,api,_
from datetime import date

from odoo.odoo.exceptions import ValidationError


class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _description = 'Nurse Data'
    _rec_name = 'name'

    name = fields.Char(required= True )
    ref = fields.Char(readonly=True, default="NEW")
    department_id = fields.Many2one('hospital.department')
    shift_start = fields.Date()
    shift_end = fields.Date()
    mobile = fields.Integer()
    assigned_patient = fields.One2many('hospital.patient', 'nurse_id')
    status = fields.Selection([('work', 'work'), ('not work', 'Not Work')], required= True , default='work')


