class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return "The balance is {:.1f} euros".format(self.balance)

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount")
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def eat_ordinary(self):
        return self.subtract_from_balance(2.95)

    def eat_luxury(self):
        return self.subtract_from_balance(5.90)


class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.ordinaries = 0
        self.luxuries = 0

    def eat_ordinary(self, payment: float):
        price = 2.95
        if payment >= price:
            self.funds += price
            self.ordinaries += 1
            return payment - price
        return payment

    def eat_luxury(self, payment: float):
        price = 5.90
        if payment >= price:
            self.funds += price
            self.luxuries += 1
            return payment - price
        return payment

    def eat_ordinary_lunchcard(self, card: LunchCard):
        if card.eat_ordinary():
            self.ordinaries += 1
            return True
        return False

    def eat_luxury_lunchcard(self, card: LunchCard):
        if card.eat_luxury():
            self.luxuries += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount")
        card.deposit_money(amount)
        self.funds += amount


# example:

if __name__ == "__main__":
    # Part 1
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)

    # Part 2
    exactum = PaymentTerminal()
    change = exactum.eat_ordinary(10)
    print("The change returned was", change)
    change = exactum.eat_ordinary(5.9)
    print("The change returned was", change)
    change = exactum.eat_luxury(5.9)
    print("The change returned was", change)
    print("Funds available at the terminal:", exactum.funds)
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries)

    # Part 3
    exactum = PaymentTerminal()
    card = LunchCard(7)
    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_ordinary_lunchcard(card)
    print("Payment successful:", result)
    print("Funds available at the terminal:", exactum.funds)
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries)

    # Part 4
    exactum = PaymentTerminal()
    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")
    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")
    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")
    print("Funds available at the terminal:", exactum.funds)
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries)

   
    peter_card = LunchCard(20)
    grace_card = LunchCard(30)
    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")
