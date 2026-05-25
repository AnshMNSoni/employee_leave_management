from odoo import models, fields


class EmployeeManagement(models.Model):
    _name = 'employee.management'
    _description = 'Employee Management'

    name = fields.Char(string='Employee Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    department = fields.Char(string='Department')
    job_title = fields.Char(string='Job Title')
    joining_date = fields.Date(string='Joining Date')

    leave_request_ids = fields.One2many(
        'employee.leave',
        'employee_id',
        string='Leave Requests'
    )