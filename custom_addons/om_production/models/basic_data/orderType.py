from odoo import api, fields, models

class OrderType(models.Model):
    _name = 'basic.data.order.type'
    _description = 'Order Type'

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


