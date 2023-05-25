from odoo import api, fields, models

class KindItem(models.Model):
    _name = 'kind.item'
    _description = 'Kind Item'

    name = fields.Char(
        string='Name')
    age = fields.Integer(
        string='Age')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('female', 'Female'), ])


