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
        'views/basic_data/production_step_view.xml',
        'views/basic_data/worker_center_view.xml',
        'views/basic_data/warehouse_view.xml',
        'views/basic_data/location_view.xml',
        'views/basic_data/lop_view.xml',
        'views/basic_data/worker_team_view.xml',
        'views/basic_data/sites_view.xml',
        'views/basic_data/production_process_view.xml',
        'views/master_data/master_item_view.xml',
        'views/follow_customer/follow_customer_order_view.xml',
        'views/report/view_bag_view.xml',
        'views/report/view_bag_summary_by_customer_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
