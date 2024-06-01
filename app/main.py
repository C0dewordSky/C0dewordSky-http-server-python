import socket

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    # Server should run indefinitely
    while True:
        conn, _ = server_socket.accept()  # wait for client

        request = conn.recv(1024)
        decoded_request = request.decode("utf-8")
        path = decoded_request.split()[1]

        if  path.startswith("/"):
            response = (b"HTTP/1.1 200 OK\r\n\r\n")
        elif path.startswith("/echo/"):
            response_body = path[len("/echo/"):]
            response = (
                f"HTTP/1.1 200 OK\r\n"
                f"Content-Type: text/plain\r\n"  # Content-Type should be fixed to text/plain
                f"Content-Length: {len(response_body)}\r\n\r\n"
                f"{response_body}"
            ).encode("utf-8")
            conn.sendall(response)
        else:
            conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")
        
        conn.close()  # Close connection after handling request

# Ensure the server runs when the script is executed
if __name__ == "__main__":
    main()
