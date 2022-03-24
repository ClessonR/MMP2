import socket
from datetime import datetime, time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.bind(('localhost', 38447))
main_socket.listen(1)
conn, addr = main_socket.accept()
print("Server connected with: {} {}".format(addr[0], addr[1]))
timer = datetime.now()

while (1):
    data = conn.recv(1024)
    if not data or ((datetime.now() - timer).seconds >= 15):
        break
    conn.sendall(data)

conn.close()
