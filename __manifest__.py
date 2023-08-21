
{
    'name': 'Appeul Inherits',
    'version': '16.0.1.0.2',
    'summary': 'Appeul - Inherits',
    'description': """POS - Remove quotations button, Remove Invoice Button
                       Remove / change browser title
                       Remove / Odoo branding : on portal page!!
                       Remove / Odoo branding on login page!!
                        """,
    'author': 'Appeul Services',
    'company': 'Appeul',
    'maintainer': 'Appeul Services',
    'category': 'Sales',
    'website': 'https://www.appeul.com',
    'sequence':"-1110",
    'depends': ['base', 'point_of_sale', 'pos_sale', 'web','portal','auth_signup','mail','base_setup', 'sale'],
    'data': [
        'security/security.xml',
        'views/payment_button_invisible.xml',
        "views/ir_ui_menu.xml",
        "views/login_templates.xml",
        "views/ap_res_config_settings_views.xml",
   ],

    'installable': True,
    'application': True,
    'assets': {
            'point_of_sale.assets': [
                'ap_inherits/static/src/js/models.js',
                'ap_inherits/static/src/js/get_total_amount.js',
                'ap_inherits/static/src/xml/pos.xml',
                'ap_inherits/static/src/xml/receipt_add_usd.xml',
                'ap_inherits/static/src/xml/pos_quotation_button.xml',
                ('remove', 'pos_sale/static/src/js/SetSaleOrderButton.js'),
                ('remove', 'pos_sale/static/src/xml/SetSaleOrderButton.xml'),


            ],
            "web.assets_backend": [
                "ap_inherits/static/src/js/user_menu_items.esm.js",

            ],

            'web.assets_backend_prod_only': [
                'ap_inherits/static/src/js/favicon.js',
            ],

        },

    'license': 'LGPL-3',

}
