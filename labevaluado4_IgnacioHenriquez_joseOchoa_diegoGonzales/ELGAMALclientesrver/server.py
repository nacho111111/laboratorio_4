from socket import *
import random
from math import pow

## FUNCIONES
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

def decrypt(en_msg, p, key, q):
 
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))

    return dr_msg

## /FUNCIONES
def escribirArchivo(nombre_archivo,cifrado):
    archivo = open(nombre_archivo, "w")
    archivo.write(cifrado+"    "+"\n")
    archivo.close()


print("Esperando a un cliente :)")

# conexion cliente servidor
direccionServidor = "localhost"
PuertoServidor = 9099

#generar sockets
socketServidor = socket(AF_INET, SOCK_STREAM)
#establecer conexion

socketServidor.bind( ( direccionServidor, PuertoServidor ) )
socketServidor.listen()

while True:
	#establecer conexion
    socketConexion, addr = socketServidor.accept()
    print("conectado con un cliente", addr)

    lEn = socketConexion.recv(4096).decode()
    socketConexion.send("recibido".encode())
    en_msg = []
    lEn = int(lEn)
    for i in range(lEn):
        en = socketConexion.recv(4096).decode()
        en = int(en)
        en_msg.append(en)
        socketConexion.send("recibido".encode())
    p = socketConexion.recv(4096).decode()
    socketConexion.send("recibido".encode())
    key = socketConexion.recv(4096).decode()
    socketConexion.send("recibido".encode())
    q = socketConexion.recv(4096).decode()

    p = int(p)
    key = int(key)
    q = int(q)

    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)

    print("Mensaje descifrado :", dmsg);

    escribirArchivo("mensajerecibido.txt",dmsg)
    break

print("Desconectado el cliente", addr)
#cerrar conexion
socketConexion.close()