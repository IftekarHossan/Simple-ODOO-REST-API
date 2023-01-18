from odoo import http
import logging
_logger = logging.getLogger(__name__)

class AaaApiDevelopContacts(http.Controller):
    @http.route('/aaa/api/develop/contacts', auth='public', website=False, csrf=False, type='json', methods=['GET','POST'])
    def index(self, **kw):

        contacts = http.request.env['res.partner'].sudo().search([])
        contact_list =[]
        for contact in contacts:
            contact_list.append
            ({
                'name': contact.name,
                'email': contact.email,
                'phone': contact.phone,
                'contact': contact.phone,
            })
        return contact_list


class AaaApiDevelopPipeline(http.Controller):
    @http.route('/aaa/api/develop/pipeline', auth='public', website=False, csrf=False, type='json', methods=['GET','POST'])
    def index2(self, **kw):

        pipelines = http.request.env['crm.lead'].sudo().search([])
        pipeline_list =[]
        for pipeline in pipelines:
            pipeline_list.append
        ({
                'name': pipeline.name,
                'email': pipeline.email_from,
                'revenue': pipeline.expected_revenue,
         })
        return pipeline_list


class AaaApiDevelopCreate(http.Controller):
    @http.route('/aaa/api/develop/create', auth='public', website=False, csrf=False, type='json', methods=['GET','POST'])
    def index3(self, **kw):
        http.request.env['res.partner'].sudo().create({'name':kw['name']})

        return kw
