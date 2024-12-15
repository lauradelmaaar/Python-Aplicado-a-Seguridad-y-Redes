import socket

# Crear un socket del tipo TCP y vinvularlo a un puerto
# Utilizamos "localhos", por lo tanto solo aceptamos conexiones desde la misma máquina
# El puerto será 8080

print("hola funciono")
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#'localhost' indica que el servidor solo aceptará conexiones desde la misma máquina 
# (también podría usarse '0.0.0.0' para aceptar conexiones desde cualquier dirección).
my_socket.bind(('localhost',8080))
my_socket.listen(5)

while True:
    print("Esperando conexiones")
    (recv_socket,address) = my_socket.accept()
    print("petición HTTP recivida: ")
    # lee hasta 1024 bytes de datos enviados por el cliente (en este caso, la solicitud HTTP). Luego, los imprime en la consola.
    print(recv_socket.recv(1024))
    recv_socket.send(bytes("HTTP/1.1        200     OK\r\n\r\n<html><body><h1><Hello World!></h1></body></html>\r\n",'utf-8'))
    recv_socket.close()
    

