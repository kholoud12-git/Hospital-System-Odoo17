from email.policy import default

from odoo import fields, models,api,_


class HospitalOperationRoom(models.Model):
    _name = 'hospital.operation.room'
    _description = 'Operation Room Date'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'


    department_id = fields.Many2one('hospital.department', string='Department', tracking=True)
    occupied_bed_count = fields.Integer(string='Occupied Beds')
    is_available = fields.Boolean()
    bed_count = fields.Integer(string='Total Beds', default=1)
    state = fields.Selection([
        ('available', 'Available'),
        ('full', 'Full'),
        ('maintenance', 'Maintenance')
    ], string='Status', default='available', tracking=True)
    ref = fields.Char(readonly= True , default="NEW")
    appointment_ids = fields.One2many('hospital.appointment','room_id', string='Appointments')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('operation_room_seq') or 'NEW'
        return super(HospitalOperationRoom, self).create(vals_list)





