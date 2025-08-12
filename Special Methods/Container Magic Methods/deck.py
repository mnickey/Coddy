import random

class Deck:
    def __init__(self):
        # TODO: Initialize the deck with 52 standard playing cards
        # TODO: Create a list of cards using suits ['H', 'D', 'C', 'S'] and
        # TODO: ranks ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # TODO: Store cards as strings like "2H" (2 of Hearts) or "AS" (Ace of Spades)
        # TODO: Use a list comprehension to create all combinations of rank+suit
        suits = ['H', 'D', 'C', 'S']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [rank + suit for suit in suits for rank in ranks]
    
    def __len__(self):
        # TODO: Return the number of cards in the deck
        # TODO: This enables the len(deck) functionality
        return len(self.cards)
    
    def __getitem__(self, index):
        # TODO: Return the card at the specified index
        # TODO: This enables indexing like deck[0] to get the first card
        return self.cards[index]
    
    def __contains__(self, card):
        # TODO: Check if the specified card is in the deck
        # TODO: This enables the 'in' operator like "AS" in deck
        return card in self.cards
    
    def __iter__(self):
        # TODO: Return an iterator for the cards
        # TODO: This enables iteration like 'for card in deck'
        # TODO: Use the built-in iter() function on your cards collection
        return iter(self.cards)
    
    def shuffle(self):
        # TODO: Randomize the order of cards in the deck
        # TODO: Use random.shuffle() on your cards collection
        random.shuffle(self.cards)
