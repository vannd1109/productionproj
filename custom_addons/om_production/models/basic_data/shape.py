from odoo import api, fields, models

class Shape(models.Model):
    _name = 'basic.data.shape'
    _description = 'Shape'

    fieldCode = fields.Char(
        string='FieldCode')
    name = fields.Char(
        string="FieldValue",
        required=False)
    fieldValueVN = fields.Char(
        string="FieldValueVN",
        required=False)
    remarks = fields.Text(
        string="Remarks",
        required=False)



