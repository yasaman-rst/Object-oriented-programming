from mammal import Mammal

class Wolf(Mammal):

    def __init__(self,name, pack,food="None"):
        super().__init__(food)  
        self.__name = name  
        self.__pack_name = pack 
    def get_name(self):
        return self.__name   
    # Getter 
    def get_pack_name(self):
        return self.__pack_name

    # Setter 
    def set_pack_name(self, pack):
        self.__pack_name = pack    

    def another_make_sound(self):
        print("*wolf howling*")
        