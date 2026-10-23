import socket


A_RECORDS = {"deakin.edu.au": "192.168.1.10","google.com": "142.250.70.14","example.com": "192.168.1.20"}


CNAME_RECORDS = {"www.deakin.edu.au": "deakin.edu.au","www.example.com": "example.com"}


server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


server_address = ("127.0.0.1", 12000)


server_socket.bind(server_address)


print("DNS Server is running...")
print("Waiting for DNS queries...")


while True:

    data, client_address = server_socket.recvfrom(1024)

    hostname = data.decode().strip().lower()

    print("\nQuery received:", hostname)


    if hostname in A_RECORDS:

        ip_address = A_RECORDS[hostname]

        response = ("Record Type: A\n"f"Hostname: {hostname}\n" f"IP Address: {ip_address}" )


    elif hostname in CNAME_RECORDS:

        real_hostname = CNAME_RECORDS[hostname]

        if real_hostname in A_RECORDS:

            ip_address = A_RECORDS[real_hostname]

            response = ("Record Type: CNAME\n" f"Alias: {hostname}\n" f"Canonical Name: {real_hostname}\n" f"IP Address: {ip_address}")

        else:

            response = "CNAME found, but no A record exists."


    else:

        response = "DNS record not found."


    server_socket.sendto( response.encode(), client_address )

    print("Response sent.")