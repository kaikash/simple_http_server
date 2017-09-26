#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServerRequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    message = "Hello world!"
    status = 200
    if self.path == '/404':
      status = 404
      message = "not found"
    elif self.path == '/400':
      status = 400
      message = "bad reqeust"

    self.send_response(status)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write(bytes(message, "utf8"))
    return
 
def run():
  print('starting server...')
  server_address = ('127.0.0.1', 8080)
  httpd = HTTPServer(server_address, HTTPServerRequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()