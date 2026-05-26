from odoo import http
from odoo.http import request


class LeaveController(http.Controller):

    @http.route(
        ['/contact-us', '/leave-request'],
        type='http',
        auth='public',
        website=True
    )
    def leave_page(self, **kwargs):
        # Fetch active employees and leave types to populate the dropdowns
        employees = request.env['employee.management'].sudo().search([])
        leave_types = request.env['leave.type'].sudo().search([])
        
        return request.render(
            'employee_leave_management.leave_request_page', {
                'employees': employees,
                'leave_types': leave_types,
            }
        )

    @http.route(
        '/leave/submit',
        type='http',
        auth='public',
        methods=['POST'],
        website=True
    )
    def submit_leave(self, **post):
        employee_id = post.get('employee_id')
        leave_type_id = post.get('leave_type_id')
        
        if employee_id and leave_type_id:
            request.env['employee.leave'].sudo().create({
                'employee_id': int(employee_id),
                'leave_type_id': int(leave_type_id),
                'start_date': post.get('start_date'),
                'end_date': post.get('end_date'),
                'reason': post.get('reason'),
                'status': 'submitted',
            })

        return request.redirect('/leave/thank-you')

    @http.route(
        '/leave/thank-you',
        type='http',
        auth='public',
        website=True
    )
    def thank_you(self):
        return request.render(
            'employee_leave_management.thank_you_page'
        )