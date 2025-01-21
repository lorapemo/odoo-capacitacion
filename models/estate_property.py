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
    