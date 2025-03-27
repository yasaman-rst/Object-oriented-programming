from wolf import Wolf  

class Dog(Wolf):
    def __init__(self, name, food="Dog Food", breed="Unknown"):
        super().__init__(name, food)  
        self.__breed = breed  # Private attribute 

    # Getter 
    def get_breed(self):
        return self.__breed

    # Setter 
    def set_breed(self, breed):
        self.__breed = breed

    def make_sound(self):
        print("Woof! Woof!")  # Dog sound

    # Another method
    def wag_tail(self):
        print(f"{self.get_name()} is wagging its tail happily!")

    # Another method
    def fetch(self, item):
        print(f"{self.get_name()} fetched the {item}!")
