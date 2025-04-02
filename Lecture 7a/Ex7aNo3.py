class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None
    
    def name(self):
        return self._name
    
    def numbers(self):
        return self._numbers
    
    def address(self):
        return self._address
    
    def add_number(self, number):
        self._numbers.append(number)
    
    def add_address(self, address):
        self._address = address
    
    def __str__(self):
        num_str = ', '.join(self._numbers) if self._numbers else "number unknown"
        addr_str = self._address if self._address else "address unknown"
        return f"{num_str}\n{addr_str}"

class PhoneBook:
    def __init__(self):
        self._persons = {}
    
    def add_number(self, name, number):
        if name not in self._persons:
            self._persons[name] = Person(name)
        self._persons[name].add_number(number)
    
    def get_entry(self, name):
        return self._persons.get(name, None)
    
    def add_address(self, name, address):
        if name not in self._persons:
            self._persons[name] = Person(name)
        self._persons[name].add_address(address)
    
    def search(self, name):
        person = self.get_entry(name)
        if person:
            print(person)
        else:
            print("number unknown\naddress unknown")

#functionality for adding an address 
def main():
    phonebook = PhoneBook()
    while True:
        print("commands:")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")
        
        command = input("command: ")
        if command == "0":
            break
        elif command == "1":
            name = input("name: ")
            number = input("number: ")
            phonebook.add_number(name, number)
        elif command == "2":
            name = input("name: ")
            phonebook.search(name)
        elif command == "3":
            name = input("name: ")
            address = input("address: ")
            phonebook.add_address(name, address)
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
