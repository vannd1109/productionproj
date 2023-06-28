from odoo import api, fields, models


class ProductionStep(models.Model):
    _name = 'basic.data.production.step'
    _description = 'Production Step'

    stepCode = fields.Char(
        string='StepCode')

    name = fields.Char(
        string='StepDescription')

    generalSequence = fields.Char(
        string='GeneralSequence')
