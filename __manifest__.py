{
    'name': 'Employee Leave Management',
    'version': '1.0',
    'summary': 'Manage employee leave requests',
    'description': 'Custom module for managing employees leave requests in Odoo',
    'author': 'Ansh Soni',
    'category': 'HR',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/leave_approval_wizard_views.xml',
        'views/employee_views.xml',
        'views/leave_type_views.xml',
        'views/leave_request_views.xml',
        'views/leave_templates.xml',
    ],
    'installable': True,
    'application': True,
}