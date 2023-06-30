from odoo import api, fields, models

class OrderType(models.Model):
    _name = 'basic.data.order.type'
    _description = 'Order Type'
    _rec_name = 'orderTypeName'

    orderTypeCode = fields.Char(
        string='OrderTypeCode', required=True)

    orderTypeName = fields.Char(
        string="OrderTypeName", required=True)

    orderTypeNameVN = fields.Char(
        string="OrderTypeNameVN", required=True)

    remarks = fields.Char(
        string="Remarks", required=False)


