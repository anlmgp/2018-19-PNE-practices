import socket
from Seq import Seq
while True:

#Create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 8889
    IP = "212.128.253.109"
    s.connect((IP, PORT))
    Sequence = Seq(input("Introduce the sequence:"))
    s.send(str.encode("The complement of the sequence:" + Sequence.complement().strbases + "    The reverse of the sequence:" + Sequence.reverse().strbases))
    msg = s.recv(2048).decode('utf-8')
    print(msg)
    s.close()
