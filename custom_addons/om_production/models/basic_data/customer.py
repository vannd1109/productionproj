from odoo import api, fields, models

class Customer(models.Model):
    _name = 'basic.data.customer'
    _description = 'Customer'
    _rec_name = 'customerCode'

    customerCode = fields.Char(
        string='CustomerCode', required=True)

    customerName = fields.Char(
        string='CustomerName', required=True)

    customerRegistration = fields.Char(
        string='CustomerRegistration', required=True)

    address = fields.Char(
        string='Address', required=True)

    phoneNumber = fields.Char(
        string='PhoneNumber', required=True)

    email = fields.Char(
        string='Email', required=True)



