# server.py
import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections
import os
import json
import sys
 
PORT = 9000
 
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps([1,2,3]).encode())

    def do_POST(self):
        if self.path == '/terminal':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'application/json')
            # self.send_header('Content-Length', '100000')
            self.end_headers()


            os.system("whoami >> log.txt")
            # old_stdout = sys.stdout
            # log_file = open("message.log","w")
            # sys.stdout = log_file
            # sys.stdout = old_stdout
            # log_file.close()
            self.wfile.write(json.dumps({'status': True}).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps([1,2,3]).encode())


 
Handler = MyHttpRequestHandler
 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()