from odoo import api, fields, models


class Lop(models.Model):
    _name = 'basic.data.lop'
    _description = 'LOP'
    _rec_name = 'lop'

    facility = fields.Many2many(
        'basic.data.sites',
        string='Facility', required=True)

    lop = fields.Char(
        string='LOP', required=True)

    yearGold = fields.Char(
        string='YearGold', required=True)

    itemNoCasting = fields.Char(
        string='ItemNoCasting', required=True)

    inputWeight = fields.Char(
        string='InputWeight', required=True)

    metalType = fields.Char(
        string='MetalType', required=True)

    metalRate = fields.Char(
        string='MetalRate', required=True)

    rejectItemNumber = fields.Char(
        string='RejectItemNumber', required=True)

    itemMFTmp = fields.Char(
        string='ItemMFTmp', required=True)

    itemNoShooting = fields.Char(
        string='ItemNoShooting', required=True)

    itemNoReturnMetal = fields.Char(
        string='ItemNoReturnMetal', required=True)

    dustItemNo = fields.Char(
        string='DustItemNo', required=True)

    colorOfGold = fields.Many2one(
        'basic.data.color',
        string='ColorOfGold', required=True)
