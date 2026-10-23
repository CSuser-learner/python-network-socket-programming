from socket import *

serverName = "127.0.0.1"
serverPort = 12000

# Create TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server
clientSocket.connect((serverName, serverPort))

message = input("Enter a message: ")

# Send message to server
clientSocket.send(message.encode())

# Receive response from server
response = clientSocket.recv(2048).decode()

print("Response from server:", response)

clientSocket.close()

