import socket
while True:

#Create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket created")
    PORT = 8888
    IP = "212.128.253.109"
    s.connect((IP, PORT))
    s.send(str.encode(input("Introduce the sequence:")))
    msg = s.recv(2048).decode('utf-8')
    print("MESSAGE FROM THE SERVICE")
    print(msg)
    s.close()

print("The end")