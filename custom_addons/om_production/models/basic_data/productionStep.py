from odoo import api, fields, models


class ProductionStep(models.Model):
    _name = 'basic.data.production.step'
    _description = 'Production Step'
    _rec_name = 'stepDescription'

    stepCode = fields.Char(
        string='StepCode', required=True)

    stepDescription = fields.Char(
        string='StepDescription', required=True)

    generalSequence = fields.Char(
        string='GeneralSequence', required=True)
