import socket
import threading

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost and port
server.bind(("127.0.0.1", 12345))

# Start listening
server.listen(10)
print("Server is listening...")

clients = []
usernames = {}

def broadcast(message):
    for client in clients:
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
                broadcast(broadcast_message)
            elif command == "QUIT":
                break
        except:
            break

    print(username + " left the chat")
    broadcast(username + " left the chat")
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
        broadcast(username + " joined the chat")
        thread = threading.Thread(target=receive_message, args=(client_socket,))
        thread.start()

accept_clients()