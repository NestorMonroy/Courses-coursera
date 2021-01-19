import xml.etree.ElementTree as ET 

data= '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>'''

stuff = ET.fromstring(data)
#Es importante incluir todos los elementos base en la declaracion de findall() exceptuando aquel que se encuentra en nivel superior
#  'users/user' , de lo contrario python no devolvera ningun elemento
lst = stuff.findall('users/user') #El método findall() devuelve una lista de subárboles que representan las estructuras ‘user’ del árbol XML.
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

