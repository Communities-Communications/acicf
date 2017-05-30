# -*- coding: utf-8 -*-
from odoo import http

# class Acicf(http.Controller):
#     @http.route('/acicf/acicf/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acicf/acicf/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('acicf.listing', {
#             'root': '/acicf/acicf',
#             'objects': http.request.env['acicf.acicf'].search([]),
#         })

#     @http.route('/acicf/acicf/objects/<model("acicf.acicf"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acicf.object', {
#             'object': obj
#         })