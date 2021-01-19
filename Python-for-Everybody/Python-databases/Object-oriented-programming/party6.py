from party5 import PartyAnimal


class CricketFan(PartyAnimal): #Cuando definimos la clase CricketFan, le estamos diciendo que extiende de PartyAnimal
                                #Esto significa que todas las variabes y metodos de la clase PartyAnimal son heredados por la clase CricketFan
    poinst = 0

    def six(self):
        self.poinst = self.poinst + 6
        self.party()
        print(self.name, "poinst", self.poinst)


s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
print(dir(j)) #al llamar dir, vemos que tiene las instancias y metodos de PartyAnimal