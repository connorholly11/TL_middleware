#not being used currently
# server.py
import http.server
import socketserver
import json

PORT = 8000

class OrderHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        print(f"Received POST request at {self.path}")
        if self.path == '/orders':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            order_data = json.loads(post_data)

            # Logging statement to track received order data
            print(f"Received order data: {order_data}")

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Order received"}).encode())
        else:
            self.send_error(404, 'Invalid endpoint')

    def do_GET(self):
        print(f"Received GET request at {self.path}")
        if self.path == '/orders':
            # Simulating a dummy response for GET requests
            dummy_response = {"orders": [{"symbol": "AAPL", "quantity": 100, "price": 150.0, "side": "buy"}]}

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dummy_response).encode())
        else:
            self.send_error(404, 'Invalid endpoint')

def run_server():
    with socketserver.TCPServer(("", PORT), OrderHandler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()