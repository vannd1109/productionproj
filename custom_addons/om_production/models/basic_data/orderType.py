from odoo import api, fields, models

class OrderType(models.Model):
    _name = 'basic.data.order.type'
    _description = 'Order Type'

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


