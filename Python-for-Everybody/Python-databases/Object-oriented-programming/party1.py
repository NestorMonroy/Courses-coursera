stuff = list()
#Cuando python crea un objecto de clase list(), llama al metodo constructor llamado __init__
stuff.append('python')
stuff.append('nestor')
stuff.sort()
print(stuff[0])  #recuperamos el elemento en la posicion 0
print(stuff.__getitem__(0)) # llamanos al metido __getitem__  con el parametro 0
print(list.__getitem__(stuff, 0)) #una forma mas verbosa de obtener un elemento en posicion 0 de la lista



#Obtener las capacidades de un objecto
print(dir(stuff))