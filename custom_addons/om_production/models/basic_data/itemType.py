from odoo import api, fields, models

class ItemType(models.Model):
    _name = 'basic.data.item.type'
    _description = 'Item Type'

    typeCode = fields.Char(
        string='TypeCode',
        required=False)
    typeName = fields.Char(
        string='TypeName',
        required=False)
    name = fields.Char(
        string='ETypeName',
        required=False)
    kindItem = fields.Many2one('basic.data.kind.item', string='KindItem')
    remarks = fields.Char(
        string='Remarks',
        required=False)
    oldTypeCode = fields.Char(
        string='OldTypeCode',
        required=False)



