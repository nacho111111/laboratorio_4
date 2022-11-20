
import random
from socket import *
import sys
import random
from math import pow

## FUNCIONES

def leer_mensaje(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    contador = 0
    while contador < len(lineas):
        lineas[contador] = lineas[contador].strip().split("    ")
        contador += 1
    mensaje = lineas[0][0]
    archivo.close()
    return mensaje
 
a = random.randint(2, 10)
 
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
 
# Generación de grandes números aleatorios
def gen_key(q):
 
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
 
    return key
 
# Exponenciación modular
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c
 
# Cifrado asimétrico
def encrypt(msg, q, h, g):
 
    en_msg = []
 
    k = gen_key(q)# Clave privada para el remitente
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])
 
    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
 
    return en_msg, p

##/ FUNCIONES
msg = leer_mensaje("mensajeentrada.txt")
print("Mensaje original :", msg)
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
key = gen_key(q)# Clave privada para el receptor
h = power(g, key, q)
print("g usada : ", g)
print("g^a usada : ", h)
en_msg, p = encrypt(msg, q, h, g)

# conexion cliente servidor 
IPServidor = "localhost"
puertoServidor = 9099

socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor,puertoServidor))
lEn = len(msg) 
lEn2 = lEn
p = str(p)
key = str(key)
q = str(q)
lEn = str(lEn)
socketCliente.send(lEn.encode())
socketCliente.recv(4096).decode()

for i in range(lEn2):
	en = str(en_msg[i])
	socketCliente.send(en.encode())
	socketCliente.recv(4096).decode()

# enviar mensaje
socketCliente.send(p.encode())
socketCliente.recv(4096).decode()
socketCliente.send(key.encode())
socketCliente.recv(4096).decode()
socketCliente.send(q.encode())
socketCliente.recv(4096).decode()
socketCliente.send(q.encode())
print("Mensaje enviado")
#cerrar socket
socketCliente.close()
sys.exit()