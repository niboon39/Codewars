import socket

def verify_password(target_password):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow reuse of the socket address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the port
    server_address = ('localhost', 65432)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Waiting for password attempts...")

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()
        try:
            # Print message when Script 1 connects to Script 2
            print(f"Connection established with {client_address}")

            # Receive the password attempt
            while True:
                data = connection.recv(1024)
                if data:
                    password_attempt = data.decode('utf-8')
                    if password_attempt == target_password:
                        connection.sendall(b"True")
                        print(f"Password verification successful: {password_attempt}")
                        return
                    else:
                        connection.sendall(b"False")
                else:
                    break
        finally:
            # Clean up the connection
            connection.close()
            print(f"Connection with {client_address} closed.")

def main():
    # Target password to verify
    target_password = "123"  # You can change this to any password you want to verify
    verify_password(target_password)

if __name__ == "__main__":
    main()
