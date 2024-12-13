import socket

ip_address = socket.gethostbyname('google.com') # Obtener la dirección IP de un dominio
ip_name = socket.gethostbyaddr('142.250.201.67') # Obtener el nombre del host a partir de una dirección IP

# Devuelve una tupla que incluye:
# (nombre canónico del host, lista de alias, lista de direcciones IP asociadas).
ex_address = socket.gethostbyname_ex('google.com')
fqdn = socket.getfqdn('google.com') # Obtener el nombre de dominio completamente calificado (FQDN)
port_number = socket.getservbyname('http') # Obtener el número de puerto por el nombre del servicio
port_number2 = socket.getservbyname('http', 'tcp') # Obtener el número de puerto para HTTP utilizando TCP
nombre_puerto = socket.getservbyport(25) # Obtener el nombre del servicio a partir de un número de puerto

print("gethostbyname: ",ip_address)
print("gethostbyaddr:", ip_name)
print("gethostbyname_ex:", ex_address)
print("fqdn: ",fqdn)
print("port number: ",port_number)
print("port number 2: ",port_number2)
print("port name: ", nombre_puerto)


pass