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

numbers.sort()  
strings.sort() 

print("\nnumbers in the list from smallest to largest:", numbers)
print("strings in alphabetical order:", strings)
