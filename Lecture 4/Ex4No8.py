class Recording:
    def __init__(self, length: int):
        self.__length = length  # __ makes it Private variable

    @property
    def length(self):
        return self.__length  # Getter method
    @length.setter
    def length(self, new_length: int):
        self.__length = new_length  # Setter method

# Example:
the_wall = Recording(43)
print(the_wall.length)  
the_wall.length = 44
print(the_wall.length)  
