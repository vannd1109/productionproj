from odoo import api, fields, models

class KindItem(models.Model):
    _name = 'basic.data.kind.item'
    _description = 'Kind Item'
    _rec_name = 'kindItemCode'

    kindItemCode = fields.Char(
        string='KindItemCode', required=True)

    kindItemName = fields.Char(
        string="KindItemName", required=True)

    kindItemNameVN = fields.Char(
        string="KindItemNameVN", required=True)

    remarks = fields.Char(
        string="Remarks", required=False)


