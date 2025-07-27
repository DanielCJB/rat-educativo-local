import socket

#crea el sever socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#dirección de servidor y puerto (localhost)
host: '127.0.0.1'
port: 4444

#asociar el bind (socket) al puerto
server_socket.bind((host, port))

#escuchar conexiones entrantes, un cliente a la vez?
server_socket.listen(1)
print(f"Esperando conexión en {host}:{port}...")

#aceptar una conexión entrante
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con {client_address}")

#