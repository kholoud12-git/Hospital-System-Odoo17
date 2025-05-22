from email.policy import default

from odoo import fields, models,api,_


class HospitalAppointments(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointments Date'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'


    patient_id = fields.Many2one('hospital.patient', string="Patient",required= True )
    doctor_id = fields.Many2one('hospital.doctor', required= True )
    ref = fields.Char(readonly= True , default="NEW")
    appointment_date = fields.Date(string='Date', required=True, tracking=True)
    appointment_time = fields.Float(string='Time', required=True, tracking=True,
                                    help="Example: 13.5 = 1:30 PM")
    medicine_line_ids = fields.One2many('hospital.appointment.medicine.line', 'appointment_id', string="Lines")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    department_id = fields.Many2one('hospital.department', string='Department')
    room_id = fields.Many2one('hospital.operation.room', string='Room')


    patient_status = fields.Selection([
        ('ambulatory', 'Ambulatory'),
        ('outpatient', 'Outpatient'),
        ('inpatient', 'Inpatient'),
    ],  default='outpatient')
    symptoms = fields.Text(string='Symptoms')
    diagnosis = fields.Text(string='Diagnosis')
    prescription = fields.Text(string='Prescription')
    comments = fields.Text()
    total_medicine_qty = fields.Float(string = 'Total Medicines', compute="_compute_total_medicine_qty" )



    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('appointment_seq') or 'NEW'
        return super(HospitalAppointments, self).create(vals_list)

    @api.depends('medicine_line_ids')
    def _compute_total_medicine_qty(self):
        for rec in self:
            total_medicine = 0
            for line in rec.medicine_line_ids:
                total_medicine += line.quantity
            rec.total_medicine_qty = total_medicine


    def print_prescription_report(self):
        return self.env.ref('hospital_management.prescription_report').report_action(self)
