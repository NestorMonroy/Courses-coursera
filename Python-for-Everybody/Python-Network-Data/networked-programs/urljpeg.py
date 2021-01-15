"""
    Uno de los requisitos para utilizar el protocolo HTTP es la necesidad de enviar y recibir datos como objectos binarios, en vez de cadenas.
    encode() y decode() convierten cadenas en objectos binarios y viceversa

    la notación b'' se utiliza para especificar que una variable debe ser almacenada como un objeto binario. (encode() y b'' son equivalentes)

    Existe un buffer entre el servidor que hace las peticiones send()y nuestra aplicación que hace las peticiones recv(). 

    La detención de la aplicación que envía los datos o de la que los recibe se llama “control de flujo”.
"""

import socket
import time

SERVIDOR = 'data.pr4e.org'
PUERTO = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((SERVIDOR,PUERTO))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

contador = 0
imagen = b''


while True:
    datos = mysock.recv(5120)
    if len(datos) < 1 : break
    #time.sleep(0.25)
    contador = contador + len(datos)
    print(len(datos), contador)
    imagen = imagen + datos

mysock.close()

# Búsqueda del final de la cabecera (2 CRLF)

pos = imagen.find(b"\r\n\r\n")
print('Header length', pos)
#print(imagen)
print(imagen[:pos].decode())

#Ignora la cabecera y guarda los datos de la imagen

imagen = imagen[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(imagen)
fhand.close()

"""
    Al ejecutar el programa, se puede ver que no se obtienen 5120 caracteres cada vez que llamamos el método recv(). 
    Se obtienen tantos caracteres como hayan sido transferidos por el servidor web hacia nosotros a través de la red 
    en el momento dela llamada a recv(). En este ejemplo, se obtienen al menos 3200 caracteres cada vez que solicitamos 
    hasta 5120 caracteres de datos.

    Los resultados pueden variar dependiendo de tu velocidad de internet. Además, observa que en la última llamada a recv()
    obtenemos 3167 bytes, lo cual es el final de la cadena, y en la siguiente llamada a recv() obtenemos una cadena de longitud 
    cero que indica que el servidor ya ha llamado close() en su lado del socket, y por lo tanto no quedan más datos pendientes 
    por recibir
"""