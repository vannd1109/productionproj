from odoo import api, fields, models
import base64
import os

from PIL import Image

class MaterItem(models.Model):
    _name = 'master.item'
    _description = 'MasterItem'

    facility = fields.Selection(
        string='Facility',
        selection=[('sip', 'SIP'), ],
        default='sip',
        required=False, )
    itemNo = fields.Char(
        string='Item No')
    drawingNo = fields.Char(
        string='Drawing No')
    itemName = fields.Char(
        string='Item Name',
        required=False)
    itemDesc = fields.Char(
        string='Item Desc',
        required=False)
    itemTypeCode = fields.Char(
        string='Item Type Code',
        required=False)
    itemTypeName = fields.Many2one(
        'basic.data.item.type',
        string='Item Type',
        required=False)
    kindItem = fields.Char(
        string='Kind Item',
        required=False)
    statusValue = fields.Char(
        string='Status Value',
        required=False)
    status = fields.Many2one(
        'basic.data.status',
        string='Status',
        required=False)
    unitValue = fields.Char(
        string='Unit Value',
        required=False)
    unit = fields.Many2one(
        'basic.data.unit',
        required=False)
    netWeight = fields.Char(
        string='Net Weight',
        required=False)
    collection = fields.Char(
        string='Collection',
        required=False)
    lastModifyDate = fields.Char(
        string='Last Modify Date',
        required=False)
    createdUser = fields.Char(
        string='Created User',
        required=False)
    lastModifyUser = fields.Char(
        string='Last Modify User',
        required=False)
    itemSize = fields.Char(
        string='Item Size',
        required=False)
    gamMe = fields.Char(
        string='Gamme',
        required=False)
    pathPictureString = fields.Char(
        string='Path Picture String',
        required=False)
    pathPicture = fields.Binary(string="Path Picture", store=True, attachment=False)
    note = fields.Char(
        string='Note',
        required=False)
    qualityCode = fields.Char(
        string='Quality',
        required=False)
    quality = fields.Many2one(
        'basic.data.quality',
        string='Quality',
        required=False)
    shapeCode = fields.Char(
        string='Shape',
        required=False)
    shape = fields.Many2one(
        'basic.data.shape',
        string='Shape',
        required=False)
    techGroup = fields.Char(
        string='Tech Group',
        required=False)
    lop = fields.Char(
        string='Lop',
        required=False)
    lacquerWeight = fields.Char(
        string='Lacquer Weight',
        required=False)
    designer = fields.Char(
        string='Designer',
        required=False)

    @api.onchange('itemTypeName')
    def onchange_type_code(self):
        self.itemTypeCode = self.itemTypeName.typeCode
        return

    @api.onchange('status')
    def onchange_status(self):
        self.statusValue = self.status.fieldCode
        return

    @api.onchange('unit')
    def onchange_unit(self):
        self.unitValue = self.unit.fieldCode
        return

    @api.onchange('quality')
    def onchange_quality(self):
        self.qualityCode = self.quality.fieldCode
        return

    @api.onchange('shape')
    def onchange_shape(self):
        self.shapeCode = self.shape.fieldCode
        return

    @api.onchange('pathPicture')
    def onchange_path_picture(self):
        # self.ensure_one()
        # data = base64.decodestring(self.pathPicture)
        # print(data)
        return
