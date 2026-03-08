# Simple Chat Application

## Overview

This is a simple multi-client chat application using TCP socket programming in Python.  
It follows a client–server architecture where a single server accepts connections from multiple clients and broadcasts messages between them.

The application demonstrates basic networking concepts such as socket communication, threads, and a simple communication protocol.

---

## Project Structure

chat-app/

│

├── server.py

├── client.py

├── README.md

└── Report.pdf

---

## Requirements

- Python 3.x
- Standard Python libraries only (`socket`, `threading`)

No external networking libraries are used.

---

## How to Run the Application

### Step 1: Start the Server

Run the following command:


python server.py


The server will start listening for incoming connections.

---

### Step 2: Start the Client

Open another terminal and run:


python client.py


You will be prompted to enter a username.

Example:


Enter username: Alice


---

### Step 3: Start Additional Clients

Open multiple terminals and run `client.py` again to simulate multiple users chatting simultaneously.

---

## Communication Protocol

The application uses a simple text-based protocol for communication between the client and server.

### Commands

**JOIN**  
Used when a client first connects to the server.

Example:


JOIN Alice


**MSG**  
Used to send a chat message to other clients.

Example:


MSG Hello everyone


**QUIT**  
Used when the client leaves the chat.

Example:


QUIT


---

## Features

- Multiple clients can connect simultaneously
- Each user chooses a username
- Messages are broadcast to all connected users
- Notifications when users join or leave the chat
- Real-time message communication
- Thread-based concurrency for handling multiple clients

---

## Testing

The application was tested using multiple client instances running in separate terminal windows.

Test cases included:

- Multiple clients joining the chat
- Simultaneous messaging
- Client disconnection
- Empty message handling
- Server stability during multiple interactions

---

## Author

Name: Pallavi Maurya  
Course: Computer Networks  
Assignment: Simple Chat Application
