import random

# Class definition
class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        result = random.randint(1, 10)  # Generate a random number between 1 and 10
        
        if result <= 5:  
            self.sideup = 'Tails'
        elif result <= 8:  
            self.sideup = 'Heads'
        elif result <= 9:  
            self.sideup = 'Upright'
        else:  
            self.sideup = 'Rabbit hole'

    def get_sideup(self):
        return self.sideup

# Main function definition
def main():
    my_coin = Coin()
    print("This side is up:", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    print("Now this side is up:", my_coin.get_sideup())

# Calling the main function
main()
