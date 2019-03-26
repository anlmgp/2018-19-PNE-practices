import http.server
import socketserver
import termcolor

PORT = 4006

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        #-- printing the request line
        termcolor.cprint(self.requestline, 'green')
        print (self.path)

        message = self.path.lstrip('/echo?msg=')
        print (message)


        if self.path.rstrip(message) == '/echo?msg=':
            file = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Title</title>
                    </head>
                    <body>
                     <h1>Echo from received message</h1>
                      <p>{}</p>
                      <a href="/">Main page</a>
                    </body>
                    </html>""".format(message)

            self.send_response(200)

            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Lenght', len(str.encode(file)))
            self.end_headers()

        # -- SEnding the body of the response message
            self.wfile.write(str.encode(file))


        elif self.path == '/' or self.path == '/favicon.ico':
            f = open("form1.html", 'r')
            contents = f.read()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Lenght', len(str.encode(contents)))
            self.end_headers()

        #-- SEnding the body of the response message
            self.wfile.write(str.encode(contents))

        else:
            s = open("error.html")
            contents = s.read()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Lenght', len(str.encode(contents)))
            self.end_headers()
            # -- SEnding the body of the response message
            self.wfile.write(str.encode(contents))

# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is closed")