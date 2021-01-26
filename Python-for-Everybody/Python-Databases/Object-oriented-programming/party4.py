class PartyAnimal:
    x = 0

    def __init__(self): #Cuando python construye el objecto, llama a nuestro metodo __init__
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So fart', self.x)

    def __del__(self):
        print('I am a destructed', self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)