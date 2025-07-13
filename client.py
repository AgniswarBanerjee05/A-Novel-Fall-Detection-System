import socket
import time
import keyboard
import pyttsx3

# Server configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

while True:
    # Receive message from the server
    data = client_socket.recv(1024).decode()
    print(f"Received message from server: {data}")
    engine = pyttsx3.init()
    # Convert text to speec
    engine.say(data)
    # Run the engine to play the speech
    engine.runAndWait()
    # Send acknowledgment if message is received
    if data:
        keyboard.press_and_release('enter')
        ack = input("Type 'seen' to acknowledge: ")
        time.sleep(5)  # Wait for the delay
        keyboard.press_and_release('enter')  # Simulate pressing and releasing Enter key

        client_socket.sendall(ack.encode())
        if ack.lower() == 'seen':
            break

# Close the connection
client_socket.close()
