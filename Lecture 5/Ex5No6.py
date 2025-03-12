import random

class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")
            winner = self.round_winner(answer1, answer2)
            if winner == 1:
                self.wins1 += 1
                print("player 1 won")
            elif winner == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class RockPaperScissorsLizardSpock(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_choices = ["rock", "paper", "scissors", "lizard", "spock"]
        if player1_word not in valid_choices or player2_word not in valid_choices:
            return 0  

        rules = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }

        if player2_word in rules[player1_word]:
            return 1
        elif player1_word in rules[player2_word]:
            return 2
        else:
            return 0  

# Example :
p =RockPaperScissorsLizardSpock(3)
p.play()