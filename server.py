import socket
import time

# Server configuration
HOST = 'localhost'
PORT = 12345
MESSAGE = "Fall Detected"

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server is listening on {HOST}:{PORT}")

while True:
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Send message in a loop until "seen" is received or timeout
    while True:
        client_socket.sendall(MESSAGE.encode())

        # Set timeout for receiving acknowledgment
        client_socket.settimeout(5)

        try:
            data = client_socket.recv(1024).decode()
            if data == "seen":
                print("Acknowledgment received. Closing connection.")
                client_socket.close()
                break
        except socket.timeout:
            print("Timeout occurred. Resending message.")
            continue
client_socket.close()
server_socket.close()