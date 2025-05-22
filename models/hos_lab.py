from email.policy import default

from odoo import fields, models, api, _


class HospitalLaboratory(models.Model):
    _name = 'hospital.laboratory'
    _description = 'Hospital Laboratory Date'
    _rec_name = 'ref'


    ref = fields.Char(readonly= True , default="NEW")
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    test_type = fields.Char(required=True)
    test_date = fields.Date(required=True)
    result = fields.Text()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('laboratory_seq') or 'NEW'
        return super(HospitalLaboratory, self).create(vals_list)
