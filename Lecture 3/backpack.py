from tools import Tools

class Backpack:
    """
    Models a backpack in an adventure game.
    """

    def __init__(self, capacity):
        """
        Initializes a new backpack that can hold up to the specified capacity of items.
        """
        self.__capacity = capacity
        self.__items = []
        self.__topmost_index = -1  # Better naming for clarity

    # Observer methods
    def is_empty(self):
        """
        Checks if the backpack is empty.
        """
        return len(self.__items) == 0

    def get_capacity(self):
        """
        Returns the total capacity.
        """
        return self.__capacity

    def get_used_space(self):
        """
        Returns the total size of items already in the backpack.
        """
        return sum(item.get_volume() for item in self.__items)

    def get_remaining_capacity(self):
        """
        Returns the amount of free space.
        """
        return self.get_capacity() - self.get_used_space()

    def contains(self, item):
        """
        Checks if the item is in the backpack.
        """
        return item in self.__items

    def show_topmost(self):
        """
        Returns the topmost item.
        """
        assert not self.is_empty(), "The backpack must not be empty."
        return self.__items[self.__topmost_index]

    def __str__(self):
        """
        Returns a string representation of the backpack.
        """
        if self.is_empty():
            return "Backpack contains nothing."
        
        backpack_info = f"Backpack: [fill ratio: ({self.get_used_space()} / {self.get_capacity()})]"
        
        indent = " " * 4  # Better spacing for readability
        for item in self.__items:
            backpack_info += f"\n{indent}{item}"
        
        return backpack_info

    # Modification methods
    def put(self, item):
        """
        Adds an item to the backpack.
        """
        assert item is not None, "Item must not be None."
        assert item.get_volume() <= self.get_remaining_capacity(), "Not enough space in the backpack."
        assert not self.contains(item), "Item is already in the backpack."
        
        self.__items.append(item)
        self.__topmost_index = len(self.__items) - 1  # Keep track of the topmost item

    def remove_topmost(self):
        """
        Removes the topmost item.
        """
        assert not self.is_empty(), "The backpack must not be empty."
        
        self.__items.pop(self.__topmost_index)
        self.__topmost_index = len(self.__items) - 1 if self.__items else -1

    def rummage(self):
        """
        Cycles the contents of the backpack so that the topmost item changes cyclically.
        """
        assert not self.is_empty(), "The backpack must not be empty."
        self.__topmost_index = (self.__topmost_index + 1) % len(self.__items)
