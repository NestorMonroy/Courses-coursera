import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crear el socket, (crear un telefono)
mysock.connect(('data.pr4e.org', 80)) # (hacer una llamada, marcar al telefono)

cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() #telnet , enviar la conexion , enconde() lo convierte a unicode para poder ser leido por python UTF-8
mysock.send(cmd)

while True: 
    data = mysock.recv(512) #recuperar la informacion
    if len(data) < 1: break
    print(data.decode(), end='') # .decode() 


mysock.close() # cerrar el socket