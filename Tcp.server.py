from socket import *

serverName = "127.0.0.1"
serverPort = 12000

# Create TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind server to IP address and port
serverSocket.bind((serverName, serverPort))

# Listen for client connection
serverSocket.listen(1)

print("TCP server is ready to receive")

# Accept client connection
connectionSocket, clientAddress = serverSocket.accept()

print("Client connected:", clientAddress)

# Receive message from client
message = connectionSocket.recv(2048).decode()

print("Message received:", message)

# Count characters
characterCount = len(message)

print("Number of characters:", characterCount)

# Convert message to uppercase
upperMessage = message.upper()

# Prepare response
response = f"{characterCount}, {upperMessage}"

# Send response to client
connectionSocket.send(response.encode())

connectionSocket.close()
serverSocket.close()

