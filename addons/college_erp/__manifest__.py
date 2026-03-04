{
    'name': 'College ERP',
    'version': '1.0',
    'summary': 'An ERP college education',
    'author': 'Andrii Chychkan',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'category': 'Education',
    'sequence': 1,
    'data': [
        'views/college_student_views.xml',
        'views/college_erp_menus.xml',
        'security/ir.model.access.csv',
    ],
}
