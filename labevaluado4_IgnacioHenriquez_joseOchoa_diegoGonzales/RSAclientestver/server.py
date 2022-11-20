from socket import *

## Funsiones

def escribirArchivo(nombre_archivo,cifrado):
    archivo = open(nombre_archivo, "w")
    archivo.write(cifrado+"    "+"\n")
    archivo.close()

def descifrarmensaje(msj,key):
    msj=msj.upper()
    lm=msj.split("  ")
    cmc=""
    lmc=[]
    for i in lm:
        pal=descifrarnumero(i,key)
        lmc.append(pal)
    for j in lmc:
        cmc=cmc+str(j)+" "
    return cmc

def descifrarnumero(m,k):
    lnc=[]
    ln=[]
    n,d=k
    cnc=""
    men=m.split(" ")
    for i in men:
        x=int(i)
        ln.append(x)
    for j in ln:
        m=(j**d)%n
        lnc.append(m)
    for k in lnc:
        l=buscarlet(k)
        cnc=cnc+str(l)
    return cnc

def buscarlet(x):
    alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    c=0
    for i in alf:
        if x==c:
            return i
        else:
            c=c+1 
## Funciones

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
	msgCifrado = socketConexion.recv(4096).decode()
	socketConexion.send("recibido".encode())
	privateKey0 = socketConexion.recv(4096).decode()
	socketConexion.send("recibido".encode())
	privateKey1 = socketConexion.recv(4096).decode()

	privateKey0 = int(privateKey0)
	privateKey1 = int(privateKey1)
	privateKey=[privateKey0,privateKey1]
	msgDesifrado = descifrarmensaje(msgCifrado,privateKey)

	print("mensaje -->",msgDesifrado)
	escribirArchivo("mensajerecibido.txt",msgDesifrado)
	break

print("Desconectado el cliente", addr)
#cerrar conexion
socketConexion.close()