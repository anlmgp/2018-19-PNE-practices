import socket

PORT = 8080
IP = "212.128.253.107"
MAX_OPEN_REQUEST = 5


def process_clinet(cs):
    msg = cs.recv(2048).decode("utf-8") # The opposite pass que need to decode (transform bites to string

    print("Mesage from the client: {}".format(msg))

    #Sending the mesague back to the clinet
    send = input(">")
    #(because we are echo server)
    cs.send(str.encode(send)) # Encode to sending ( a string no bites)

    cs.close()

# Cretae a sockey for connnecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST) # If there are more than 5 clients it should reject them.

print("Socket ready: {}".format(serversocket))

while True:

    print("Wating for connections at: {}, {}".format(IP, PORT))
    (clientsocket, adress) = serversocket.accept()

    process_clinet(clientsocket)

    #-- Process the clinet request
    print("Attending client: {}".format(adress))

