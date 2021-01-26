class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)



class FootballFan(PartyAnimal): #Cuando definimos la clase FootballFan, le estamos diciendo que extiende de PartyAnimal
                                #Esto significa que todas las variabes y metodos de la clase PartyAnimal son heredados por la clase FootballFan
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal('Sally')
s.party()
j = FootballFan('Jim')
j.party()
j.touchdown()
#print(dir(j)) #al llamar dir, vemos que tiene las instancias y metodos de PartyAnimal

"""
    Class - a template
    Attribute - a variable within a class
    Method - a function within a class
    Object - a particular instance of a class
    Constructor - Code that runs when an object is created
    Inheritance - The ability to extens a class to  make a new class

"""