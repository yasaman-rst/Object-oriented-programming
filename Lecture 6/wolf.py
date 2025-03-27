from mammal import Mammal

class Wolf(Mammal):

    def __init__(self, pack,food="None"):
        Mammal.__init__(self,food)
        self.pack_name = pack

    def another_make_sound(self):
        print("*wolf howling*")
        