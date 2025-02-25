class Character:
    """
        Models a character in an adventure game.
    """

    def __init__(self, name, strength, skill, max_health):
        self.__name = name
        self.__strength = strength
        self.__skill = skill
        self.__max_health = max_health
        self.__health = max_health

        self.__left_hand = None
        self.__right_hand = None
        self.__backpack = None

    # Observation

    def is_alive(self):
        return self.__health > 0.0

    def has_free_hand(self):
        return self.is_left_hand_free() or self.is_right_hand_free()

    def is_left_hand_free(self):
        return self.__left_hand is None

    def is_right_hand_free(self):
        return self.__right_hand is None

    def get_left_hand_item(self):
        return self.__left_hand

    def get_right_hand_item(self):
        return self.__right_hand

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_backpack(self):
        """Returns the character's backpack."""
        return self.__backpack

    def __str__(self):
        class_name = self.__class__.__name__
        character_info = f"{class_name}: [{self.__name} {self.__strength} {self.__skill} ({self.__health} / {self.__max_health})]"

        indent = " " * (len(character_info) // 4)
        character_info += f"\n{indent}right: {self.__right_hand}"
        character_info += f"\n{indent}left: {self.__left_hand}"
        
        if self.__backpack:
            character_info += "\n" + self.__backpack.__str__()
        
        return character_info

    # Modification

    def set_left_hand(self, item):
        self.__left_hand = item

    def set_right_hand(self, item):
        self.__right_hand = item

    def set_free_hand(self, item):
        if self.is_right_hand_free():
            self.set_right_hand(item)
        else:
            self.set_left_hand(item)

    def set_backpack(self, new_backpack):
        self.__backpack = new_backpack

    def give_item(self, other, item):
        other.set_free_hand(item)
        if item == self.get_left_hand_item():
            self.set_left_hand(None)
        if item == self.get_right_hand_item():
            self.set_right_hand(None)

    def take_damage(self, damage_amount):
        self.__health -= damage_amount

    def attack(self, other, use_right_hand):
        import random
        luck = random.random()
        multiplier = self.__strength / 100.0 + self.__skill / 120.0

        weapon = self.get_right_hand_item() if use_right_hand else self.get_left_hand_item()
        damage = 1.0 if weapon is None or not weapon.is_functional() else weapon.get_damage()
        
        damage *= multiplier * luck
        other.take_damage(damage)

    def heal_fully(self):
        self.__health = self.__max_health
