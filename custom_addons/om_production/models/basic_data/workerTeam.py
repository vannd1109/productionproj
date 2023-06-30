from odoo import api, fields, models

class WorkerTeam(models.Model):
    _name = 'basic.data.worker.team'
    _description = 'Worker Team'
    _rec_name = 'workerTeamName'

    facility = fields.Many2many(
        'basic.data.sites',
        string='Facility', required=True)

    workerTeamName = fields.Char(
        string='WorkerTeamName', required=True)

    workType = fields.Char(
        string='WorkType', required=True)

    shootingItem = fields.Char(
        string='ShootingItem', required=True)


