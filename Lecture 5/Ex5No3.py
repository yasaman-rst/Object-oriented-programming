class Item:
    def __init__(self, name: str, weight: int):
        self._name = name
        self._weight = weight
    
    def name(self) -> str:
        return self._name
    
    def weight(self) -> int:
        return self._weight
    
    def __str__(self) -> str:
        return f"{self._name} ({self._weight} g)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.items = []
    
    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.max_weight:
            self.items.append(item)
    
    def weight(self) -> int:
        return sum(item.weight() for item in self.items)
    
    def print_items(self):
        for item in self.items:
            print(item)
    
    def heaviest_item(self) -> Item:
        if not self.items:
            return None
        return max(self.items, key=lambda item: item.weight())
    
    def __str__(self) -> str:
        count = len(self.items)
        weight = self.weight()
        item_word = "item" if count == 1 else "items"
        return f"{count} {item_word} ({weight} g)"
    
class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight * 1000  #  kg to grams
        self.suitcases = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.max_weight:
            self.suitcases.append(suitcase)
    
    def weight(self) -> int:
        return sum(suitcase.weight() for suitcase in self.suitcases)
    
    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()
    
    def __str__(self) -> str:
        count = len(self.suitcases)
        weight = self.weight()
        return f"{count} suitcases, total weight {weight} g"


# Test
book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)
adas_suitcase = Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)
peters_suitcase = Suitcase(1000)
peters_suitcase.add_item(brick)
cargo_hold = CargoHold(100)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)
print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()