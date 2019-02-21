import socket

IP = "212.128.253.95"
PORT = 8884

while True:

    # Before connecting to the server, ask the user for the string
    msg = input("> ")
    if len(msg) == 0:
        msg = " "


    # Now we can create the socket and connect to the servewr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()