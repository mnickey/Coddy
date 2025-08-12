from deck import Deck

# Comprehensive test case handler
test_case = input()

def test_basic_functionality():
    deck = Deck()
    assert len(deck) == 52, f"Deck should have 52 cards, but has {len(deck)}"
    
    first_card = deck[0]
    assert isinstance(first_card, str), f"Card should be a string, but got {type(first_card)}"
    
    assert "AS" in deck, "Ace of Spades should be in the deck"
    assert "XY" not in deck, "XY is not a valid card and should not be in the deck"
    
    cards = [card for card in deck]
    assert len(cards) == 52, f"Iteration should yield 52 cards, but got {len(cards)}"
    
    original_first_five = [deck[i] for i in range(5)]
    deck.shuffle()
    shuffled_first_five = [deck[i] for i in range(5)]
    assert original_first_five != shuffled_first_five or len(deck) <= 5, "Shuffle should change card order"
    
    print("Basic functionality tests passed!")

def test_edge_cases():
    deck = Deck()
    
    # Test first and last card access
    first_card = deck[0]
    last_card = deck[51]
    assert isinstance(first_card, str) and isinstance(last_card, str), "First and last cards should be strings"
    
    # Test negative indexing
    assert deck[-1] == deck[51], "Negative indexing should work correctly"
    
    # Test out of bounds access
    try:
        invalid_card = deck[52]
        print("Test failed: Should raise IndexError for out of bounds access")
    except IndexError:
        print("Edge case test passed: IndexError raised for out of bounds access")
    
    print("Edge case tests passed!")

def test_card_uniqueness():
    deck = Deck()
    cards = [card for card in deck]
    unique_cards = set(cards)
    
    assert len(unique_cards) == 52, f"All cards should be unique, but found {len(unique_cards)} unique cards"
    
    # Verify specific cards exist
    expected_cards = ["2H", "10S", "KD", "AC"]
    for card in expected_cards:
        assert card in deck, f"Expected card {card} not found in deck"
    
    print("Card uniqueness tests passed!")

def test_shuffle_behavior():
    deck = Deck()
    original_order = [card for card in deck]
    
    # First shuffle
    deck.shuffle()
    first_shuffle = [card for card in deck]
    assert len(first_shuffle) == 52, "Shuffle should preserve all 52 cards"
    assert set(first_shuffle) == set(original_order), "Shuffle should not add or remove cards"
    
    # Most likely the order changed (though there's a tiny probability it didn't)
    different_order = (original_order != first_shuffle)
    
    # Second shuffle to be extra sure
    deck.shuffle()
    second_shuffle = [card for card in deck]
    different_order_2 = (first_shuffle != second_shuffle)
    
    assert different_order or different_order_2, "Multiple shuffles should change the order"
    
    print("Shuffle behavior tests passed!")

def test_contains_behavior():
    deck = Deck()
    
    # Test all valid cards are in the deck
    suits = ['H', 'D', 'C', 'S']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    for suit in suits:
        for rank in ranks:
            card = rank + suit
            assert card in deck, f"Valid card {card} should be in the deck"
    
    # Test invalid cards are not in the deck
    invalid_cards = ["1H", "11S", "XD", "AX", "JX", ""]
    for card in invalid_cards:
        assert card not in deck, f"Invalid card {card} should not be in the deck"
    
    print("Contains behavior tests passed!")

def test_iteration_behavior():
    deck = Deck()
    
    # Test iteration
    card_count = 0
    for card in deck:
        card_count += 1
        assert isinstance(card, str), f"Each card should be a string, but got {type(card)}"
    
    assert card_count == 52, f"Iteration should yield 52 cards, but got {card_count}"
    
    # Test multiple iterations
    first_iteration = [card for card in deck]
    second_iteration = [card for card in deck]
    assert first_iteration == second_iteration, "Multiple iterations should yield the same order"
    
    print("Iteration behavior tests passed!")

# Run the appropriate test based on input
if test_case == "basic_functionality":
    test_basic_functionality()
elif test_case == "edge_cases":
    test_edge_cases()
elif test_case == "card_uniqueness":
    test_card_uniqueness()
elif test_case == "shuffle_behavior":
    test_shuffle_behavior()
elif test_case == "contains_behavior":
    test_contains_behavior()
elif test_case == "iteration_behavior":
    test_iteration_behavior()
else:
    # Default test - run the original test suite
    def test_deck():
        try:
            # Test initialization and length
            deck = Deck()
            assert len(deck) == 52, f"Deck should have 52 cards, but has {len(deck)}"
            
            # Test getitem
            first_card = deck[0]
            assert isinstance(first_card, str), f"Card should be a string, but got {type(first_card)}"
            
            # Test contains
            assert "AS" in deck, "Ace of Spades should be in the deck"
            assert "XY" not in deck, "XY is not a valid card and should not be in the deck"
            
            # Test iteration
            cards = [card for card in deck]
            assert len(cards) == 52, f"Iteration should yield 52 cards, but got {len(cards)}"
            assert len(set(cards)) == 52, "All cards in the deck should be unique"
            
            # Test shuffle (basic check that order changes)
            original_first_five = [deck[i] for i in range(5)]
            deck.shuffle()
            shuffled_first_five = [deck[i] for i in range(5)]
            assert original_first_five != shuffled_first_five or len(deck) <= 5, "Shuffle should change card order"
            
            # Check that shuffle doesn't lose cards
            assert len(deck) == 52, f"Deck should still have 52 cards after shuffle, but has {len(deck)}"
            
            print("All tests passed!")
        except AssertionError as e:
            print(f"Test failed: {e}")

    test_deck()
    print("Tests completed")
