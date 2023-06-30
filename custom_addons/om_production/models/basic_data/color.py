from odoo import api, fields, models

class Color(models.Model):
    _name = 'basic.data.color'
    _description = 'Color'
    _rec_name = "colorCode"

    colorCode = fields.Char(
        string='ColorCode', required=True)

    colorName = fields.Char(
        string="ColorName", required=True)

    colorNameVN = fields.Char(
        string="ColorNameVN", required=True)

    remarks = fields.Char(
        string="Remarks", required=False)


