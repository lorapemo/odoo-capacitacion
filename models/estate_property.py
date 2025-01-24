from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class estate_property(models.Model):
    _name = 'estate.property'
    _description = 'Registro de Ventas'
    _inherit = 'mail.thread'
    
    name = fields.Char(required=True, tracking=True)
    description = fields.Text(string="Descripcion")
    postcode = fields.Char(string="Codigo Postal", tracking=True)
    date_available = fields.Date(string="Fecha valida")
    expected_price = fields.Float(string="Precio Esperado")
    selling_price = fields.Float(string="Precio Venta")
    bedrooms = fields.Integer(string="Habitaciones")
    living_area = fields.Integer(string="Sala")
    facades = fields.Integer(string="Fachada")
    garage = fields.Boolean(string="Garaje")
    garden = fields.Boolean(string="Jardin")
    garden_area = fields.Integer(string="Tamaño del jardin")
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
    property_offer = fields.One2many(
        comodel_name = 'estate.property.offer',
        string= "Oferta",
        ondelete = 'set null',
        inverse_name = 'estate_property_id'
    )
    total_area = fields.Float(compute="_compute_area")
    best_offer = fields.Float(compute="_compute_best_offer")
    
    """ CAMPOS BOTONES """
    status = fields.Selection([
        ('sold', 'Vendido'),
        ('cancelled', 'Cancelado')
    ], string= 'Estado')

    @api.depends('garden_area', 'living_area')
    def _compute_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends('property_offer.price')
    def _compute_best_offer(self):
        for record in self:
            if record.property_offer:
                record.best_offer = max(record.property_offer.mapped('price'))
            else:
                record.best_offer = 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 1000.00
            self.garden_orientation = "nort"
        else:
            self.garden_area = 0
            self.garden_orientation = None

    def action_button_vendido(self):
        if 'cancelled' in self.mapped('status'):
            raise UserError("No podemos vender una propiedad cancelada")
        self.write({'status':'sold'})
    
    def action_button_cancelado(self):
        if 'sold' in self.mapped('status'):
            raise UserError("No podemos cancelar una propiedad vendida")
        self.write({'status':'cancelled'})

class estate_propery_type(models.Model):
    _name = 'estate.property.type'
    _description = 'Tipo de propiedad de la que se trata'

    name= fields.Char(string="Tipo de propiedad")

class estate_property_tag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Etiquetas descriptoras para propiedades'

    name= fields.Char(string='Etiqueta')

class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
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
    validity_days = fields.Integer(string = 'Validez (en días)', default=7)
    deadline = fields.Date(compute= "_compute_deadline", inverse="_inverse_deadline", store=True)

    @api.depends('validity_days', 'create_date')
    def _compute_deadline(self):
        for record in self:
            record.deadline = fields.Date.today() + timedelta(days=record.validity_days)
    
    def _inverse_deadline(self):
        for record in self:
            record.validity_days = (record.deadline - fields.Date.today()).days
            
    @api.onchange('deadline')
    def _onchange_deadline_days(self):
        for record in self:
            record.validity_days = (record.deadline - fields.Date.today()).days
