from email.policy import default

from odoo import fields, models, api, _


class HospitalInvoice(models.Model):
    _name = 'hospital.invoice'
    _description = 'Invoices Date'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', required=True)
    appointment_id = fields.Many2one('hospital.appointment',required=True)
    total_amount = fields.Float()
    paid_amount = fields.Float()
    payment_status = fields.Selection(
        selection=[('paid', 'Paid'), ('unpaid', 'Unpaid')])
    invoice_date = fields.Date(required=True)
    ref = fields.Char(readonly=True, default="NEW")


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('invoice_seq') or 'NEW'
        return super(HospitalInvoice, self).create(vals_list)
