from odoo import models, fields


class LeaveType(models.Model):
    _name = 'leave.type'
    _description = 'Leave Type'

    name = fields.Char(string='Leave Type', required=True)
    max_days = fields.Integer(string='Maximum Days')
    is_paid = fields.Boolean(string='Paid Leave')