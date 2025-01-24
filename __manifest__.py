{
    'name' : 'Venta de Bienes',
    'version' : '0.1',
    'author' : 'Lorenzo Perez',
    'description' : 'Ventas de bienes raices',
    'depends' : [
        'base',
        'account',
        'mail'
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_offer_view.xml',
        'views/fleet_spending_view.xml'
    ],
    'application' : True,
    'installable' : True
}