from odoo import api, fields, models

class Shape(models.Model):
    _name = 'basic.data.shape'
    _description = 'Shape'
    _rec_name = 'shapeName'

    shapeCode = fields.Char(
        string='ShapeCode', required=True)

    shapeName = fields.Char(
        string="ShapeName",required=True)

    shapeNameVN = fields.Char(
        string="ShapeNameVN",required=True)

    remarks = fields.Text(
        string="Remarks", required=False)



