import socket


def StartSaladServer():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 54140

    server_socket.bind((host, port))

    server_socket.listen(5)

    return server_socket

def SaladInvade(server_socket):
        print("Waiting for connection")
        client_socket, addr = server_socket.accept()
        if client_socket:
            print("Connected!")
            return client_socket

def SaladSend(client_socket, string):
    print(f"Sending {string.encode()}")
    client_socket.send(string.encode())
    print("Sent")

def SaladCloseClient(client_socket):
    client_socket.close()

def SaladCloseServer(server_socket):
    server_socket.close()