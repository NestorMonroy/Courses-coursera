"""
    Una forma sencilla de analizar HTML consiste en utilizar expresiones regulares para hacer búsquedas repetitivas 
    que extraigan subcadenas coincidentes con un patrón en particular

    href="http[s]?://.+?" => Nuestra expresión regular busca cadenas que comiencen con “href="http://” o“href="https://”, 
    seguido de uno o más caracteres (.+?), seguidos por otra comilladoble. El signo de interrogación después de[s]? indica 
    que la coincidencia debe ser hecha en modo “no-codicioso”, en vez de en modo “codicioso”.

    La librería ssl permite a nuestro programa acceder a los sitios web que estrictamente requieren HTTPS. 
    El método read() devuelve código fuente en HTML como un objeto binario en vez de devolver un objeto HTTPResponse.
    El método de expresiones regulares findall() nos da una lista de todas las cadenas que coinciden con la expresión regular, 
    devolviendo solamente el texto del enlace entre las comillas doble


"""
import urllib.request
import re
import ssl

#Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Indroduzca - ') # https://docs.python.org
html = urllib.request.urlopen(url).read()
enlaces = re.findall(b'href="(http[s]?://.*?)"', html)

for enlace in enlaces:
    enlace = enlace.decode()
    print(enlace)