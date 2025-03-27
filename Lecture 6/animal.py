class Animal:

    def __init__(self, number_of_legs,food="unknown"):
        self.__legs = number_of_legs
        self.__food=food #new attribute based on ex1b
    # Getter 
    def get_legs(self):
        return self.__legs

    # Getter 
    def get_food(self):
        return self.__food    

    def make_sound(self):
        print("*it's quiet*")
      
        
        