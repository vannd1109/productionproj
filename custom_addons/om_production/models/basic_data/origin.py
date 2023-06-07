from odoo import api, fields, models

class Origin(models.Model):
    _name = 'basic.data.origin'
    _description = 'Origin'

    fieldCode = fields.Char(
        string='FieldCode')
    fieldValue = fields.Text(
        string="FieldValue",
        required=False)
    fieldValueVN = fields.Text(
        string="FieldValueVN",
        required=False)
    remarks = fields.Text(
        string="Remarks",
        required=False)


