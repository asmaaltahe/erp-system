# -*- coding: utf-8 -*-
# from odoo import http


# class EducationErp(http.Controller):
#     @http.route('/education_erp/education_erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/education_erp/education_erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('education_erp.listing', {
#             'root': '/education_erp/education_erp',
#             'objects': http.request.env['education_erp.education_erp'].search([]),
#         })

#     @http.route('/education_erp/education_erp/objects/<model("education_erp.education_erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('education_erp.object', {
#             'object': obj
#         })
