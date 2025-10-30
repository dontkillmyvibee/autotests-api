import socket

messages = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(10)

while True:
    client_socket, client_address = server.accept()
    print(f"Пользователь с адресом: {client_address} подключился к серверу")

    data = client_socket.recv(1024)
    message = data.decode()
    print(f"Пользователь с адресом: {client_address} отправил сообщение: {message}")
    messages.append(message)
    client_socket.send('\n'.join(messages).encode())

    client_socket.close()
