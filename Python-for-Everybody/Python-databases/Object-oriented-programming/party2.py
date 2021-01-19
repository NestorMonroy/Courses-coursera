
class PartyAnimal:
    x = 0

    def party(self): #Cada ves que llamamos este metodo x incrementa 1
        self.x = self.x + 1
        print('So fart', self.x)


an = PartyAnimal()  #Crear un objecto o una instancia 
an.party() 
an.party()
an.party()
PartyAnimal.party(an)  #Otra forma de llamadar al metodo party