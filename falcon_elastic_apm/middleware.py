# -*- coding: utf-8 -*-

import socket
import elasticapm
elasticapm.instrument()


class ElasticApmMiddleware(object):

    def __init__(self, service_name='falcon_apm', server_url='http://localhost:8200'):

        self.hostname = socket.gethostname()
        self.client = elasticapm.Client(
            service_name=service_name,
            server_url=server_url
        )

    def get_data_from_request(self, request):

        result = {
            "method": request.method,
            "remote_addr": request.remote_addr,
            "relative_uri": request.relative_uri,
            "forwarded_uri": request.forwarded_uri,
            "host": request.host,
            "app": request.app,
            "cookies": request.cookies,
            "headers": request.headers,
            "params": request.params,
            "url": request.url,
        }

        return result

    def process_request(self, req, resp):
        """
        req.stream corresponds to the WSGI wsgi.input environ variable,
        and allows you to read bytes from the request body.
        See also: PEP 3333
        """

        self.client.begin_transaction('web.falcon')

        context = {}
        context = self.get_data_from_request(req)
        context['hostname'] = self.hostname

        elasticapm.set_custom_context(context)

    def process_response(self, req, resp, resource, req_succeeded):

        self.client.end_transaction(req.relative_uri, 'success')
