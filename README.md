# python-network-socket-programming
Hands-on Python networking project demonstrating TCP client-server communication and UDP-based DNS simulation, focusing on socket programming and OSI Transport Layer concepts.

# TCP and UDP Socket Programming Using Python

## Project Overview

This project was developed as part of my Computer Networks studies to gain practical experience with socket programming and understand how TCP and UDP protocols work at the Transport Layer of the OSI model.

I created two client-server applications using Python:

1. **TCP Client-Server Application** – Demonstrates connection-oriented communication between a client and server.
2. **UDP-Based DNS Simulation** – Demonstrates connectionless communication by simulating DNS lookups using predefined records.

Both applications run locally using the loopback IP address `127.0.0.1`.

## 1. TCP Client-Server Application

### Objective

To understand how TCP establishes a connection between a client and server and allows data to be exchanged.

### How It Works

- The server creates a TCP socket and listens on port `12000`.
- The client connects to the server using the local IP address.
- The user enters a message through the client.
- The server receives the message, counts the characters and converts the message to uppercase.
- The server sends the processed message back to the client.
- The client displays the response, and the connection is closed.

### Example Output

**Client:**


Enter a message: Hello Network
Response from server: 13, HELLO NETWORK


**Concepts Practised**

- TCP socket creation using `SOCK_STREAM`
- IP addresses and port numbers
- Client-server connection establishment
- Sending and receiving data
- Encoding and decoding messages
- Closing socket connections

## 2. UDP-Based DNS Simulation

### Objective

To understand how UDP communication works and how DNS records can be used to map domain names to IP addresses.

### How It Works

- The UDP server stores predefined DNS A records and CNAME records.
- The client sends a hostname query to the server.
- The server searches its stored DNS records.
- If an A record is found, the server returns the associated IP address.
- If a CNAME record is found, the server identifies the canonical hostname and looks up its IP address.
- If the hostname does not exist in the stored records, the server returns a "DNS record not found" message.
- The client can send multiple queries without restarting the application.

### Example Output

**Client:**


DNS Client started

Enter hostname or alias: www.deakin.edu.au

DNS Response:
Record Type: CNAME
Alias: www.deakin.edu.au
Canonical Name: deakin.edu.au
IP Address: 192.168.1.20


**Concepts Practised**

- UDP socket creation using `SOCK_DGRAM`
- Connectionless communication
- Sending and receiving datagrams using `sendto()` and `recvfrom()`
- DNS A records and CNAME records
- Hostname lookup logic
- Handling unknown hostnames

**Note:** This is an educational DNS simulation using predefined records. It does not communicate with external DNS servers or implement the full DNS protocol.

## 3. TCP vs UDP Comparison

| Feature | TCP | UDP |

| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable delivery | Delivery not guaranteed |
| Data ordering | Maintains order | No ordering guarantee |
| Python socket type | `SOCK_STREAM` | `SOCK_DGRAM` |
| Application in this project | Text processing | DNS lookup simulation |

## 4. Technologies Used

- Python 3
- Python `socket` library
- TCP/IP networking
- UDP communication
- DNS concepts
- OSI Model – Transport Layer

## 5. How to Run the Project

### Requirements

- VS Code with python extensions installed


### TCP Application

Open two terminals.

**Terminal 1 – Start the server**


python TCP-Client-Server/server.py


**Terminal 2 – Start the client**


python TCP-Client-Server/client.py


Enter a message in the client terminal to see the server's response.

The TCP server processes one client connection and then closes. Restart the server before running another client session.

### UDP DNS Simulation

Open two terminals.

**Terminal 1 – Start the DNS server**


python UDP-DNS-Simulation/dns_server.py


**Terminal 2 – Start the DNS client**


python UDP-DNS-Simulation/dns_client.py


Try the following hostnames:


deakin.edu.au
www.deakin.edu.au
google.com
www.example.com
unknown.com


The DNS server continues listening for queries until stopped manually.

Both applications use localhost and port `12000`. Run only one server at a time to avoid confusion when testing.

## 6. What I Learned

Working on these applications helped me understand how networking concepts are implemented in code rather than only studying them in theory.

Through the TCP application, I practised creating sockets, establishing a connection and exchanging messages between a client and server.

Through the UDP DNS simulation, I learned how datagrams can be exchanged without establishing a connection and how A and CNAME records can be used in hostname resolution.

The project also helped me better understand the differences between TCP and UDP and their roles in network communication.


**Project Type:** Academic / Hands-on Networking Practice

**Focus:** Python Socket Programming, TCP/IP, UDP and DNS Fundamentals
