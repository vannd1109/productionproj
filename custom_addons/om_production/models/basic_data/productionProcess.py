from odoo import api, fields, models


class ProductionProcess(models.Model):
    _name = 'basic.data.production.process'
    _description = 'Production Process'

    productionProcessCode = fields.Char(
        string='Production Process Code')

    name = fields.Char(
        string='Production Process Name')

    siteName = fields.Many2one(
        'basic.data.sites',
        string='SiteName',
        required=True)
