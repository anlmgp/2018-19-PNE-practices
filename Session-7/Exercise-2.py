# Programing our first client

import socket

#Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#The are different types of sockets in internet but we want one to comunicate with internet, amd we always use the final parameter

print ("Socket created")

PORT = 8080
IP = "212.128.253.64"

while True:
    s.connect((IP, PORT))

    s.send(str.encode(""))
    msg = s.recv(2048).decode('utf-8')
    print("MESSAGE FROM THE SERVICE")
    print(msg)


s.close()

print("The end")