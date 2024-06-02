"""
import socket
import sys
import os

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    directory = sys.argv[2]
    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    # Server should run indefinitely
    while True:
        conn, _ = server_socket.accept()  # wait for client
    

        request = conn.recv(1024)
        decoded_request = request.decode("utf-8")
        path = decoded_request.split()[1]

        if  path.startswith("/echo/"):
            response_body = path[len("/echo/"):]
            # agent_response = path[len("User-Agent"):]
            response = (
                f"HTTP/1.1 200 OK\r\n"
                f"Content-Type: text/plain\r\n"  # Content-Type should be fixed to text/plain
                f"Content-Length: {len(response_body)}\r\n\r\n"
                f"{response_body}"
            ).encode()
            conn.sendall(response)
        elif path == "/":
            response = b"HTTP/1.1 200 OK\r\n\r\n"
            conn.sendall(response)
        elif path =="/user-agent":
            user_agent = get_header(decoded_request)
            if user_agent:
                response = (
                    f"HTTP/1.1 200 OK\r\n"
                    f"Content-Type: text/plain\r\n"
                    f"Content-Length: {len(user_agent)}\r\n\r\n"
                    f"{user_agent}"
                ).encode()
                conn.sendall(response)
            elif path.startswith("/files"):
                filename = path[7:]
                try:
                 with open(f"/{directory}/{filename}", "r") as f:
                    body = f.read()
                 response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(body)}\r\n\r\n{body}".encode()
                except Exception as e:
                  response = f"HTTP/1.1 404 Not Found\r\n\r\n".encode()
        else:
            response = b"HTTP/1.1 404 Not Found\r\n\r\n"
            conn.sendall(response)
        
        conn.close()  # Close connection after handling request

# Ensure the server runs when the script is executed

def get_header(request_str):
    lines = request_str.split("\r\n")
    for line in lines:
        if line.startswith("User-Agent:"):
            return line.split(":", 1)[1].strip()
    return None

if __name__ == "__main__":
    main()
"""

import socket
import threading
import sys

def main():
    def handle_req(client, addr):
        data = client.recv(1024).decode()
        req = data.split('\r\n')
        path = req[0].split(" ")[1]
        if path == "/":
            response = "HTTP/1.1 200 OK\r\n\r\n".encode()  
        elif path.startswith('/echo'):
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(path[6:])}\r\n\r\n{path[6:]}".encode()
        elif path.startswith("/user-agent"):
            user_agent = req[2].split(": ")[1]
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}".encode()
        elif path.startswith("/files"):
            directory = sys.argv[2]
            filename = path[7:]
            print(directory, filename)
            try:
                with open(f"/{directory}/{filename}", "r") as f:
                    body = f.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(body)}\r\n\r\n{body}".encode()
            except Exception as e:
                response = f"HTTP/1.1 404 Not Found\r\n\r\n".encode()
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
        client.send(response)
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:    
        client, addr = server_socket.accept()
        threading.Thread(target=handle_req, args=(client, addr)).start()
    

if __name__ == "__main__":
    main()