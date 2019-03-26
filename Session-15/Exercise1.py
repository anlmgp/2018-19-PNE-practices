import http.server
import socketserver
import termcolor

PORT = 4000

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        #-- printing the request line
        termcolor.cprint(self.requestline, 'green')
        print (self.path)

        f = open("form1.html", 'r')
        contents = f.read()
        self.path.lstrip('/echo?msg=')
        if self.path == '/echo' in range[0:4]:
            file = """<!DOCTYPE html>
            <html lang = "en">
            < head>
                <meta charset = "UTF-8">
                <title> Message </ title>
            </ head>
            <body style = "background-color: white;" >
              < h1 > Eco of the message recived < / h1 >
              < p > self.path.lstrip('/echo?msg=') < / p >
              < a href = "/" > Main page < / a >
            < / body >
            < / html >"""
            contents = content.write(file)
            content.close()


        else:
            f = open("form1.html", 'r')
            contents = f.read()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Lenght', len(str.encode(contents)))
        self.end_headers()

        #-- SEnding the body of the response message
        self.wfile.write(str.encode(contents))






# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is closed")