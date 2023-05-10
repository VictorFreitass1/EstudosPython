# IMPORT MODULES AND DEFINE VARIABLES

import random

def jogar():
    print("***************************************")
    print("***Bem vindo no jogo de blackjack!***")
    print("***************************************")

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

# CLASSES


class Card:  # Creates all the cards

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:  # creates a deck of cards

    def __init__(self):
        self.deck = []  # haven't created a deck yet
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):  # shuffle all the cards in the deck
        random.shuffle(self.deck)

    def deal(self):  # pick out a card from the deck
        single_card = self.deck.pop()
        return single_card


class Hand:   # show all the cards that the dealer and player have

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # keep track of aces

    def add_card(self, card):  # add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:   # keep track of chips

    def __init__(self):
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# FUNCTIONS

def take_bet(chips):  # ask for user's bet

    while True:
        try:
            chips.bet = int(input("Quantas fichas você gostaria de apostar? "))
        except ValueError:
            print("Desculpe! Por favor, você pode digitar um número: ")
        else:
            if chips.bet > chips.total:
                print("Você aposta não pode exceder 1000! ")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):   # hit or stand
    global playing

    while True:
        ask = input("\nVocê gostaria de bater ou ficar? Digite 'b' ou 'f':")

        if ask[0].lower() == 'b':
            hit(deck, hand)
        elif ask[0].lower() == 'f':
            print("Jogador fica de pé, Dealer está jogando.")
            playing = False
        else:
            print("Desculpe! Eu não entendi isso! Por favor, tente novamente!")
            continue
        break


def show_some(player, dealer):
    print("\nMão do dealer: ")
    print(" <cartão escondido>")
    print("", dealer.cards[1])
    print("\nMão do jogador:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nMão do dealer: ", *dealer.cards, sep='\n ')
    print("Mão do dealer =", dealer.value)
    print("\nMão do jogador: ", *player.cards, sep='\n ')
    print("Mão do jogador =", player.value)


# game endings

def player_busts(player, dealer, chips):
    print("BUSTO DO JOGADOR!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("JOGADOR GANHA!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("BUSTO DO DEALER")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER GANHA!")
    chips.lose_bet()


def push(player, dealer):
    print("É um empurrão! Laço do jogador e do negociante!")


# Gameplay!

while True:
    print("Bem vindo ao BlackJack!")

    # create an shuffle deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up the player's chips
    player_chips = Chips()

    # ask player for bet
    take_bet(player_chips)

    # show cards
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("\nOs ganhos do jogador estão em", player_chips.total)

    new_game = input("\nGostaria de jogar novamente? Digite 's' ou 'n': ")
    if new_game[0].lower() == 's':
        playing = True
        continue
    else:
        print("\nObrigado por jogar!")
        break

if(__name__ == "__main__"):
    jogar()