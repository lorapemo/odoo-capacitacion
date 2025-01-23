{
    'name' : 'Venta de Bienes',
    'version' : '0.1',
    'author' : 'Lorenzo Perez',
    'description' : 'Ventas de bienes raices',
    'depends' : [
        'base',
        'account'
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml'
    ],
    'application' : True,
    'installable' : True
}