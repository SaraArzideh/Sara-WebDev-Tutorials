import socket
# Server side
def server():
    #get hostname
    host = socket.gethostname()
    port= 15000

    # Printing a message to indicate the server is running
    print(f"Server running on {host}:{port}")

    server_socket = socket.socket() # defaault socket is SOCK_STREAM
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5) #tuple
    print(f"Server listening on {host}:{port}")

    conn, address = server_socket.accept()
    print("Connection from address:", str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From user:", str(data))
        
        data= input("->")
        conn.send(data.encode())
    conn.close()
  

if __name__ == "__main__":
    server()