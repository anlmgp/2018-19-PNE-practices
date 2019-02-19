import socket
import termcolor

PORT = 8087
IP = "212.128.253.107"
MAX_OPEN_REQUEST = 5


def process_clinet(cs):
    msg = cs.recv(2048).decode("utf-8") # The opposite pass que need to decode (transform bites to string
    if msg == "EXIT":
        print ("The server finish")
        end = 'The server finish'
        cs.send(str.encode(end))
        cs.close()
        exit()
    elif msg != "EXIT":
        color1 = termcolor.colored(msg, "blue")
        color2 = termcolor.colored(msg, "green")
        print("Mesage from the client: {}".format(color1))

        #Sending the mesague back to the clinetThe server finish
        #(because we are echo server)
        cs.send(str.encode(color2))
        cs.close()

# Cretae a sockey for connnecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Wating for connections at: {}, {}".format(IP, PORT))
    (clientsocket, adress) = serversocket.accept()

    process_clinet(clientsocket)

    #-- Process the clinet request
    print("Attending client: {}".format(adress))