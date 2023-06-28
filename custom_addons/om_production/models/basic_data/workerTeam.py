from odoo import api, fields, models

class WorkerTeam(models.Model):
    _name = 'basic.data.worker.team'
    _description = 'Worker Team'

    facility = fields.Char(
        string='Facility')

    name = fields.Char(
        string='TeamName')

    workType = fields.Char(
        string='WorkType')

    shootingItem = fields.Char(
        string='ShootingItem')


