{
    'name': 'To-Do App',
    'author': 'Khalil Hamwi',
    'version': '17.0.0.1.0',
    'summary': """To Do List""",
    'description': """todo list app""",
    'sequence': 3,
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'reports/todo_task_report.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
