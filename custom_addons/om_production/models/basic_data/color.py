from odoo import api, fields, models

class Color(models.Model):
    _name = 'basic.data.color'
    _description = 'Color'

    fieldCode = fields.Char(
        string='FieldCode', translate=True)
    fieldValue = fields.Text(
        string="FieldValue",
        required=False)
    fieldValueVN = fields.Text(
        string="FieldValueVN",
        required=False)
    remarks = fields.Text(
        string="Remarks",
        required=False)




