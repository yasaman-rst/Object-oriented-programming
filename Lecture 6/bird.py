from animal import Animal

class Bird(Animal):

    def __init__(self,food="None"):
        Animal.__init__(self, 2,food)
        self.__food = food
    def get_food(self):
        return self.__food
    def set_food(self, food):
        self.__food = food
    
    def make_sound(self):
        print("*clear bird singing*")
        