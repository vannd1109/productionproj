from odoo import api, fields, models

class Origin(models.Model):
    _name = 'origin'
    _description = 'Origin'

    name = fields.Char(
        string='Name')
    age = fields.Integer(
        string='Age')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('female', 'Female'), ])


