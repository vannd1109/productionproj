from odoo import api, fields, models


class FollowCustomerOrder(models.Model):
    _name = 'follow.customer.order'
    _description = 'Follow Customer Order'

    drawingNo = fields.Char(
        string='DrawingNo')
    qty = fields.Char(
        string="Qty",
        required=False)
    remarks = fields.Char(
        string="Remarks",
        required=False)
    remarks1 = fields.Char(
        string="Remarks1",
        required=False)
    weight1Pcs = fields.Char(
        string="Weight1Pcs",
        required=False)
    totalWeight = fields.Char(
        string="TotalWeight",
        required=False)

    customerCode = fields.Many2one('basic.data.customer', string='CustomerCode')


    def action_test(self):
        print("Button CLicked!!!!")

