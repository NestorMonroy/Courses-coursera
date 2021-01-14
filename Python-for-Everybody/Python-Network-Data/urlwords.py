import urllib.request as request

man_a = request.urlopen('http://data.pr4e.org/romeo.txt')

contadores = {}

for linea in man_a:
    words = linea.decode().split()
    for word in words:
        contadores[word] = contadores.get(word, 0) + 1

print(contadores)
