from odoo import api, fields, models, tools
import base64


class ViewBagSummaryByCustomer(models.Model):
    _name = 'report.view.bag.summary.by.customer'
    _description = 'View Bag Summary By Customer'

    sites = fields.Many2one(
        'basic.data.sites',
        string=' Sites')

    productionProcess = fields.Many2one(
        'basic.data.production.process',
        string='ProductionProcess')

    customerCode = fields.Many2one(
        'basic.data.customer',
        string='CustomerCode')

    generalSequence = fields.Selection(
        string='General Sequence',
        selection=[('first', '1'),
                   ('second', '2'),
                   ('third', '3'),
                   ('four', '4'),
                   ('five', '5'),
                   ('seven', '7'),
                   ('eight', '8'),
                   ('nine', '9'),
                   ('ten', '10'),
                   ('twelve', '12'),
                   ])

    stepName = fields.Many2one(
        comodel_name='basic.data.production.step',
        string='Step Name')

    totalQty = fields.Float(
        string='Total Quantity', digits=(12, 4))

    totalMetalWeight = fields.Float(
        string='Total Metal Weight', digits=(12, 4))
