from odoo import api, fields, models

class Customer(models.Model):
    _name = 'basic.data.customer'
    _description = 'Customer'

    name = fields.Char(
        string='CustomerCode',
        required=False)
    customerName = fields.Char(
        string='CustomerName',
        required=False)
    customerRegistration = fields.Char(
        string='CustomerRegistration',
        required=False)
    address = fields.Char(
        string='Address',
        required=False)
    phoneNumber = fields.Char(
        string='PhoneNumber',
        required=False)
    email = fields.Char(
        string='Email',
        required=False)



