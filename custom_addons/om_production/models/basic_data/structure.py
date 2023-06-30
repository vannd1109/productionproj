from odoo import api, fields, models

class Structure(models.Model):
    _name = 'basic.data.structure'
    _description = 'Structure'

    structureCode = fields.Char(
        string='StructureCode', required=True)

    structureName = fields.Char(
        string="StructureName", required=True)

    structureNameVN = fields.Char(
        string="structureNameVN", required=True)

    remarks = fields.Text(
        string="Remarks", required=False)



