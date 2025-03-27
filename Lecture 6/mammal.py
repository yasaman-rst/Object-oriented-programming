from animal import Animal

class Mammal(Animal):

    def __init__(self,food="None"):
        super().__init__(4)
        self.__food = food  # Private variable 
    # Getter 
    def get_food(self):
        return self.__food

    # Setter 
    def set_food(self, food):
        self.__food = food

    def make_sound(self): 
        print("*mammal breathing*")

    def number_of_legs(self):
        return 4     