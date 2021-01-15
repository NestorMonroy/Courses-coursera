
"""
    Los corchetes se usan para indicar un conjunto de caracteres que
    queremos aceptar como coincidencias. 
    La secuencia \S retornara el conjunto de caracteres que sea un espacio en blanco

    [a-zA-Z0-9]\S*@\S*[a-zA-Z] 
    Subcadenas que comiencen con una letra en minuscula, una letra mayuscula o numero [a-zA-Z0-9] 
    seguida de 0 o mas caracteres que no sean espacios en blanco (\S*), seguidos de un signo @, 
    seguido de cero o mas caracteres que no sean espacio en blanco (\S*) seguidos por una letra
    miniscula o mayusucula

    se esta usando * para indicar cero o mas caracteres que no sean espacio, ya que [a-zA-Z0-9]
    implica un caracter distinto de espacio
    
"""
import re
handle = open('mbox-short.txt')
# Búsqueda de líneas que tengan una arroba entre caracteres
# Los caracteres deben ser una letra o un número
count = 0
for line in handle:
    line = line.strip()
    x = re.findall(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        count +=1
        print(x)

print(count)