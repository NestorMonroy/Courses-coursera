import xml.etree.ElementTree as ET #el uso de ElementTree nos permite extraer datos del XML sin preocuparnos por esas reglas de sintaxis

data = '''
    <person>
        <name> Chuck </name>
        <phone type="int1" > +1 734 303 44 56</phone>
        <email hide="yes" />
    </person>
    '''

tree = ET.fromstring(data) # la llamada a fromstring => convierte la representación de cadena del XML en un “árbol” de nodos XML. 
print('Name', tree.find('name').text) #La función find() busca a través del árbol XML y recupera el nodo que coincide con la etiqueta especificad
print('Atrr', tree.find('email').get('hide'))

"""
    XML Terminology

    Tags  => indicate the beginning aqnd ending of alements
    Attributres => Keyword/value pairs on t hen opening tags of XML
    Serialize/ De-Serialize => Convert data in one program into a common 
    format that can be stored and/or transmitted between system in a 
    programming language-independent manner
    

"""