import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 12345))

server.listen(10)
print("Server is listening...")

clients = []
usernames = {}

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message.encode())

def receive_message(client_socket):
    username = usernames[client_socket]
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            parts = message.split(" ", 1)
            command = parts[0]
            if command == "MSG":
                if len(parts) > 1:
                    text = parts[1]
                else:
                    text = ""
                broadcast_message = username + ": " + text
                print(broadcast_message)
                broadcast(broadcast_message, client_socket)
            elif command == "QUIT":
                broadcast(username +" left the chat", client_socket)
                break
        except:
            break

    clients.remove(client_socket)
    del usernames[client_socket]
    client_socket.close()


def accept_clients():

    while True:
        client_socket, address = server.accept()
        print("Connected to:", address)
        join_message = client_socket.recv(1024).decode()
        parts = join_message.split(" ", 1)
        if parts[0] == "JOIN":
            username = parts[1]
        clients.append(client_socket)
        usernames[client_socket] = username
        print(username + " joined the chat")
        broadcast(username + " joined the chat", client_socket)
        thread = threading.Thread(target=receive_message, args=(client_socket,))
        thread.start()

accept_clients()