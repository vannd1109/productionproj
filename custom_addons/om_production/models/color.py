from odoo import api, fields, models

class Color(models.Model):
    _name = 'basic.data.color'
    _description = 'Color'

    name = fields.Char(
        string='Name')
    age = fields.Integer(
        string='Age')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('female', 'Female'), ])



