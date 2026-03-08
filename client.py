import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 12345))

username = input("Enter username: ")

# send JOIN message
client.send(("JOIN " + username).encode())

def send_message():
    while True:
        message = input()

        if message == "/quit":
            client.send("QUIT".encode())
            break

        client.send(("MSG " + message).encode())


def receive_message():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

thread1 = threading.Thread(target=send_message)
thread2 = threading.Thread(target=receive_message)

thread1.start()
thread2.start()