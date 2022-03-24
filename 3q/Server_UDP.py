import socket
import time

Message_F_Server = bytes("Hello UDP Cliente",'utf-8')

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind(('localhost', 27156))

print("Server is READY")

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    message = repr(message)[2:-1]

    #? Conditionals
    if message == "Me diga as horas":
        current_time = str(time.time())
        Message_F_Server = bytes(current_time, 'utf-8')
    elif message == "Em que anos estamos?":
        Message_F_Server = bytes("Estamos em 2022, o ano do Hexa", 'utf-8')
    elif message == "Encerrar":
        Message_F_Server = bytes("Encerrando conexão em breve", 'utf-8')
        pass
    else:
        print("Mensagem:", message)

    UDPServerSocket.sendto(Message_F_Server, address)
