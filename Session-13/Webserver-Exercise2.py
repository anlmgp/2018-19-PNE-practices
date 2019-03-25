import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8002


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            content = open("Index-Exercise1.html")
            contents = content.read()
            content.close()
        elif self.path == '/green.html':
            content = open("green.html")
            contents = content.read()
            content.close()
        elif self.path == '/blue.html':
            content = open("blue.html")
            contents = content.read()
            content.close()
        elif self.path == '/pink.html':
            content = open("pink.html")
            contents = content.read()
            content.close()
        else:
            content = open("error.html")
            contents = content.read()
            content.close()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html') #Be carefull we must change the type of text
        self.send_header('Content-Length', len(str.encode(contents)))
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")