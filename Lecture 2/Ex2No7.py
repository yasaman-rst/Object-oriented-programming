class Pet :
    def __init__(self,name,species,year_of_birth):
        self.name = name 
        self.species = species
        self.year_of_birth = year_of_birth
def new_pet(name,species,year_of_birth):
        return Pet(name, species, year_of_birth)

Jasper = new_pet("Jasper", "poodle dog", 2023)

print(Jasper.name)          
print(Jasper.species)      
print(Jasper.year_of_birth)       