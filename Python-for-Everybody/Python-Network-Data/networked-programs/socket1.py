"""
    El programa realiza una conexion al puerto 80 del servidor www.py4e.com
    ya que nuestro programa esta jugando el rol de "navegador web", el protocolo
    HTTP dice que debemos enviar el comando GET seguido de una linea en blanco.
    \r\n => representan un salto de linea (EOL)
    \r\n\r\n => significa que no hay nada entre dos secuencias de salto de linea, Eso es equivalente de una linea en blanco

    Una vez que enviamos esa linea en blanco, escribimos un bucle que recibe los datos desde el socket 
    en bloques de 512 caracteres y los imprime en la pantalla hasta que no quedan mas datos por leer la llamada 
    a recv() devuelve una cadena vacía

    encode() y decode() convierten cadenas en objectos binarios y viceversa
    
"""

import socket

misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
misock.send(cmd)

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end='')

misock.close()