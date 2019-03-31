import http.server
import socketserver
import termcolor
from Seq_analyzer import Seq

PORT = 4003

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        #-- printing the request line
        termcolor.cprint(self.requestline, 'green')
        print (self.path)

        message = self.path.replace('/myserver?msg=', '').replace('&len=on', '')
        message1 = message.replace ('&operation=count', '').replace('&operation=perc','')
        message2 = message1.replace('&base=A','').replace('&base=T','').replace('&base=G','').replace('&base=G','')
        print (message2)
        letters = ('A', 'C','T','G')

        path = self.path

        if path.startswith('/myserver?msg='):
            message2 = message2.upper()
            conditon = True
            while conditon == True:
                for i in message2:
                    if i in letters:
                        conditon = True
                        pass
                    else:
                        file1 = """<!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <title>Title</title>
                                </head>
                                <body>
                                  <h1> Not correct sequence</h1>
                                  <p>Sorry you must introduce a sequence that contains [A,C,T,G]</p>
                                  <a href="/">Main page</a>
                                </body>
                                </html>"""

                        self.send_response(200)
                        self.send_header('Content-Type', 'text/html')
                        self.send_header('Content-Lenght', len(str.encode(file1)))
                        self.end_headers()
                        # -- SEnding the body of the response message
                        self.wfile.write(str.encode(file1))
                        conditon = False
                        break

                if conditon == True:
                    if 'len' in path:
                        if 'count' in path:
                            letter = message1[-1]
                            msg = Seq(message2)
                            file = """<!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="UTF-8">
                                        <title>RESULT</title>
                                    </head>
                                    <body>
                                      <h1>Analysis of dna</h1>
                                      <p>Sequence: {}</p>
                                      <p>Len: {} </p>
                                      <p> Operation count on the {} base: {} </p>
                                      <a href="/">Main page</a>
                                    </body>
                                    </html>""".format(message2, msg.len(),letter, msg.count1(letter))
                            file = str(file)

                            self.send_response(200)
                            self.send_header('Content-Type', 'text/html')
                            self.send_header('Content-Lenght', len(str.encode(file)))
                            self.end_headers()
                            # -- SEnding the body of the response message
                            self.wfile.write(str.encode(file))
                            conditon = False

                        elif 'perc' in path :
                            letter = message1[-1]
                            msg = Seq(message2)
                            file = """<!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="UTF-8">
                                        <title>RESULT</title>
                                    </head>
                                    <body>
                                      <h1>Analysis of dna</h1>
                                      <p>Sequence: {}</p>
                                      <p>Len: {} </p>
                                      <p> Operation percentage on the {} base: {} </p>
                                      <a href="/">Main page</a>
                                    </body>
                                    </html>""".format(message2, msg.len(),letter, str(msg.perc(letter))+ '%')
                            file = str(file)

                            self.send_response(200)
                            self.send_header('Content-Type', 'text/html')
                            self.send_header('Content-Lenght', len(str.encode(file)))
                            self.end_headers()
                            # -- SEnding the body of the response message
                            self.wfile.write(str.encode(file))
                            conditon = False
                    else:
                        if 'count' in path:
                            letter = message1[-1]
                            msg = Seq(message2)
                            file = """<!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="UTF-8">
                                        <title>RESULT</title>
                                    </head>
                                    <body>
                                      <h1>Analysis of dna</h1>
                                      <p>Sequence: {}</p>
                                      <p> Operation count on the {} base: {} </p>
                                      <a href="/">Main page</a>
                                    </body>
                                    </html>""".format(message2,letter, msg.count1(letter))
                            file = str(file)

                            self.send_response(200)
                            self.send_header('Content-Type', 'text/html')
                            self.send_header('Content-Lenght', len(str.encode(file)))
                            self.end_headers()
                            # -- SEnding the body of the response message
                            self.wfile.write(str.encode(file))
                            conditon = False

                        elif 'perc' in path :
                            letter = message1[-1]
                            msg = Seq(message2)
                            file = """<!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="UTF-8">
                                        <title>RESULT</title>
                                    </head>
                                    <body>
                                      <h1>Analysis of dna</h1>
                                      <p>Sequence: {}</p>
                                      <p> Operation percentage on the {} base: {} </p>
                                      <a href="/">Main page</a>
                                    </body>
                                    </html>""".format(message2,letter, str(msg.perc(letter))+ '%')
                            file = str(file)

                            self.send_response(200)
                            self.send_header('Content-Type', 'text/html')
                            self.send_header('Content-Lenght', len(str.encode(file)))
                            self.end_headers()
                            # -- SEnding the body of the response message
                            self.wfile.write(str.encode(file))
                            conditon = False

        elif self.path == '/' or self.path == '/favicon.ico':
            f = open("form.html", 'r')
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
