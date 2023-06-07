from odoo import api, fields, models

class TechGroup(models.Model):
    _name = 'basic.data.tech.group'
    _description = 'TechGroup'

    fieldCode = fields.Char(
        string='FieldCode')
    fieldValue = fields.Text(
        string="FieldValue",
        required=False)
    fieldValueVN = fields.Text(
        string="FieldValueVN",
        required=False)
    remarks = fields.Text(
        string="Remarks",
        required=False)


