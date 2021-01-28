import random

def get_def_and_pop(word_list, word_dict):
    """
        Recupera una definicion y una palabra del diccionario
    """
    random_index = random.randrange(len(word_list)) #randrange => devuelve un elemento en el rango selecionado
    word = word_list.pop(random_index) #.pop => elimina el objeto de la lista
    definition = word_dict.get(word) #.get => devuelve un valor por cada llave en este caso word

    return word, definition

#rawstring trata la "\" como caracter normal sin tomar en cuenta el espacio
def get_word_and_definition(rawstring):
    """
        Regresa una lista separa por comas
    """
    word, definition = rawstring.split(',', 1)
    return word, definition


fh = open("Vocabulary_list.csv", "r")
wd_list = fh.readlines()
#print(wd_list)

wd_list.pop(0) # Elimina la cabecera
wd_set = set(wd_list) # set => crea una nueva coleccion, eliminando los repetidos
fh = open("Vocabulary_set.csv", "w") 
fh.writelines(wd_set) 

word_dict = {}
for rawstring in wd_set:
    word, definition = get_word_and_definition(rawstring)
    #print('dic', word, definition)
    word_dict[word] = definition
    
    #print(word)


while True:
    wd_list = list(word_dict)# se obtiene una lista del diccionario
    choice_list = []
    for x in range(4):
        word,definition = get_def_and_pop(wd_list,word_dict)
        choice_list.append(definition)
    random.shuffle(choice_list)

    print(word)
    print('*' * 5)
    
    for idx, choice in enumerate(choice_list):
        print(idx+1, choice)
    choice = int(input('Enter 1,2,3 or 4; 0 to exit '))
    if choice_list[choice - 1] == definition:
        print('Correct! \n')
    elif choice == 0:
        exit(0)
    else:
        print("Incorrect ")



# A tuple return multiple items from a function