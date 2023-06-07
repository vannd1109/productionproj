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
        'views/basic_data/color_view.xml',
        'views/basic_data/kind_item_view.xml',
        'views/basic_data/order_type_view.xml',
        'views/basic_data/origin_view.xml',
        'views/basic_data/quality_view.xml',
        'views/basic_data/shape_view.xml',
        'views/basic_data/status_view.xml',
        'views/basic_data/structure_view.xml',
        'views/basic_data/tech_group_view.xml',
        'views/basic_data/unit_view.xml',
        'views/basic_data/item_type_view.xml',
        'views/basic_data/customer_view.xml',
        'views/master_data/master_item_view.xml',
        'views/follow_customer/follow_customer_order_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'om_production/static/src/js/tree_button.js',
            # 'om_production/static/src/xml/tree_button.xml',
            # 'button_near_create/static/src/js/kanban_button.js',
        ],
        'web.assets_qweb': [
            'om_production/static/src/xml/tree_button.xml',
        ],
    },
    'license': 'LGPL-3',
}
