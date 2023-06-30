from odoo import api, fields, models

class TechGroup(models.Model):
    _name = 'basic.data.tech.group'
    _description = 'TechGroup'

    techGroupCode = fields.Char(
        string='TechGroupCode', required=True)

    techGroupName = fields.Char(
        string="TechGroupName", required=True)

    techGroupNameVN = fields.Char(
        string="TechGroupNameVN", required=True)

    remarks = fields.Text(
        string="Remarks", required=False)



