#!/usr/bin/env python
"""
HTTP Server to receive change stat in a cs go game
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import config

class reqHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        if post_data['map']
        print post_data  # <-- Print post data
        self._set_headers()


def run(server_class=HTTPServer, handler_class=reqHandler):
    server_address = (config.Server['ip'], config.Server['port'])
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd on port = ', config.Server['port']
    httpd.serve_forever()


if __name__ == "__main__":

    run()