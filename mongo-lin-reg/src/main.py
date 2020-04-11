import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from handleSigterm import handleSigterm
from predictHousePrice import predictHousePrice

hostName = "0.0.0.0"
serverPort = int(os.environ['CONTAINER_PORT'])


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        prediction = predictHousePrice(sqFeet=1650, numOfBedrooms=3)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>mongo-lin-reg</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p>{prediction}</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    # Exit gracefully when Docker sends sigterm
    handleSigterm()

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        webServer.server_close()
        print("Server stopped.")
