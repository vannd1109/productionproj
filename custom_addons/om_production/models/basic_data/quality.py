from odoo import api, fields, models

class Quality(models.Model):
    _name = 'basic.data.quality'
    _description = 'Quality'
    _rec_name = 'qualityName'

    qualityCode = fields.Char(
        string='QualityCode', required=True)

    qualityName = fields.Char(
        string="QualityName", required=True)

    qualityNameVN = fields.Char(
        string="qualityNameVN", required=True)

    remarks = fields.Text(
        string="Remarks", required=False)



