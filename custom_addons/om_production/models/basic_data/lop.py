from odoo import api, fields, models


class Lop(models.Model):
    _name = 'basic.data.lop'
    _description = 'LOP'

    facility = fields.Selection(
        string='Facility',
        selection=[('sip', 'SIP')])

    name = fields.Char(
        string='LOP')

    yearGold = fields.Char(
        string='YearGold')

    itemNoCasting = fields.Char(
        string='ItemNoCasting')

    inputWeight = fields.Char(
        string='InputWeight')

    metalType = fields.Char(
        string='MetalType')

    metalRate = fields.Char(
        string='MetalRate')

    rejectItemNumber = fields.Char(
        string='RejectItemNumber')

    itemMFTmp = fields.Char(
        string='ItemMFTmp')

    itemNoShooting = fields.Char(
        string='ItemNoShooting')

    itemNoReturnMetal = fields.Char(
        string='ItemNoReturnMetal')

    dustItemNo = fields.Char(
        string='DustItemNo')

    colorOfGold = fields.Many2one(
        'basic.data.color',
        string='ColorOfGold')
