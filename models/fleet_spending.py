from odoo import models, fields

class fleet_spending(models.Model):
    _inherit = ['account.move']

    maintainment_spending = fields.Float(string="Gastos por mantenimiento")
    autorized_spending = fields.Float(string="Gastos autorizados")