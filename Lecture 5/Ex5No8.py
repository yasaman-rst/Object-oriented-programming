class Property:
    def __init__(self, square_feet='', num_bedrooms='', num_bathrooms=''):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
    
    def display(self):
        print(f"Square Feet: {self.square_feet}")
        print(f"Bedrooms: {self.num_bedrooms}")
        print(f"Bathrooms: {self.num_bathrooms}")
    
    @classmethod
    def prompt_init(cls):
        return cls(
            square_feet=input("Enter the square feet: "),
            num_bedrooms=input("Enter number of bedrooms: "),
            num_bathrooms=input("Enter number of bathrooms: ")
        )

property = Property.prompt_init()
property.display()

class Apartment(Property):
    def __init__(self, square_feet='', num_bedrooms='', num_bathrooms='', balcony='', laundry=''):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.balcony = balcony
        self.laundry = laundry
    def display(self):
        super().display()
        print(f"Balcony: {self.balcony}")
        print(f"Laundry: {self.laundry}")
class House(Property):
    def __init__(self, square_feet='', num_bedrooms='', num_bathrooms='', num_stories='', garage='', fenced_yard=''):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard        