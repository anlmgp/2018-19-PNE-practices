import socket
from Seq_analyzer import Seq


PORT = 8885

IP = socket.gethostbyname('DESKTOP-RM5P08K')
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    condition = True
    while condition:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg1 = clientsocket.recv(2048).decode("utf-8")
        msg2 = msg1.replace('\n', ' ')
        msg3 = msg1.split('\n')
        msg = Seq(msg3[0])
        print("> {}".format(msg1))

        letters = ('A', 'C','T', 'G')

        if msg2.startswith(" "):
            message = "ALIVE"
            send_bytes = str.encode(message)
            clientsocket.send(send_bytes)
            clientsocket.close()
            condition = False
        elif not msg2.startswith(letters):
            message = "ERROR"
            send_bytes = str.encode(message)
            clientsocket.send(send_bytes)
            clientsocket.close()
            condition = False
        else:
            message1 = "OK"
            message1 += '\n'
            for i in msg3[1:]:
                if i == 'len':
                    message1 =  message1 + str(msg.len())
                    message1 += '\n'
                elif i == 'complement':
                    message1 = message1 + str(msg.complement().strbases)
                    message1 += '\n'
                elif i == 'reverse':
                    message1 += str(msg.reverse().strbases)
                    message1 += '\n'
                elif i == 'countA':
                    message1 += str(msg.count1('A'))
                    message1 += '\n'
                elif i == 'countT':
                    message1 += str(msg.count1('T'))
                    message1 += '\n'
                elif i == 'countC':
                    message1 += str(msg.count1('C'))
                    message1 += '\n'
                elif i == 'countG':
                    message1 += str(msg.count1('G'))
                    message1 += '\n'
                elif i == 'percA':
                    message1 += str(msg.perc('A')) + '%'
                    message1 += '\n'
                elif i == 'percT':
                    message1 += str(msg.perc('T')) + '%'
                    message1 += '\n'
                elif i == 'percC':
                    message1 += str(msg.perc('C')) + '%'
                    message1 += '\n'
                elif i == 'percG':
                    message1 += str(msg.perc('G')) + '%'
                    message1 += '\n'

            send_bytes = str.encode(message1)
                 # We must write bytes, not a string
            clientsocket.send(send_bytes)


except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()