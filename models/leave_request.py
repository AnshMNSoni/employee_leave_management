from odoo import models, fields, api
from datetime import timedelta


class EmployeeLeave(models.Model):
    _name = 'employee.leave'
    _description = 'Employee Leave Request'

    employee_id = fields.Many2one(
        'employee.management',
        string='Employee',
        required=True
    )

    leave_type_id = fields.Many2one(
        'leave.type',
        string='Leave Type',
        required=True
    )

    start_date = fields.Date(
        string='Start Date',
        required=True
    )

    end_date = fields.Date(
        string='End Date',
        required=True
    )

    reason = fields.Text(string='Reason', required=True)

    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft')

    total_days = fields.Integer(
        string='Total Days',
        compute='_compute_total_days',
        store=True
    )

    @api.depends('start_date', 'end_date')
    def _compute_total_days(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.total_days = (
                    rec.end_date - rec.start_date
                ).days + 1
            else:
                rec.total_days = 0