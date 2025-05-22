from email.policy import default

from odoo import fields, models,api,_


class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _description = 'Department Date'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    name = fields.Char(required= True )
    description = fields.Char()
    manager_name = fields.Many2one('hospital.doctor')
    ref = fields.Char(readonly= True , default="NEW")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('department_seq') or 'NEW'
        return super(HospitalDepartment, self).create(vals_list)





