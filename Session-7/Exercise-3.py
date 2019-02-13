import socket
while True:

#Create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket created")
    PORT = 8080
    IP = "212.128.253.113"
    s.connect((IP, PORT))
    s.send(str.encode(input("Write a message:")))
    msg = s.recv(2048).decode('utf-8')
    print("MESSAGE FROM THE SERVICE")
    print(msg)


print("The end")