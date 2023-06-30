from odoo import api, fields, models


class Location(models.Model):
    _name = 'basic.data.location'
    _description = 'Location'

    warehouse = fields.Many2one(
        'basic.data.warehouse',
        string='Warehouse', required=True)

    location = fields.Char(
        string='Location', required=True)

    description = fields.Char(
        string='Description', required=True)

    group = fields.Selection(
        string='Group',
        selection=[('finding', 'Finding'),
                   ('metal', 'Metal'), ('stone', 'Stone'), ('rej', 'Rej')], required=True)
