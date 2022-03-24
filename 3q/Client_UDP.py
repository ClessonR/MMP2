import socket

Message_F_Client = bytes("Hello UDP Server", 'utf-8')
ServerAddressPort = ('localhost', 27156)
buffersize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)

message = bytes(input(),'utf-8')

while(repr(message)[2:-1] != "quit"):
    UDPClientSocket.sendto(message, ServerAddressPort)
    if repr(message)[2:-1] == "Me diga as horas":
        Message_F_Server = UDPClientSocket.recvfrom(buffersize)
        print(repr(Message_F_Server[0])[2:-1])
    elif repr(message)[2:-1] == "Em que ano estamos?":
        Message_F_Server = UDPClientSocket.recvfrom(buffersize)
        print(repr(Message_F_Server[0])[2:-1])
    elif message == "Encerrar":
        pass
    message = input()
    message = bytes(message, 'utf-8')
