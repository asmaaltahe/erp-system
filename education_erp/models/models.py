# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class education_erp(models.Model):
#     _name = 'education_erp.education_erp'
#     _description = 'education_erp.education_erp'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
