import json

data = '''
    [
        { "id" :"001",
            "x":"2",
            "name" : "Chuck"
        },
        { "id" :"009",
            "x":"7",
            "name" : "Brent"
        }
    ]
'''

info = json.loads(data) #json.loads() es una lista de PYthon que recorremos con un bucle for y cada elemento dentro de esa lista es un diccionario
print('User count:', len(info), "\n")

for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])
