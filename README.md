# UDP_test_in_python
This code is UDP test source code written in python and it enable the server to communicate with client and send and visualize image, CSV and JSON files. Additionally, it can send a message to many clients simultaneously.
In this code, a UDP socket is created using socket.socket() with the socket.AF_INET and socket.SOCK_DGRAM parameters to establish a UDP connection. The sendto() method is used to send file data to the target client or multiple clients.

The send_file() function sends the file to a single client and calculates the end-to-end latency by recording the start and end times of the transmission. The visualize_file() function is a placeholder for visualizing the received file on the client side.

The broadcast_file() function allows broadcasting the file to multiple clients by iterating over the list of client IP addresses and sending the file data to each client.

Finally, in the main() function, the user is prompted for the file path, target IP address, and port number. The file is sent to the target client, and its latency is calculated. The file is then visualized on the client side. Additionally, the user is asked for the number of clients to broadcast the file, and their IP addresses are collected. The file is then broadcasted to those clients.

