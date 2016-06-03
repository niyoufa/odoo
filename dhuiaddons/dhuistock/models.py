# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Good(models.Model):
    _name = 'dhuistock.good'

    name = fields.Char()
    sku = fields.Char()

class Order(models.Model):
    _name = 'dhuistock.order'

    name = fields.Char()
    status = fields.Char