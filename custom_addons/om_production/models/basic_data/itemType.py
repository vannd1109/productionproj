from odoo import api, fields, models

class ItemType(models.Model):
    _name = 'basic.data.item.type'
    _description = 'Item Type'
    _rec_name = 'eTypeName'

    typeCode = fields.Char(
        string='TypeCode', required=True)

    typeName = fields.Char(
        string='TypeName', required=True)

    eTypeName = fields.Char(
        string='ETypeName', required=True)

    kindItem = fields.Many2one(
        'basic.data.kind.item',
        string='KindItem', required=True)

    remarks = fields.Char(
        string='Remarks', required=False)

    oldTypeCode = fields.Char(
        string='OldTypeCode', required=False)



