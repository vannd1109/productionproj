from odoo import api, fields, models

class Origin(models.Model):
    _name = 'basic.data.origin'
    _description = 'Origin'

    fieldCode = fields.Char(
        string='FieldCode')
    name = fields.Char(
        string="FieldValue",
        required=False)
    fieldValueVN = fields.Char(
        string="FieldValueVN",
        required=False)
    remarks = fields.Char(
        string="Remarks",
        required=False)


