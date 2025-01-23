import random

numbers = []
strings = []

print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nEnter 10 strings:")
for i in range(10):
    string = input(f"Enter string {i+1}: ")
    strings.append(string)

print("\nList of Numbers:", numbers)
print("List of Strings:", strings)

for i in range(10):
    numbers[i] = random.randint(1, 100)

print("\nRandomly generated numbers", numbers)
