from odoo import api, fields, models

class Sites(models.Model):
    _name = 'basic.data.sites'
    _description = 'Sites'

    siteCode = fields.Char(
        string='SiteCode')

    name = fields.Char(
        string='SiteName')


