#!/usr/bin/env python
"""
HTTP Server to receive change stat in a cs go game
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import config
import json
import stats


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
        isCompet = False
        post_data = json.loads(post_data)
        for key, val in post_data.items():
            if key == 'map':
                for key_map, val_map in val.items():
                    if key_map == 'mode' and val_map == 'competitive':
                        isCompet = True
                    if key_map == 'phase' and val_map == 'gameover' and isCompet:
                        stats.ParserStat(post_data).write_in_file()
        self._set_headers()


def run(server_class=HTTPServer, handler_class=reqHandler):
    server_address = (config.Server['ip'], config.Server['port'])
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd on port = ', config.Server['port']
    httpd.serve_forever()


if __name__ == "__main__":

    run()