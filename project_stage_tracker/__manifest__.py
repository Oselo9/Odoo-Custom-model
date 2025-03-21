{
    'name': 'Project Stage Tracker',
    'version': '17.0.1.0.0',
    'summary': 'Track time spent in each project task stage and report it in chatter',
    'description': 'This module tracks the number of days a project task spends in each stage and logs it in the chatter when the stage changes.',
    'author': 'OSELO9',
    'website': 'https://www.odoo.com/apps/modules/browse?author=OSELO9',
    'support': 'omar.iselo9@gmail.com',
    'category': 'Project',
    'depends': ['project'],
    'data': [
        'views/project_stage_tracker_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'price': 5.00,
    'currency': 'USD',
    'images': [
        'static/description/project-stage-tracker.png',
    ],
}
