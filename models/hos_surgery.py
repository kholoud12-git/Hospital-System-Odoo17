from email.policy import default

from odoo import fields, models,api,_


class HospitalSurgery(models.Model):
    _name = 'hospital.surgery'
    _description = 'Surgery Date'


    ref = fields.Char(readonly=True, default="NEW")
    patient_id = fields.Many2one('hospital.patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', required=True)
    room_id = fields.Many2one('hospital.operation.room', required=True)
    surgery_type = fields.Selection([
        ('elective','Elective'),
        ('emergency','Emergency'),
    ],required= True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], required=True)
    notes = fields.Text()
    scheduled_time = fields.Date()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital_surgery_seq') or 'NEW'
        return super(HospitalSurgery, self).create(vals_list)




