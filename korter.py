class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit} {self.value}"


class Deck:
    def __init__(self):
        self.cards = self.make_deck()

    @staticmethod
    def make_deck():
        cards = []
        suits = ["♠", "♥", "♣", "♦"]
        values = ["A",1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

        for suit in suits:
            for value in values:
                cards.append(Card(suit, value))

        return cards

    def show_deck(self):
        for card in self.cards:
            print(card)

    def draw_card(self):
        if self.cards:
            removed_card = self.cards.pop()
            print(f"{removed_card} has been removed")
            return removed_card
        else:
            print("No cards left")
            return None

deck = Deck()
deck.show_deck()

while True:
    user_choice = input("Do you want to remove card (yes/no):")
    if user_choice.lower() == "y":
        deck.draw_card()
    elif user_choice.lower() == "n":
        print("Quiting the game")
        break
    else:
        print("S")