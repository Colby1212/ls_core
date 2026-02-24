import random

class Deck:
    HEARTS = chr(9829)
    SPADES = chr(9824)
    CLUBS = chr(9827)
    DIAMONDS = chr(9830)
    RANKS= list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    SUITS = [HEARTS, SPADES, CLUBS, DIAMONDS]

    def __init__(self):
        self.deck = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS]
    
    def deal(self):
        return self.deck.pop(0)
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def build_deck(self):
        self.deck = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS]

    def __len__(self):
        return len(self.deck)

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f'{self.rank}{self.suit}'

class Hand:

    def __init__(self):
        self.hand = []

    def value_of_first_card(self):
        if not self.hand:
            return 0

        first_card = self.hand[0]
        first_card_value = self.card_value(first_card)
        if first_card_value == 1:
            first_card_value += 10
        return first_card_value

    def add_card(self, card):
        self.hand.append(card)

    Values = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 1,
    }

    def card_value(self, card):
        return self.Values.get(card.rank, card.rank)

    def value(self):
        hand_value = 0 
        ace_counter = 0
        for card in self.hand:
            hand_value += self.card_value(card)
            if card.rank == 'A':
                ace_counter += 1
        if ace_counter > 0 and hand_value < 12:
            hand_value += 10
        return hand_value

    def is_bust(self):
        return self.value() > 21

    def is_21(self):
        return self.value() == 21

    def reveal_one(self):
        card_width = 6
        rank_suit = f'{self.hand[0].rank}{self.hand[0].suit}'
        line1 = f"{' ' + '-' * card_width + '  '}"
        line2 = f"|{rank_suit:<{card_width}}| "
        line3 = f"|{' '*card_width}| "
        line4 = f"|{rank_suit:>{card_width}}| "
        line5 = f"{' ' + '-' * card_width + '  '}"
        line1 += f"{' ' + '-' * card_width + '  '}"
        line2 += f"|{'/' * card_width}|"
        line3 += f"|{'/' * card_width}|"
        line4 += f"|{'/' * card_width}|"
        line5 += f"{' ' + '-' * card_width + '  '}"
        print(line1, line2, line3, line4, line5, sep = '\n')


    def reveal_hand(self):
        card_width = 6
        line1 = ''
        line2 = ''
        line3 = ''
        line4 = ''
        line5 = ''
        for card in self.hand:
            rank_suit = f'{card.rank}{card.suit}'
            line1 += f"{' ' + '-' * card_width + '  '}"
            line2 += f"|{rank_suit:<{card_width}}| "
            line3 += f"|{' '*card_width}| "
            line4 += f"|{rank_suit:>{card_width}}| "
            line5 += f"{' ' + '-' * card_width + '  '}"
        print(line1, line2, line3, line4, line5, sep = '\n')

class Player:

    def __init__(self):
        self.hand = Hand()
        self.money = 0

    def reset_hand(self):
        self.hand = Hand()

    def is_broke(self):
        return self.money <= 0

    def add_funds(self, amount):
        self.money += amount

    def wager_funds(self, amount):
        self.money -= amount

    def display_funds(self):
        print(f'You have {self.money}')

    def hand_value(self):
        return self.hand.value()
    
    def is_hand_bust(self):
        return self.hand.is_bust()
    
    def is_hand_21(self):
        return self.hand.is_21()

    def hit(self, card):
        self.hand.add_card(card)

    def reveal(self):
        return self.hand.reveal_hand()

class Human(Player):
    PLAYER_MOVES = ['hit', 'stand']

    @staticmethod
    def _join_or(choices, separator=", ", conjunction='or'):
        if len(choices) == 2:
            return f'{choices[0]} {conjunction} {choices[1]}'

        last = choices[-1]
        initial = choices[:-1]
        initial = [str(choice) for choice in initial]
        prompt = separator.join(initial)
        return f'{prompt}{separator}{conjunction} {last}'

    def __init__(self):
        super().__init__()

    def choose_move(self):
        while True:
            response = input(f'{self._join_or(self.PLAYER_MOVES)}: ')
            if response.lower() in self.PLAYER_MOVES:
                return response.lower()

            print('Invalid input. Please Try again')


class Dealer(Player):
    def __init__(self):
        super().__init__()

    def one_face_up(self):
        return self.hand.reveal_one()
    

    def face_up_value(self):
        return self.hand.value_of_first_card()


