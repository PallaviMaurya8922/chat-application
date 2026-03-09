import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 12345))

username = input("Enter username: ")

client.send(("JOIN " + username).encode())

def send_message():
    while True:
        message = input("Type a message: ")

        if message == "/quit":
            client.send("QUIT".encode())
            client.close()
            print("You left the chat")
            break

        client.send(("MSG " + message).encode())

def receive_message():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\n" + message)
        except:
            break

thread1 = threading.Thread(target=send_message)
thread2 = threading.Thread(target=receive_message)

thread1.start()
thread2.start()