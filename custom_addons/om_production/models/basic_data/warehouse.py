from odoo import api, fields, models


class Warehouse(models.Model):
    _name = 'basic.data.warehouse'
    _description = 'Warehouse'
    _rec_name = 'wareHouseCode'

    wareHouseCode = fields.Char(
        string='WareHouseCode', required=True)

    wareHouseDescription = fields.Char(
        string='WareHouseDescription', required=True)
