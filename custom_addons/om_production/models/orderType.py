from odoo import api, fields, models

class OrderType(models.Model):
    _name = 'order.type'
    _description = 'Order Type'

    name = fields.Char(
        string='Name')
    age = fields.Integer(
        string='Age')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('female', 'Female'), ])


