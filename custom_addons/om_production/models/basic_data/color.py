from odoo import api, fields, models

class Color(models.Model):
    _name = 'basic.data.color'
    _description = 'Color'

    name = fields.Char(
        string='FieldCode')

    fieldValue = fields.Char(
        string="FieldValue",
        required=False)

    fieldValueVN = fields.Char(
        string="FieldValueVN",
        required=False)

    remarks = fields.Char(
        string="Remarks",
        required=False)


