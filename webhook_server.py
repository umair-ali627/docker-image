#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Webhook received\n".encode())
        subprocess.run(["/home/ubuntu/docker-image/deploy.sh"])

server = HTTPServer(('', 8088), WebhookHandler)
print("🌐 Listening on port 8088...")
server.serve_forever()

