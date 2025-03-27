from animal import Animal

class Mammal(Animal):

    def __init__(self,food="None"):
        Animal.__init__(self, 4,food)

    def make_sound(self): 
        print("*mammal breathing*")
        