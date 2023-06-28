from odoo import api, fields, models, tools
import base64


class ViewBag(models.Model):
    _name = 'report.view.bag'
    _description = 'View Bag'

    origin = fields.Many2one(
        'basic.data.origin',
        string='Origin')

    workCenter = fields.Char(
        string='WorkCenter')

    customer = fields.Many2one(
        'basic.data.customer',
        string=' Customer')

    kindItem = fields.Many2one('basic.data.kind.item', string='KindItem')

    customerCode = fields.Char(
        string='CustomerCode')

    name = fields.Char(
        string='BagNumber')

    itemNo = fields.Char(
        string='ItemNo')

    image = fields.Image(string="Image")

    drawingNo = fields.Char(
        string='DrawingNo')

    quantity = fields.Char(
        string='Quantity')

    weight = fields.Char(
        string='Weight')

    stoneWeight = fields.Char(
        string='StoneWeight')

    stoneWeightWS = fields.Char(
        string='StoneWeightWS')

    metalWeight = fields.Char(
        string='MetalWeight')

    finishDate = fields.Date(
        string='FinishData', options="{'format': 'DD/MM/YYYY'}")

    transDate = fields.Char(
        string='TransDate')

    diffDate = fields.Char(
        string='DiffDate')

    stepName = fields.Char(
        string='StepName')

    wcName = fields.Char(
        string='WcName')

    currentWorker = fields.Char(
        string='CurrentWorker')

    remark = fields.Char(
        string='Remark')

    orderID = fields.Char(
        string='OrderID')

    lop = fields.Many2one(
        'basic.data.lop',
        string='LOP')

    size = fields.Char(
        string='Size')

    typeCode = fields.Char(
        string='TypeCode')

    techGroup = fields.Char(
        string='TechGroup')

    orderType = fields.Many2one(
        'basic.data.order.type',
        string=' OrderType')

    lastPriority = fields.Char(
        string='LastPriority')

    lastDate = fields.Char(
        string='LastDate')

    lastUser = fields.Char(
        string='LastUser')

    sites = fields.Selection(
        string='Sites',
        selection=[('cn1', 'CN1'),
                   ('tsc', 'TSC'), ], )

    productionProcess = fields.Selection(
        string='Production Process',
        selection=[('tsx', 'TSX'),
                   ('cnnv', 'CNNV'),
                   ('nc', 'NC'),
                   ('sx1', 'SX1'),
                   ('sx2', 'SX2')])

    workerTeam = fields.Many2one(
        'basic.data.worker.team',
        string=' workerTeam')

    deliveryOrder = fields.Char(
        string='DeliveryOrder')

    view_bag_detail_id = fields.One2many('report.view.bag.detail', 'view_bag_id', string="View Bag Line")

    totalBags = fields.Char(
        string='TotalBags')

    dateFrom = fields.Date(
        string='DateFrom')

    # @api.model
    # def init(self):
    #     query = """SELECT * FROM basic_data_color"""
    #     self.env.cr.execute(query)
    #
    #     result = self.env.cr.fetchall()
    #     print(result)
    #     return

    def _set_image(self):
        for record in self:
            path = record.get_image_path()  #: image path in odoo folder structure, example: /odoo/images/<file>
            if not record.image:
                with open(path, 'rb') as img:
                    record.image = base64.b64encode(img.read())


class ViewBagDetail(models.Model):
    _name = "report.view.bag.detail"
    _description = "View Bag Detail"

    facility = fields.Selection(
        string='Facility',
        selection=[('sip', 'SIP')])
    bagNumber = fields.Many2one('report.view.bag')
    bagLine = fields.Char(
        string='BagLine')
    wcCode = fields.Char(
        string='WcCode')
    wcName = fields.Char(
        string='WcName')
    type = fields.Char(
        string='Type')
    currentID = fields.Char(
        string='CurrentID')
    workerIN = fields.Char(
        string='WorkerIN')
    workerOut = fields.Char(
        string='WorkerOut')
    forWorker = fields.Char(
        string='ForWorker')
    qty = fields.Char(
        string='Qty')
    dateIn = fields.Char(
        string='DateIn')
    dateOut = fields.Char(
        string='DateOut')
    weightIn = fields.Char(
        string='WeightIn')
    weightOut = fields.Char(
        string='WeightOut')
    stoneQty = fields.Char(
        string='StoneQty')
    stoneWeight = fields.Char(
        string='StoneWeight')
    rejectQty = fields.Char(
        string='RejectQty')
    rejectWeight = fields.Char(
        string='RejectWeight')
    dustWeight = fields.Char(
        string='DustWeight')
    dspStatus = fields.Char(
        string='DspStatus')
    stoneWeightWS = fields.Char(
        string='StoneWeightWS')
    stoneReject = fields.Char(
        string='StoneReject')
    sites = fields.Char(
        string='Sites')
    productionProcess = fields.Char(
        string='ProductionProcess')
    repairQty = fields.Char(
        string='RepairQty')
    repairRemark = fields.Char(
        string='RepairRemark')
    orderNumber = fields.Char(
        string='OrderNumber')
    name = fields.Char(
        string='Name')
    view_bag_id = fields.Many2one('report.view.bag', string='View Bag')
