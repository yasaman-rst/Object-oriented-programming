import random

min = 1
max = 6

#The function for rolling the dice. Should print a number between 1 and 6...
def roll (min, max):
    number = random.randint(min, max)
    print("The random number for you is :",number)
    return

roll(min, max)