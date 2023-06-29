from odoo import api, fields, models

class Color(models.Model):
    _name = 'basic.data.color'
    _description = 'Color'

    ColorCode = fields.Char(
        string='ColorCode')

    ColorName = fields.Char(
        string="ColorName",
        required=False)

    ColorNameVN = fields.Char(
        string="ColorNameVN",
        required=False)

    Remarks = fields.Char(
        string="Remarks",
        required=False)


