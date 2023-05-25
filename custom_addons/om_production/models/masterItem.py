from odoo import api, fields, models

class MaterItem(models.Model):
    _name = 'master.item'
    _description = 'MasterItem'

    name = fields.Char(
        string='Name')
    age = fields.Integer(
        string='Age')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('female', 'Female'), ])


