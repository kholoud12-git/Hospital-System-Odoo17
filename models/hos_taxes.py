from email.policy import default

from odoo import fields, models, api, _


class HospitalTaxes(models.Model):
    _name = 'hospital.taxes'
    _description = 'Medication Taxes Date'
    _rec_name = 'name'

    name = fields.Char(required=True, string="Tax Name")


