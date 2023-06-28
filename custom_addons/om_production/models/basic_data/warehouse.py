from odoo import api, fields, models


class Warehouse(models.Model):
    _name = 'basic.data.warehouse'
    _description = 'Warehouse'

    name = fields.Char(
        string='Warehouse')

    description = fields.Char(
        string='Description')
