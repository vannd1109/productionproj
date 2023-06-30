from odoo import api, fields, models

class Unit(models.Model):
    _name = 'basic.data.unit'
    _description = 'Unit'
    _rec_name = 'unitName'

    unitCode = fields.Char(
        string='UnitCode', required=True)

    unitName = fields.Char(
        string="UnitName", required=True)

    unitNameVN = fields.Char(
        string="UnitNameVN", required=True)

    remarks = fields.Text(
        string="Remarks", required=False)



