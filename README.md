Simple Chat Application

**Overview**

This is a simple multi-client chat application using TCP socket programming in Python.
It follows a client–server architecture where single server accepts connections from multiple clients and broadcasts messages between them.

The application shows basic example of networking using socket communication, threads and a communication protocol.

**Project Structure**

chat-app/

│

├── server.py

├── client.py

├── README.md

└── Report.pdf

**Requirements**

Python 3.x
Standard Python libraries only (socket, threading)

No external networking libraries are used.

**How to Run the Application**

**Step 1**: Start the Server

python server.py
The server will start listening for incoming connections.

**Step 2**: Start the Client

Open another terminal and run:
python client.py
You will be prompted to enter a username.
Example:
Enter username: Alice

**Step 3:** Start Additional Clients

Open multiple terminals and run client.py again to simulate multiple users chatting simultaneously.

**Communication Protocol**

The application uses a simple text-based protocol for communication between client and server.

Commands

JOIN
Used when a client first connects to the server.

Example:
JOIN Alice

MSG
Used to send a chat message to other clients.

Example:
MSG Hello everyone

QUIT
Used when the client leaves the chat.

Example:
QUIT

**Features**

1. Multiple clients can connect simultaneously
2. Each user chooses a username
3. Messages are broadcast to all connected users
4. Notifications when users join or leave the chat
5. Real-time message communication
6. Thread-based concurrency for handling multiple clients

**Testing**

The application was tested using multiple client instances running in separate terminal windows.
Test cases included:
Multiple clients joining the chat
Client disconnection
Empty message handling
Server stability during multiple interactions

Name: Pallavi Maurya

Course: Computer Networks

Assignment: Simple Chat Application
