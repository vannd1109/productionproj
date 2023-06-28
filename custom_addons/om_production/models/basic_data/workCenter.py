from odoo import api, fields, models

class WorkerCenter(models.Model):
    _name = 'basic.data.worker.center'
    _description = 'Worker Center'

    facility = fields.Selection(
        string='Facility',
        selection=[('sip', 'SIP')])

    wcCode = fields.Char(
        string='WcCode')

    wcName = fields.Char(
        string='WcName')
    
    stepCodeIN = fields.Char(
        string='StepCodeIN')

    stepCodeOUT = fields.Char(
        string='StepCodeOUT')

    stepCodeTransit = fields.Char(
        string='StepCodeTransit')

    statusWeight = fields.Char(
        string='StatusWeight')

    statusWeightJobIN = fields.Char(
        string='StatusWeightJobIN')

    statusWeightJobOUT = fields.Char(
        string='StatusWeightJobOut')

    preventMixing = fields.Char(
        string='PreventMixing')

    subProcess = fields.Char(
        string='SubProcess')

    origin = fields.Char(
        string='Origin')

    dustInput = fields.Char(
        string='DustInput')

    stdProcess = fields.Char(
        string='StdProcess')

    perLimit = fields.Char(
        string='PerLimit')

    efficiency = fields.Char(
        string='Efficiency')

    showPic = fields.Char(
        string='ShowPic')

    workerTeam = fields.Many2one(
        'basic.data.worker.team',
        string='WorkerTeam')

    showStdProcess = fields.Char(
        string='ShowStdProcess')

    showRpt = fields.Char(
        string='ShowRpt')

    repair = fields.Char(
        string='Repair')

    repairWCCode = fields.Char(
        string='RepairWCCode')



