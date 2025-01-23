phonebook = {}

while True:
    command = input("1=search, 2=add, 3=quit: ")

    if command == '1':
        name = input("name: ")
        print(phonebook.get(name, "no number"))

    elif command == '2':
        name = input("name: ")
        number = input("number: ")
        phonebook[name] = number
        print("ok!")

    elif command == '3':
        break
