{
    'name': "Production Proj",
    'version': '1.0.0',
    'category': 'ERP',
    'author': 'Duy Van Nguyen',
    'sequence': -100,
    'summary': 'ERP Production Proj',
    'description': """
    ERP Production Proj.
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/color_view.xml',
        'views/kind_item_view.xml',
        'views/order_type_view.xml',
        'views/origin_view.xml',
        'views/master_item_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}