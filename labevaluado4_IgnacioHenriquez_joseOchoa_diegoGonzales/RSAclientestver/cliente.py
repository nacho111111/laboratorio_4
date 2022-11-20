
import random
from socket import *
import sys

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

def esPrimo(n):
	c=0
	x=2
	if n>=2:
		while x<=n/2:
			if n%x==0:
				c=c+1
				x=x+1
			else:
				x=x+1
		if c==0:
			return True
		else:
			return False
	else:
		return False

def mcd(e,FI):
	m=FI%e
	while m!=0:
		FI=e
		e=m
		m=FI%e
	return e

def calculae(FI):
	e=2
	le=[]
	while e>1 and e<FI : # valores que dan MCD = 1 se agregan a la lista
		if mcd(e,FI)==1:
			le.append(e)
			e=e+1
		else:
			e=e+1
	e = random.choice(le) # se toma cualquier valor de la lista 

	return e

def calculard(FI,e):
	k = 1
	t = (1+(k)*(FI))%(e)
	while t != 0:
		k=k+1
		t = (1+(k)*(FI))%(e)
	d = int((1+(k)*(FI))/(e))
	return d

## CIFRADO Y DESIFRADO
def cifrarmensaje(msj,key):
    msj=msj.upper()
    lm=msj.split(" ")
    cmc=""
    lmc=[]
    for i in lm:
        pal=cifrarpalabra(i,key)
        lmc.append(pal)
    for j in lmc:
        cmc=cmc+str(j)+" "
    return cmc

def cifrarpalabra(m,k):
    lpc=[]
    lp=[]
    n,e=k
    cpc=""
    for i in m:
        x=buscarpos(i)
        lp.append(x)
    for j in lp:
        c=(j**e)%n
        lpc.append(c)
    for k in lpc:
        cpc=cpc+str(k)+" "
    return cpc  
    

def buscarpos(x):
    alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    c=0
    for i in alf:
        if x==i:
            return c
        else:
            c=c+1   

  
##/ CIFRADO Y DESIFRADO
##/ FUNCIONES


nombre=input("\n Ingresa tu nombre: ")
p=int(input("Hola " + nombre +" ingresa 2 numeros primos: "))

q=int(input("El segundo: " ))

while esPrimo(p)==False:
	print("No es primo")
	p=int(input("Hola " + nombre +" ingresa 2 numeros primos: "))

while esPrimo(p)==False or p == q:
	print("No es primo o es igual a p")
	q=int(input("El segundo: " ))

n = p*q
print("\n     se calcula n")
print("\nn = p * q")
print("n = ",n," \n")

FI = (p-1) * (q-1)
print("     se calcula FI")
print("\nFI = (p-1) * (q-1)")
print("FI = ",FI," \n")

e = calculae(FI)

print("     se calcula e")
print("\n 1 < e < FI , MCD(e,FI) = 1")
print("e = ",e," \n")

d = calculard(FI,e)
print("     se calcula d")
print("\n d = [1+(x) * (FI)] / e")
print("d = ",d," \n")


m = leer_mensaje("mensajeentrada.txt")
print("Mensaje a cifrar", m)

publicKey = [n,e]
privateKey = [n,d]

msgCifrado = cifrarmensaje(m,publicKey)
msgCifrado = msgCifrado[:-1]
msgCifrado = msgCifrado[:-1]
# conexion cliente servidor 
IPServidor = "localhost"
puertoServidor = 9099

socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor,puertoServidor))

privateKey0 = str(privateKey[0])
privateKey1 = str(privateKey[1])
# enviar mensaje
socketCliente.send(msgCifrado.encode())
socketCliente.recv(4096).decode()
socketCliente.send(privateKey0.encode())
socketCliente.recv(4096).decode()
socketCliente.send(privateKey1.encode())
print("Mensaje enviado")
#cerrar socket
socketCliente.close()
sys.exit()