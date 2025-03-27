from animal import Animal

class Bird(Animal):

    def __init__(self,food="None"):
        Animal.__init__(self, 2,food)

    def make_sound(self):
        print("*clear bird singing*")
        