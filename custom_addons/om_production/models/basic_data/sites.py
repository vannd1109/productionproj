from odoo import api, fields, models

class Sites(models.Model):
    _name = 'basic.data.sites'
    _description = 'Sites'
    _rec_name = 'siteName'

    siteCode = fields.Char(
        string='SiteCode', required=True)

    siteName = fields.Char(
        string='SiteName', required=True)


