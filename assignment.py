import random

# Function that generates a shuffled deck of 52 cards.
def generate_deck():
    suits = ['c', 'd', 'h', 's']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    deck = [f'{value}{suit}' for suit in suits for value in values]
    random.shuffle(deck)
    return deck

# Function that returns the name of a card given its string representation.
def card_name(card):
    """Converts a card's string representation into a readable name."""
    value_dict = {
        '1': 'Ace', '11': 'Jack', '12': 'Queen', '13': 'King'
    }
    suit_dict = {
        'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts', 's': 'Spades'
    }
    value = card[:-1]
    suit = card[-1]
    
    value_name = value_dict.get(value, value)
    suit_name = suit_dict[suit]
    
    return f'{value_name} of {suit_name}'

# Function that displays the names of the cards in a hand.
def display_hand(hand):
    return ', '.join(card_name(card) for card in hand)

# Function that calculates and returns the total value of a hand.
def hand_value(hand):
    """Calculates the total value of a hand, adjusting for aces if necessary."""
    value_dict = {
        '1': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10, '11': 10, '12': 10, '13': 10
    }
    
    total = 0
    num_aces = 0
    
    for card in hand:
        value = card[:-1]
        total += value_dict[value]
        if value == '1':
            num_aces += 1
    
    # Adjust for aces
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    
    return total

def main():
    print("Starting the Blackjack game...")
    
    deck = generate_deck()
    user_hand = []
    dealer_hand = []
    
    # User's turn
    while True:
        action = input("Draw a card or stop? (d/s): ").strip().lower()
        if action == 'd':
            card = deck.pop()
            user_hand.append(card)
            print(f"You drew: {card_name(card)}")
            print(f"Your hand: {display_hand(user_hand)}")
            if hand_value(user_hand) > 21:
                print("Busted! You Lose!")
                break
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'd' to draw or 's' to stop.")
    
    # Dealer's turn
    while hand_value(dealer_hand) < 17:
        card = deck.pop()
        dealer_hand.append(card)
    
    print(f"Dealer's hand: {display_hand(dealer_hand)}")
    
    # Determine winner
    user_total = hand_value(user_hand)
    dealer_total = hand_value(dealer_hand)
    
    print(f"Your hand value: {user_total}")
    print(f"Dealer's hand value: {dealer_total}")
    
    if user_total > 21:
        print("You lose!")
    elif dealer_total > 21 or user_total > dealer_total:
        print("You win!")
    elif user_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
