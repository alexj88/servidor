import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_headers()
                self.wfile.write(b"<h1>Ola, mundo!</h1>")

        def do_POST(self):
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_headers()
                self.wfile.write(b"<h1>Requisicao POST recebida!</h1>")
                self.wfile.write(f"<p>Dados recebidos: {post_data.decode('utf-8')}</p>".encode('utf-8'))
with socketserver.TCPServer(("",PORT),MyHandler) as httpd:
    print(f"Servidor iniciado na porta {PORT}")
    httpd.server_forever()
