class Animal:

    def __init__(self, number_of_legs,food="unknown"):
        self.legs = number_of_legs
        self.food=food #new attribute based on ex1b

    def number_of_legs(self): 
        return self.legs

    def make_sound(self):
        print("*it's quiet*")
      
        
        