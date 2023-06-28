from odoo import api, fields, models


class Location(models.Model):
    _name = 'basic.data.location'
    _description = 'Location'

    warehouse = fields.Many2one(
        'basic.data.warehouse',
        string='Warehouse')

    location = fields.Char(
        string='Location')

    description = fields.Char(
        string='Description')

    group = fields.Selection(
        string='Group',
        selection=[('finding', 'Finding'),
                   ('metal', 'Metal'), ('stone', 'Stone'), ('rej', 'Rej')])
