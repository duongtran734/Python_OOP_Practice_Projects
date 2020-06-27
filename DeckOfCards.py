from random import randrange, randint
from colored import fg, bg, attr


# Card Class can generate a Card
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        if value == 1:
            self.value = 'Aces'
        elif value == 11:
            self.value = "Jacks"
        elif value == 12:
            self.value = "Queens"
        elif value == 13:
            self.value = "Kings"
        else:
            self.value = value

    def __str__(self):
        return self.show()

    def show(self):
        return f"{fg(0)}{self.value} of {self.suit.show()}"


# Suit Class
class Suit:

    def __init__(self, symbol):
        if symbol == "Clubs":
            self._symbol = f"{fg(232)}♣"
        elif symbol == "Diamonds":
            self._symbol = f"{fg(1)}♦"
        elif symbol == "Hearts":
            self._symbol = f"{fg(1)}♥"
        elif symbol == "Spades":
            self._symbol = f"{fg(232)}♠"

    def show(self):
        return f'{self._symbol}'

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, new_to):
        self._symbol = new_to


# Deck class to create a deck of card
class Deck:

    def __init__(self):
        self.deck = []
        self.build_deck()

    def build_deck(self):
        Suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        for suit in Suits:
            for value in range(1, 14):
                self.deck.append(Card(Suit(suit), value))

    def show(self):
        for card in self.deck:
            print(card.show())

    # Fisher-Yates Shuffle Algorithm
    def shuffle(self):
        for i in range(len(self.deck) - 1, 0, -1):
            swap_loc = randint(0, i)
            if self.deck[i] != self.deck[swap_loc]:
                self.deck[i], self.deck[swap_loc] = self.deck[swap_loc], self.deck[i]

    # Remove a card from top of the deck
    # Note: deck is a list contain cards
    # Cards are objects created from class Card
    def draw_card(self):
        return self.deck.pop()

    # Get the size of the deck
    def __len__(self):
        return len(self.deck)


# User class
class User():

    def __init__(self, user_name):
        self.name = user_name
        self.hand = []

    # Draw a card from top of the deck and put it into player hand
    # return self from a method: returns a reference to the instance object on which it was called
    # used return self to chain the method together
    def draw(self, deck):
        self.hand.append(Deck.draw_card(deck))
        return self

    def show_hand(self):
        for card in self.hand:
            print(card.show())
        return self

    # Remove 1 card from the hand
    def discard(self):
        return self.hand.pop(randint(0, len(self.hand) - 1))


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.show()

    user1 = User("Bob")
    user1.draw(deck).draw(deck)
    user1.show_hand()


