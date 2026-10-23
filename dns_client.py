import socket


client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


server_address = ("127.0.0.1", 12000)


print("DNS Client started")


while True:

    hostname = input("\nEnter hostname or alias: ")


    client_socket.sendto(hostname.encode(),server_address )


    data, server = client_socket.recvfrom(1024)


    response = data.decode()


    print("\nDNS Response:")
    print(response)


    choice = input("\nWould you like to make another DNS query? (y/n): " )


    if choice.lower() != "y":

        print("DNS Client closed.")
        break


client_socket.close()