class TwentyOneGame:

    TARGET_SCORE = 21
    DEALER_MUST_STAY_SCORE = 17

    def determine_outcome(self):
        if self.player.is_hand_bust():
            return 'player busts'
        
        if self.dealer.is_hand_bust():
            return 'dealer busts'

        winner = self.compare_hands()
        if winner == 'player':
            return 'player wins'
        
        if winner == 'dealer':
            return 'dealer wins'
        
        return 'push'

    def display_final_result(self, outcome):
        if outcome == 'player busts':
            print(f'You busted with {self.player.hand_value()}!')
        
        elif outcome == 'dealer busts':
            print('Dealer busts! You win!')

        elif outcome == 'player wins':
            print('You win!')
        
        elif outcome == 'dealer wins':
            print('Dealer wins.')

        elif outcome == 'push':
            print('Its a push!')

    def settle_bet(self, outcome, wager):
        if outcome in ['dealer busts', 'player wins']:
            payout = wager * 2
            self.player.add_funds(payout)
        elif outcome == 'push':
            self.player.add_funds(wager)
        
        self.player.display_funds()

    def ensure_cards_available(self):
        minimum_deck_length = 18
        if len(self.deck) < minimum_deck_length:
            print('reshuffling')
            self.deck.build_deck()
            self.deck.shuffle()

    def opening_deal(self):
        for _ in range(2):
            self.player.hit(self.deck.deal())
            self.dealer.hit(self.deck.deal())

    def display_board(self, turn = None):
        if turn == 'player':
            self.dealer.one_face_up()
            print(self.dealer.face_up_value())
            print()
            print()
            print()
            self.player.reveal()
            print(self.player.hand_value())
        else:
            self.dealer.reveal()
            print(self.dealer.hand_value())
            print()
            print()
            print()
            self.player.reveal()
            print(self.player.hand_value())

    def display_welcome_message(self):
        print('Welcome to the game 21!')

    def display_goodbye_message(self):
        print('Goodbye! Thank you for playing 21.')

    def deposit_money(self):
        while True:
            prompt = 'How much would you like to deposit (positive numbers only): $'
            deposit_amount = input(prompt)
            try:
                deposit_amount = int(deposit_amount)
                if deposit_amount > 0:
                    break
            except ValueError:
                print('Please enter a valid number')
                pass
        
        self.player.add_funds(deposit_amount)


    def player_bet(self):
        max_bet = self.player.money
        while True:
            prompt = f'How much would you like to bet(1 - {max_bet}) $'
            bet_amount = input(prompt)
            try:
                bet_amount = int(bet_amount)
                if 0 < bet_amount <= max_bet:
                    break
            except ValueError:
                pass
        self.player.wager_funds(bet_amount)
        print(f'You bet {bet_amount}')
        return bet_amount
        
    def player_twentyone(self):
        return self.player.is_hand_21()

    def __init__(self):
        self.deck = Deck()
        self.player = Human()
        self.dealer = Dealer()

    def reset_players(self):
        self.player.reset_hand()
        self.dealer.reset_hand()

    def compare_hands(self):
        if self.player.hand_value() > self.dealer.hand_value():
            return 'player'
        elif self.player.hand_value() < self.dealer.hand_value():
            return 'dealer'
        else:
            return None

    def player_turn(self):
        while not self.player.is_hand_bust() and not self.player.is_hand_21():
            self.display_board('player')
            choice = self.player.choose_move()
            if choice == 'hit':
                card = self.deck.deal()
                self.player.hit(card)
            else:
                break


    def dealer_turn(self):
        self.display_board()
        while self.dealer.hand_value() < self.DEALER_MUST_STAY_SCORE:
            self.dealer.hit(self.deck.deal())
            self.display_board()

    def one_round(self):
        self.reset_players()
        wager = self.player_bet()
        self.opening_deal()

        if self.player.is_hand_21():
            self.display_board()
            outcome = self.determine_outcome()
            self.display_final_result(outcome)
            self.settle_bet(outcome, wager)
            return
        else:
            self.player_turn()
        
        self.dealer_turn()

        outcome = self.determine_outcome()
        print('\n ----- Final Hands -----')
        self.display_board()
        self.display_final_result(outcome)
        self.settle_bet(outcome, wager)

    def play_again(self):
        while True:
            answer = input('Would you like to play again (y/n) ').lower()
            if answer in ['y', 'n']:
                break
            print("Sorry, that's not a valid choice.\n")
        return answer == 'y'
    
    def start(self):
        self.display_welcome_message()
        self.deck.shuffle()
        self.deposit_money()
        while not self.player.is_broke():
            self.ensure_cards_available()
            self.one_round()
            if self.player.is_broke() or not self.play_again():
                break
        if self.player.is_broke():
            print("\nYou're out of money!")

        self.display_goodbye_message()

game = TwentyOneGame()
game.start()