from odoo import api, fields, models


class ProductionProcess(models.Model):
    _name = 'basic.data.production.process'
    _description = 'Production Process'
    _rec_name = 'productionProcessName'

    productionProcessCode = fields.Char(
        string='Production Process Code', required=True)

    productionProcessName = fields.Char(
        string='Production Process Name', required=True)

    siteName = fields.Many2one(
        'basic.data.sites',
        string='SiteName', required=True)
