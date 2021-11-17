from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import conf.initialize
from app.urls import url_patterns

hostName = "127.0.0.1"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/favicon.ico':
            render = url_patterns[self.path]()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes(render, "utf-8"))


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
