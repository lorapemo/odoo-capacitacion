from odoo import models, fields

class estate_property(models.Model):
    _name = 'estate.property'
    _description = 'Registro de Ventas'
    
    name = fields.Char(required=True)
    description = fields.Text(string="Descripcion")
    postcode = fields.Char(string="Codigo Postal")
    date_available = fields.Date(string="Fecha valida")
    expected_price = fields.Float(string="Precio Esperado")
    selling_price = fields.Float(string="Precio Venta")
    bedrooms = fields.Integer(string="Habitaciones")
    living_area = fields.Integer(string="Sala")
    facades = fields.Integer(string="Fachada")
    garage = fields.Boolean(string="Garaje")
    garden = fields.Boolean(string="Jardin")
    garden_Area = fields.Integer(string="Tamaño del jardin")
    garden_orientation = fields.Selection([
        ('nort','Norte'),
        ('south','Sur'),
        ('west','Oeste'),
        ('east','Este'),
    ], string= "Orientacion")
    property_type_id = fields.Many2one(
        comodel_name = 'estate.property.type',
        string = "Tipo de propiedad",
        ondelete = 'set null'
    )
    buyer = fields.Many2one(
        comodel_name = 'res.partner',
        string = "Comprador",
        ondelete = 'set null'
    )
    seller = fields.Many2one(
        comodel_name = 'res.users',
        string = "Vendedor",
        default= lambda self: self.env.user,
        ondelete = 'set null'
    )
    property_tags = fields.Many2many(
        comodel_name = 'estate.property.tag'
    )
    property_offers = fields.One2many(
        comodel_name = 'estate.property.offers',
        string= "Oferta",
        ondelete = 'set null',
        inverse_name = 'estate_property_id'
    )

class estate_propery_type(models.Model):
    _name = 'estate.property.type'
    _description = 'Tipo de propiedad de la que se trata'

    name= fields.Char(string="Tipo de propiedad")

class estate_property_tag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Etiquetas descriptoras para propiedades'

    name= fields.Char(string='Etiqueta')

class estate_property_offers(models.Model):
    _name = 'estate.property.offers'
    _description = 'Ofertas hechas por la propiedad'

    price = fields.Float(string='Precio ofrecido')
    status = fields.Selection([
        ('accepted','Aceptado'),
        ('denied','Rechazado')
    ],
    string = 'Estatus',
    copy = False
    )
    buyer = fields.Many2one(
        comodel_name = 'res.partner',
        string = "Comprador",
        ondelete = 'set null',
        #required = True
    )
    estate_property_id = fields.Many2one(
        comodel_name = 'estate.property',
        string = "Propiedad",
        ondelete = 'set null',
        #required = True
    )