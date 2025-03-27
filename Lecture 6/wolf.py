from mammal import Mammal

class Wolf(Mammal):

    def __init__(self, pack,food="None"):
        Mammal.__init__(self,food)
        self.__pack_name = pack
    # Getter 
    def get_pack_name(self):
        return self.__pack_name

    # Setter 
    def set_pack_name(self, pack):
        self.__pack_name = pack    

    def another_make_sound(self):
        print("*wolf howling*")
        