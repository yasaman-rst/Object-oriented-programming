import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self._pet = None

    @property
    def pet(self):
        return self._pet

    @pet.setter
    def pet(self, mammal):
        self._pet = mammal

    def __str__(self):
        pet_info = str(self.pet) if self.pet else "No pet assigned"
        return f"Player {self.player_id}: {self.name} | Pet: {pet_info}"
class Mammal:
    def __init__(self, mammal_id, species, name, size, weight):
        self.mammal_id = mammal_id
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight
    def __str__(self):
        return f"{self.name} ({self.species}) - Size: {self.size}, Weight: {self.weight}kg"   

def roll_dice(num_dice):
    return [Dice().roll() for _ in range(num_dice)]

def mammal_based_on_dice():
    Mammals=[
        Mammal(1, "Hamster","Snow","Small",2),
        Mammal(2, "Cat","Katty","Medium,",6),
        Mammal(3, "Dog","Rockie","Big",15),
    ]
    dice_rolls = roll_dice(2)  # Rolls two dice
    dice_sum = sum(dice_rolls)

    
    if dice_sum <= 5:
        return Mammals[0]  
    elif dice_sum <= 9:
        return Mammals[1] 
    else:
        return Mammals[2]  

def main():
    num_players = int(input("Enter number of players: "))
    num_dice = int(input("Enter number of dice: "))
    players = {i: Player(i, input(f"Enter name for player {i}: ")) for i in range(num_players)}
    
    for player in players.values():
        rolls = roll_dice(num_dice)
        pet = mammal_based_on_dice()
        player.pet = pet
        print(f"{player.name} rolled: {rolls} with sum: {sum(rolls)}")
        
    # Example of assigning a mammal based on a roll
    for player in players.values():
        print(player)

if __name__ == "__main__":
    main()
