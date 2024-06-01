# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, _ = server_socket.accept() # wait for client

    request = conn.recv(1024) 
  # if request.decode("utf-8").split()[1] == "/":
  #     conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n") 
  #  else:
  #      conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")
  #  conn.close"""
    
    if request.decode("utf-8").split()[1] == "/echo/":
        conn.sendall(f"HTTP/1.1 200 OK\r\nContent-Type: {str}\r\nContent-Length: {len(str)}\r\n\r\n{str}")
    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")    
    conn.close
    
if __name__ == "__main__":
    main()
