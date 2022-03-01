# -*- coding: utf-8 -*-
# from odoo import http


# class Modu(http.Controller):
#     @http.route('/modu/modu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modu/modu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modu.listing', {
#             'root': '/modu/modu',
#             'objects': http.request.env['modu.modu'].search([]),
#         })

#     @http.route('/modu/modu/objects/<model("modu.modu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modu.object', {
#             'object': obj
#         })
