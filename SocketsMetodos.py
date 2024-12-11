import socket
from socket import gethostbyname, gethostbyaddr
import sys
import optparse
from threading import Thread


# Primer script: Obtención de información de DNS
def script_1():
    try:
        print("gethostbyname_ex:", socket.gethostbyname_ex('www.google.es'))
        print("gethostbyaddr:", socket.gethostbyaddr('142.250.200.99'))
        print("getfqdn:", socket.getfqdn('www.google.es'))
        
    except socket.error as error:
        print(f"Error de conexión: {error}")
        sys.exit(1)  # Salir con código de error

# Segundo script: Resolución de una IP específica (8.8.8.8)
def script_2():
    try:
        result = socket.gethostbyaddr("8.8.8.8")
        print(f"The host name is: {result[0]}")
        print("Address:")
        for item in result[2]:
            print(f" {item}")
        
    except socket.herror as e:
        print("Error al resolver la dirección IP:", e)
        
def escanerPuertos():
    ip='172.24.45.55'
    portlist = [22,23,80,912,135,445,20,631]
    try:
        for port in portlist:
            mySock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result=mySock.connect_ex((ip,port))
            print(port, ":", result)
            mySock.close
    except socket.error as error:
        print(f"Error: {str(error)}")
        print("Error de conexion")
        
def escanearPuertosDominio(dominio, puertosUsuario):
    # Convertir la lista de puertos de string a lista de enteros
    puertos_lista = [int(port) for port in puertosUsuario.split(",")]

    # Imprimir la IP y la lista de puertos seleccionados
    print(f"Escaneando la IP: {dominio} con los puertos: {puertos_lista}")

    try:
        # Iterar sobre cada puerto de la lista
        for port in puertos_lista:
            mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mySock.settimeout(5)  # Limita el tiempo de espera por conexión

            result = mySock.connect_ex((dominio, port))  # Intentar la conexión con el puerto

            # Verificar si la conexión fue exitosa
            if result == 0:
                print(f"Puerto {port}: ABIERTO")
            else:
                print(f"Puerto {port}: CERRADO")
            
            mySock.close()  # Cerrar el socket después de la prueba

    except socket.error as error:
        print(f"Error: {str(error)}")
        print("Error de conexión")

def escanearPuertosIP(ipUsuario, puertoInicio, puertoFin):

    # Imprimir la IP y la lista de puertos seleccionados
    print(f"Escaneando la IP: {ipUsuario} desde el puerto {puertoInicio} hasta el puerto {puertoFin}")

    try:
        for port in range(int(puertoInicio),int(puertoFin)+1):
            print(f"Probando puerto {port}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            
            if(s.connect_ex((ipUsuario,port))==0):
                print(f"El puerto {port} está ABIERTO")
                
            """else:
                print(f"El puerto {port} está CERRADO")"""
            s.close()
            

    except socket.error as error:
        print(f"Error: {str(error)}")
        print("Error de conexión")
        
    
def socketScan(host,port):
    try:
        socketConnect = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crea un socket para conexiones TCP
        socketConnect.settimeout(20) 
        socketConnect.connect((host, port)) # Intenta conectarse al host en el puerto especificado. Si la conexión es exitosa, significa que el puerto está abierto.
        print(f'[+] {port}/tcp open')
    except Exception as error: 
        print(error)
        print(f'[-] {port}/tcp closed')
        
    finally:
        socketConnect.close()
        

def portScanning(host, ports):
    try:
        # Obtener la dirección IP del host proporcionado
        ip = gethostbyname(host)

    except:
        print(f"[-] cannot resolve '{host}': Unknown host")
        return
    
    try:
        # Intentar obtener el nombre del host a partir de la IP
        name = gethostbyaddr(ip)
        print(f"\n[+] Scan results for: {name[0]}")
    except:
        # Si no se puede obtener el nombre, mostrar la dirección IP
        print(f"\n[+] Scan Results for: {ip}")
    
    # Lista para almacenar los hilos
    threads = []
    
    for port in ports:
        try:
            # Crear y agregar un hilo para cada puerto
            t = Thread(target=socketScan, args=(ip, int(port)))
            threads.append(t)
            t.start()
        except ValueError:
            # Manejar puertos no válidos
            print(f"Invalid port: {port}")
    
    # Esperar a que todos los hilos terminen
    for t in threads:
        t.join()


        
        
        
# Bloque principal: Ejecutar uno u otro script según el caso
if __name__ == "__main__":
    print("Elige el script que deseas ejecutar:")
    print("1: Información de DNS para google.com")
    print("2: Resolución de IP para 8.8.8.8")
    print("3: Escaner de puertos")
    print("4: Escaner de puertos dado un dominio y una lista de peurtos")
    print("5: Escaner de puertos dado una dirección IP, un puerto de inicio y un puerto fin")
    print("6: Escaneo de un único puerto en un host")
    print("7: Escaneo de múltiples puertos en un host")

    
    choice = input("Introduce el número del script: ").strip()
    
    if choice == "1":
        script_1()
    elif choice == "2":
        script_2()    
    elif choice == "3":
        escanerPuertos()
    elif choice == "4":
        ip_usuario = input("Introduce el nombre de dominio (ej. www.google.com): ")
        puertos_usuario = input("Introduce la lista de puertos separados por comas (ej. 22,80,443): ")
        escanearPuertosDominio(ip_usuario, puertos_usuario)  # Llamada a la función escanearPuertosDominio
    elif choice == "5":
        ip_usuario = input("Introduce dirección ip separada por puntos (ej. 172.24.45.55): ")
        puertoInicio = input("Introduce el puerto de inicio (ej. 22): ")
        puertoFin = input("Introduce el puerto de Fin: ")
       
        escanearPuertosIP(ip_usuario, puertoInicio, puertoFin)  
        
    elif choice == "6":
        # Nuevo script para escaneo de un único puerto
        host = input("Introduce el host o dirección IP (ej. www.google.com o 127.0.0.1): ")
        puerto = int(input("Introduce el puerto a escanear (ej. 80): "))
        socketScan(host, puerto)  # Llamada a la función socketScan
        
    elif choice == "7":
        host = input("Introduce el host o dirección IP (ej. www.google.com): ")
        puertos_usuario = input("Introduce la lista de puertos separados por comas (ej. 22,80,443): ")
        puertos = [int(port.strip()) for port in puertos_usuario.split(",") if port.strip().isdigit()]
        portScanning(host, puertos)
    
        
    else:
        print("Opción no válida.")
        sys.exit(1)

