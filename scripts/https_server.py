#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

HOST = "0.0.0.0"
PORT = 443

httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Servidor HTTPS escuchando en https://{HOST}:{PORT}")
httpd.serve_forever()
