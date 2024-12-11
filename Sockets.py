import socket

import socket

# Obtener la dirección IP de un dominio
ip_address = socket.gethostbyname('google.com')
ip_name = socket.gethostbyaddr('142.250.201.67')
ex_address = socket.gethostbyname_ex('google.com')
fqdn = socket.getfqdn('google.com')
port_number = socket.getservbyname('http')
port_number2 = socket.getservbyname('http', 'tcp')
nombre_puerto = socket.getservbyport(25)

print("gethostbyname: ",ip_address)
print("gethostbyaddr:", ip_name)
print("gethostbyname_ex:", ex_address)
print("fqdn: ",fqdn)
print("port number: ",port_number)
print("port number 2: ",port_number2)
print("port name: ", nombre_puerto)




    






pass