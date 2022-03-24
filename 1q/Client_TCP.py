import socket
from datetime import datetime, time
socket.setdefaulttimeout(15)
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.settimeout(15)
main_socket.connect(('localhost',24883))
msg = input()
timer = datetime.now()

while (msg !='quit' and ((datetime.now() - timer).seconds) <= 15):
    main_socket.sendall(bytes(msg,'utf-8'))
    data = main_socket.recv(1024)
    print('Received:', repr(data)[2:-1], "and the current time passed is {}".format((datetime.now() - timer).seconds))

    msg = input()

main_socket.close()