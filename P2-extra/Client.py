import socket
while True:

#Create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 8882
    IP = "212.128.253.109"
    s.connect((IP, PORT))
    s.send(str.encode(input("Introduce the sequence:")))
    msg = s.recv(2048).decode('utf-8')
    print("Message from the server")
    print("The complement of the sequence is: {}".format(msg))
    s.close()

print("The end")