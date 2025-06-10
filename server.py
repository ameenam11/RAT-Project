import socket
import threading

def handle_client(client_socket):
    try:
        while True:
            # Receive command from server
            command = input("Enter command: ")
            if not command:
                continue
            
            # Send command to client
            client_socket.send(command.encode())
            
            if command.lower() == 'exit':
                break
                
            # Receive output from client
            output = client_socket.recv(4096).decode()
            print(f"Output:\n{output}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))  # Listen on all interfaces
    server.listen(5)
    print("[*] Server listening on port 9999")

    while True:
        client_sock, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        
        # Start client handler thread
        client_handler = threading.Thread(
            target=handle_client,
            args=(client_sock,)
        )
        client_handler.start()

if __name__ == "__main__":
    start_server()