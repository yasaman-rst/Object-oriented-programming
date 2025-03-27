from animal import Animal
from mammal import Mammal
from wolf import Wolf
from bird import Bird
from dog import Dog

def run_a_tests():
    a1 = Animal(6,"nectar") # an insect?
    a2 = Animal(4,"grass") # a cow?
        
    print("a1 Food:", a1.get_food())  # Should be "nectar"
    print("a1 Legs:", a1.get_legs())  # Should be 6
    
    print("a2 Food:", a2.get_food())  # Should be "grass"
    print("a2 Legs:", a2.get_legs())  # Should be 4


def run_b_tests():
    a3 = Mammal("Meat")
    a4 = Bird("Seeds")
    
        
    print("a3 Food:", a3.get_food())  # Should be "Meat"
    print("a4 Food:", a4.get_food())  # Should be "Seeds"
    
    print("a3 Legs:", a3.get_legs())  # Should be 4
    print("a4 Legs:", a4.get_legs())  # Should be 2
    
    # Make sounds
    a3.make_sound()  # Should print sound for Mammal
    a4.make_sound()  # Should print sound for Bird

def run_wolf_tests():
    # Test the Wolf class
    wolf1 = Wolf("Jasper","Raasinkorpi", "Ship_Meat")
    print("Wolf Food:", wolf1.get_food())  # Should be "Ship_Meat"
    wolf1.make_sound()  # Should print "Wolf howling"
    wolf1.another_make_sound()  # Should print another sound

def run_dog_tests():
    print("\nRunning Dog tests...")

    dog1 = Dog("Buddy", "Chicken", "Golden Retriever")
    dog2 = Dog("Max", "Beef", "Bulldog")

    print("Dog1 Name:", dog1.get_name())  
    print("Dog1 Food:", dog1.get_food())  
    print("Dog1 Breed:", dog1.get_breed())  

    print("Dog2 Name:", dog2.get_name())  
    print("Dog2 Food:", dog2.get_food())  
    print("Dog2 Breed:", dog2.get_breed())  

    dog1.set_breed("Labrador")
    print("Updated Dog1 Breed:", dog1.get_breed())

    dog1.make_sound()  
    dog2.make_sound()  

    dog1.wag_tail()  
    dog2.fetch("ball")     

if __name__ == "__main__":
    print("Running A tests...")
    run_a_tests()

    print("\nRunning B tests...")
    run_b_tests()

    print("\nRunning Wolf tests...")
    run_wolf_tests()

    print("\nRunning Dog tests...")
    run_dog_tests()


    


