from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class InventoryRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = json.dumps({
            'name': 'Pants',
            'price': 50.00,
            'quantity': 10
        })
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-length', len(data))
        self.end_headers()
        self.wfile.write(data.encode())

def run():
    addr = ('', 44332)
    httpd = HTTPServer(addr, InventoryRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()