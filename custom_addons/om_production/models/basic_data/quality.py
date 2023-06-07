from odoo import api, fields, models

class Quality(models.Model):
    _name = 'basic.data.quality'
    _description = 'Quality'

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



