from odoo import api, fields, models

class Origin(models.Model):
    _name = 'basic.data.origin'
    _description = 'Origin'
    _rec_name = 'originName'

    originCode = fields.Char(
        string='OriginCode', required=True)

    originName = fields.Char(
        string="OriginName", required=True)

    originNameVN = fields.Char(
        string="originNameVN", required=True)

    remarks = fields.Char(
        string="Remarks", required=False)


