from odoo import api, fields, models

class Status(models.Model):
    _name = 'basic.data.status'
    _description = 'Status'
    _rec_name = 'statusName'

    statusCode = fields.Char(
        string='StatusCode', required=True)

    statusName = fields.Char(
        string="StatusName", required=True)

    statusNameVN = fields.Char(
        string="statusNameVN", required=True)

    remarks = fields.Text(
        string="Remarks", required=False)



