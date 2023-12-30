import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = '/mnt/s3'

Handler = http.server.SimpleHTTPRequestHandler
os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()