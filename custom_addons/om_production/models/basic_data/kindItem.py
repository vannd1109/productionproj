from odoo import api, fields, models

class KindItem(models.Model):
    _name = 'basic.data.kind.item'
    _description = 'Kind Item'

    name = fields.Char(
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


