from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EmployeeLeaveApprovalWizard(models.TransientModel):
    _name = 'employee.leave.approval.wizard'
    _description = 'Employee Leave Approval Wizard'

    leave_id = fields.Many2one(
        'employee.leave',
        string='Leave',
        required=True
    )

    action = fields.Selection([
        ('approve', 'Approve'),
        ('reject', 'Reject')
    ], string='Action', required=True, default='approve')

    manager_note = fields.Text(string='Manager Note')

    def action_confirm(self):
        self.ensure_one()

        if self.action == 'approve':
            new_status = 'approved'
        else:
            new_status = 'rejected'

        if self.leave_id.status == new_status:
            raise ValidationError('Leave already has this status.')

        self.leave_id.write({
            'status': new_status
        })

        return {'type': 'ir.actions.act_window_close'}
