from http.server import SimpleHTTPRequestHandler, HTTPServer

Host = "127.0.0.1"
port = 8080

server = HTTPServer((Host, port), SimpleHTTPRequestHandler)

print(f"Iniciado servidor em {Host}:{port} !")
print(f"Versão do servidor - ({server.server_address})")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
    
print("\nEncerrando servidor")
server.server_close()