from odoo import api, fields, models

class Unit(models.Model):
    _name = 'basic.data.unit'
    _description = 'Unit'

    fieldCode = fields.Char(
        string='FieldCode')
    name = fields.Text(
        string="FieldValue",
        required=False)
    fieldValueVN = fields.Text(
        string="FieldValueVN",
        required=False)
    remarks = fields.Text(
        string="Remarks",
        required=False)



