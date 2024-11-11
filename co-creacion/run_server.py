import os
import http.server
import socketserver

PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Sirviendo en el puerto {PORT}. Accede a http://localhost:{PORT}")
    httpd.serve_forever()
