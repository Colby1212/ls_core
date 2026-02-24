import random
# import os
HEARTS = chr(9829)
SPADES = chr(9824)
CLUBS = chr(9827)
DIAMONDS = chr(9830)
CARD_NUMBERS= ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = [HEARTS, SPADES, CLUBS, DIAMONDS]
player_moves = ['hit', 'stand']
def prompt(message):
    print(f' ==> {message}')

def join_or(sequence, delimiter=', ', word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{sequence[0]} {word} {sequence[1]}"

    leading_items = delimiter.join(str(item) for item in sequence[0:-1])
    return f'{leading_items}{delimiter}{word} {sequence[-1]}'

def display_hand(hand, starting_dealer_hand = False):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    line5 = ''
    if starting_dealer_hand:
        line1 += " ------  "
        line2 += f"|{hand[0]:<6}| "
        line3 += "|      | "
        line4 += f"|{hand[0]:>6}| "
        line5 += " ------  "
        line1 += " ------  "
        line2 += "|//////| "
        line3 += "|//////| "
        line4 += "|//////| "
        line5 += " ------  "
    else:
        for card in hand:
            line1 += " ------  "
            line2 += f"|{card:<6}| "
            line3 += "|      | "
            line4 += f"|{card:>6}| "
            line5 += " ------  "
    print(line1, line2, line3, line4, line5, sep = '\n')

def display_board(player_hand, dealer_hand, starting_dealer_hand = False):
    # os.system('clear')

    print(f' Dealer: {evaluate_hand(dealer_hand, starting_dealer_hand)}')
    display_hand(dealer_hand, starting_dealer_hand)

    print(''''
     
      
       ''')

    display_hand(player_hand, False)
    print(f'player:{evaluate_hand(player_hand, False)}')


def card_value(card):
    if card[:-1] in ['J', 'Q', 'K']:
        value = 10

    elif card[:-1] == "A":
        value = 1

    else:
        value =  int(card[:-1])
    return value

def reshuffle_deck():
    card_deck = [card + str(suit) for card in CARD_NUMBERS for suit in suits]
    random.shuffle(card_deck)
    shoe = random.randint(15,25)
    return card_deck, shoe

def deal(hand, card_deck):
    hand.append(card_deck.pop())

def player_turn(action, player_hand, card_deck):
    if action == 'hit':
        deal(player_hand, card_deck)

def valid_actions():
    action = input(f'{join_or(player_moves)}: ')
    while action.lower() not in player_moves:
        prompt('Sorry thats not a valid choice')
        action = input(f'{join_or(player_moves)}: ')
    return action.lower()

def opening_deal(player_hand, dealer_hand, card_deck):
    deal(player_hand, card_deck)
    deal(dealer_hand, card_deck)
    deal(player_hand, card_deck)
    deal(dealer_hand, card_deck)

def evaluate_hand(hand, starting_dealer_hand = False):
    hand_value = 0
    if starting_dealer_hand:
        hand = hand[:-1]
    for card in hand:
        if card[:-1] in ['J', 'Q', 'K']:
            hand_value += 10

        elif card[:-1] == "A":
            hand_value += 1

        else:
            hand_value +=  int(card[:-1])
    for card in hand:
        if card[:-1] == "A":
            if hand_value <= 11:
                hand_value += 10
    return hand_value

def check_winner(player_hand, dealer_hand):
    if evaluate_hand(player_hand) > evaluate_hand(dealer_hand):
        return 'player wins'
    if evaluate_hand(player_hand) < evaluate_hand(dealer_hand):
        return 'Dealer wins'
    return 'Push'


def start_new_round(text):
    prompt(text)
    answer = input().lower()
    if answer and answer[0] != 'y':
        return False
    return True


def twenty_one():
    prompt('New Deck')
    card_deck, reshuffle_threshold = reshuffle_deck()
    while True:
        if len(card_deck) < reshuffle_threshold:
            card_deck, reshuffle_threshold = reshuffle_deck()
            prompt('New Deck')
        player_hand = []
        dealer_hand = []
        opening_deal(player_hand, dealer_hand, card_deck)
        display_board(player_hand, dealer_hand, True)

        if evaluate_hand(player_hand) == 21:
            display_board(player_hand, dealer_hand)
            prompt(check_winner(player_hand, dealer_hand))
            continue

        while evaluate_hand(player_hand) < 21:
            move = valid_actions()
            if move == 'stand':
                break
            player_turn(move, player_hand, card_deck)
            display_board(player_hand, dealer_hand, True)

        if evaluate_hand(player_hand) > 21:
            display_board(player_hand, dealer_hand, False)
            prompt('Bust You lose')
            if not start_new_round('Would you like to play again? (y/n)'):
                break
            continue

        while evaluate_hand(dealer_hand) < 17:
            deal(dealer_hand, card_deck)
            display_board(player_hand, dealer_hand, False)
        
        display_board(player_hand, dealer_hand, False)

        if evaluate_hand(dealer_hand) > 21:
            prompt('dealer Busts. You win.')
        else:
            prompt(f'{check_winner(player_hand, dealer_hand)}')

        if not start_new_round('Would you like to play again? (y/n)'):
            break

twenty_one()