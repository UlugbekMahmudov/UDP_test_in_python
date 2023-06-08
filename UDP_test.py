import socket
import os
import time

def send_file(ip, port, file_path):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Read the file and send it in chunks
    with open(file_path, "rb") as file:
        start_time = time.time()  # Record the start time
        data = file.read(1024)
        while data:
            client_socket.sendto(data, (ip, port))
            data = file.read(1024)
        end_time = time.time()  # Record the end time

    # Calculate the end-to-end latency
    latency = end_time - start_time
    print("End-to-End Latency:", latency, "seconds")

    # Close the socket
    client_socket.close()


def broadcast_file(ips, port, file_path):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Read the file and broadcast it to multiple clients
    with open(file_path, "rb") as file:
        data = file.read(1024)
        while data:
            for ip in ips:
                client_socket.sendto(data, (ip, port))
            data = file.read(1024)

    # Close the socket
    client_socket.close()

def main():
    # Get the file path, target IP address, and port number from the user
    file_path = input("Enter the file path: ")
    ip = input("Enter the target IP address: ")
    port = int(input("Enter the target port number: "))

    # Send the file to the target client and measure the end-to-end latency
    send_file(ip, port, file_path)



    # Get the IP addresses of multiple clients to broadcast the file
    num_clients = int(input("Enter the number of clients to broadcast the file: "))
    ips = []
    for i in range(num_clients):
        client_ip = input("Enter the IP address of client {}: ".format(i+1))
        ips.append(client_ip)

    # Broadcast the file to multiple clients
    broadcast_file(ips, port, file_path)

if __name__ == "__main__":
    main()
