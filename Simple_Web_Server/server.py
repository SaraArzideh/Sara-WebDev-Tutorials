import socket
import os

# Function to handle incoming HTTP requests and generate responses
def handle_request(request):
    # Split the request into headers and extract the requested filename
    headers=request.split('\n')
    filename=headers[0].split()[1]

    if filename=="/":  # If the requested filename is "/", default to "/index.html"
        filename="/index.html"
    
    try:
        # Try to open and read the requested file from the "public" directory
        fin=open("public"+filename,"r")
        content=fin.read()
        fin.close()

        # Build a successful HTTP response with the file's content
        response="HTTP/1.0 200 ok\nContent-Type:text/html\n\n"+content
    except:
        # Handle the "file not found" error with a 404 response
        response="HTTP/1.0 404 NOT FOUND\nFile not found\n\n"
    return response

def main():
    # Print the current working directory
    print(os.getcwd())

    # Define the server's address and port
    SERVER_ADDRESS="127.0.0.1"
    SERVER_PORT= 8080

    # Create a socket and configure it to reuse the address if available
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the server's address aand port
    server_socket.bind((SERVER_ADDRESS,SERVER_PORT))
    server_socket.listen(1)

    # Print a message to indicate that server is listening
    print("Listening in port",SERVER_PORT)
    while True:
        # Accept incomming client connection
        conn,address = server_socket.accept()
        
        # Receive the client's http request and decode it
        request = conn.recv(1024).decode()
        print(request)

        if not request:
            continue

        # Handle the request and generate a response
        response = handle_request(request)

        # Send the response back to the client and close the connection
        conn.sendall(response.encode())
        
        conn.close()
        
     #server_socket.close()

if __name__ == "__main__":
	main()

