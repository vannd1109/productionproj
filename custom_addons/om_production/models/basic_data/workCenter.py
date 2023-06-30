from odoo import api, fields, models

class WorkerCenter(models.Model):
    _name = 'basic.data.worker.center'
    _description = 'Worker Center'

    facility = fields.Many2many(
        'basic.data.sites',
        string=' Facility', required=True)

    wcCode = fields.Char(
        string='WcCode', required=True)

    wcName = fields.Char(
        string='WcName', required=True)
    
    stepCodeIN = fields.Char(
        string='StepCodeIN', required=True)

    stepCodeOUT = fields.Char(
        string='StepCodeOUT', required=True)

    stepCodeTransit = fields.Char(
        string='StepCodeTransit', required=True)

    statusWeight = fields.Char(
        string='StatusWeight', required=True)

    statusWeightJobIN = fields.Char(
        string='StatusWeightJobIN', required=True)

    statusWeightJobOUT = fields.Char(
        string='StatusWeightJobOut', required=True)

    preventMixing = fields.Char(
        string='PreventMixing', required=True)

    subProcess = fields.Char(
        string='SubProcess', required=True)

    origin = fields.Many2many(
        'basic.data.origin',
        string='Origin', required=True)

    dustInput = fields.Char(
        string='DustInput', required=True)

    stdProcess = fields.Char(
        string='StdProcess', required=True)

    perLimit = fields.Char(
        string='PerLimit', required=True)

    efficiency = fields.Char(
        string='Efficiency')

    showPic = fields.Char(
        string='ShowPic', required=True)

    workerTeam = fields.Many2one(
        'basic.data.worker.team',
        string='WorkerTeam', required=True)

    showStdProcess = fields.Char(
        string='ShowStdProcess', required=True)

    showRpt = fields.Char(
        string='ShowRpt', required=True)

    repair = fields.Char(
        string='Repair', required=True)

    repairWCCode = fields.Char(
        string='RepairWCCode', required=True)



