import os #Om du vill cleara skärmen skriv först import os högst upp   #["♠", "♥", "♣", "♦"]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
#Vanlig metod i en klass

    def show(self):
        return f"{self.suit} {self.value}"
    
    def __str__(self):
        return f"{self.suit} {self.value}"
    
    def __repr__(self):
    
        return f"{self.suit} {self.value}"
    

class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = []

        self.cards = cards


    @staticmethod
    def make_deck():
        cards = []
        card_suits = ["♠", "♥", "♣", "♦"]
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        
        for suit in card_suits:
            for value in values:
                cards.append(Card(suit, value))
        return cards
    
deck = Deck()
    

os.system("cls" if os.name == "nt" else "clear") # Sedan skriv detta för att det ska cleara skärmen


for card in deck.cards:
    print(card)


def __str__(self):
    return f"{self.value}"

    pass



cards = Deck.make_deck()

deck = Deck(cards)

cards = Deck.make_deck
dek = Deck(cards)

print(deck)


#cards.append(Card("Hjärter", 2))
#cards.append(Card("Hjärter", 3))
#cards.append(Card("Hjärter", 4))
#cards.append(Card("Hjärter", 5))
#cards.append(Card("Hjärter", 6))
#cards.append(Card("Hjärter", 7))
#cards.append(Card("Hjärter", 8))


