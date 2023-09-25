import socket
# Client side
def client():
    #get hostname
    host =  socket.gethostname()
    port= 15000

    # Printing a message to indicate the client is attempting to connect to the server
    print(f"Connecting to server at {host}:{port}")

    client_socket = socket.socket() # defaault socket is SOCK_STREAM
    client_socket.connect((host, port))
    print(f"connected to server at {host}:{port}")

    message = input("->")

    while message.lower().strip !="bye":
        client_socket.send(message.encode())        
        data = client_socket.recv(1024)
        
        print("Server tells us", data)

        message = input("->")
    client_socket.close()

if __name__ == "__main__":
    client()