from odoo import api, fields, models

class Status(models.Model):
    _name = 'basic.data.status'
    _description = 'Status'

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



