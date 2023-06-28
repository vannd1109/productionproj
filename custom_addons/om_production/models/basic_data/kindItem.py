from odoo import api, fields, models

class KindItem(models.Model):
    _name = 'basic.data.kind.item'
    _description = 'Kind Item'

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


