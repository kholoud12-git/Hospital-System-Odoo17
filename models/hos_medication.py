from email.policy import default

from odoo import fields, models, api, _


class HospitalMedication(models.Model):
    _name = 'hospital.medication'
    _description = 'Medication Date'
    _rec_name = 'name'

    name = fields.Char(required=True)
    ref = fields.Char(readonly= True , default="NEW")
    is_active = fields.Boolean()
    price = fields.Float(string="Price", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    expiry_date = fields.Date(required=True)
    taxes_id = fields.Many2one('hospital.taxes',string="Taxes")


    medication_patient_id = fields.Many2one('hospital.patient',string="Medication")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('medication_seq') or 'NEW'
        return super(HospitalMedication, self).create(vals_list)