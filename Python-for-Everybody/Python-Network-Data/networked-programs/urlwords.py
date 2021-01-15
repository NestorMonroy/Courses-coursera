import urllib.request as request

fhand = request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}

for line in fhand:
    words = line.decode().split()
    for word in words:
        contador[word] = counts.get(word, 0) + 1

print(counts)
