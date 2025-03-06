from typing import List, Optional
import random

class Item:
    """ an item that can be bought, sold, or gambled."""
    def __init__(self, name: str, value: int):
        
        self.name = name
        self.value = value

class Backpack:
    """ the player's backpack, which holds items."""
    def __init__(self):
        """ an empty backpack."""
        self.items: List[Item] = []

    def add_item(self, item: Item):
        """
        Add an item to the backpack.
        """
        self.items.append(item)

    def remove_item(self, item: Item) -> bool:
        """
        Remove an item from the backpack.
        
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def get_random_item(self) -> Optional[Item]:
        """
         a random item from the backpack.
        
        """
        if not self.items:
            return None
        return random.choice(self.items)

class Shopkeeper:
    def __init__(self, name: str):
        self.name = name

    def greet(self):
        """Greet the player."""
        print(f"{self.name}: Welcome to my shop!")

    def offer_gamble(self, player: 'Player', desired_item: Item) -> bool:
        """
        Offer the player a gamble.
        """
        if not player.backpack.items:
            print(f"{self.name}: Your backpack is empty. No gamble possible.")
            return False

        print(f"{self.name}: Would you like to gamble a random item from your backpack for {desired_item.name}?")
        # Simulate a 50% chance of success
        if random.choice([True, False]):
            random_item = player.backpack.get_random_item()
            player.backpack.remove_item(random_item)
            player.backpack.add_item(desired_item)
            print(f"{self.name}: Congratulations! You received {desired_item.name}.")
            return True
        else:
            print(f"{self.name}: Better luck next time!")
            return False

class Shop:
    
    def __init__(self, shopkeeper: Shopkeeper, items: List[Item]):
        
        self.shopkeeper = shopkeeper
        self.items = items

    def display_items(self):
        """Display the items available in the shop."""
        print("Items for sale:")
        for item in self.items:
            print(f"- {item.name} (Value: {item.value})")

    def buy_item(self, player: 'Player', item: Item):
        """
        Allow the player to buy an item from the shop.
        
        """
        if item in self.items:
            # Simulate currency exchange (not implemented in this example)
            player.backpack.add_item(item)
            self.items.remove(item)
            print(f"{self.shopkeeper.name}: You've purchased {item.name}.")
        else:
            print(f"{self.shopkeeper.name}: That item is not available.")

    def sell_item(self, player: 'Player', item: Item):
        """
        Allow the player to sell an item to the shop.
        
        """
        if item in player.backpack.items:
            player.backpack.remove_item(item)
            self.items.append(item)
            print(f"{self.shopkeeper.name}: You've sold {item.name}.")
        else:
            print(f"{self.shopkeeper.name}: You don't have that item.")

class Player:
    """ the player's character."""
    def __init__(self, name: str):
        
        self.name = name
        self.backpack = Backpack()

# Example usage
if __name__ == "__main__":
    # Create items
    sword = Item("Sword", 50)
    shield = Item("Shield", 30)
    potion = Item("Health Potion", 10)

    # Create shopkeeper and shop
    shopkeeper = Shopkeeper("Old Man")
    shop = Shop(shopkeeper, [sword, shield, potion])

    # Create player
    player = Player("Adventurer")

    # Display shop items
    shop.display_items()

    # Player buys an item
    shop.buy_item(player, sword)

    # Player sells an item
    shop.sell_item(player, sword)

    # Player attempts a gamble
    shop.shopkeeper.offer_gamble(player, shield)