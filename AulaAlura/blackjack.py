import random

def jogar():
    print("***************************************")
    print("***Bem vindo no jogo de blackjack!***")
    print("***************************************")

    naipes = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    valors = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
            'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    playing = True

    # CLASSES


    class Card: #Carta
        def __init__(self, naipe, valor):
            self.naipe = naipe
            self.valor = valor

        def __str__(self):
            return self.valor + ' de ' + self.naipe


    class Deck:  # Baralho

        def __init__(self):
            self.deck = []
            for naipe in naipes:
                for valor in valors:
                    self.deck.append(Card(naipe, valor))

        def __str__(self):
            deck_comp = ''
            for card in self.deck:
                deck_comp += '\n ' + card.__str__()
            return 'O baralho contém: ' + deck_comp

        def shuffle(self):  # embaralhar
            random.shuffle(self.deck)

        def deal(self):  # distribuir
            single_card = self.deck.pop()
            return single_card # carta unica


    class Hand:   # mao

        def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0  

        def add_card(self, card):  # adicionar carta
            self.cards.append(card)
            self.value += values[card.valor]
            if card.valor == 'Ace':
                self.aces += 1

        def adjust_for_ace(self): # ajustar para ace
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1

    class Chips:   # Fichas

        def __init__(self):
            self.total = 1000
            self.bet = 0

        def win_bet(self): #ganhar aposta
            self.total += self.bet

        def lose_bet(self): #perder aposta
            self.total -= self.bet


    # FUNCTIONS

    def take_bet(chips):  # fazer aposta
        while True:
            try:
                chips.bet = int(input("Quantas fichas você gostaria de apostar? "))
            except ValueError:
                print("Desculpe! Por favor, você pode digitar um número: ")
            else:
                if chips.bet > chips.total: #total de fichas
                    print("Você aposta não pode exceder 1000! ")
                else:
                    break


    def hit(deck, hand): #bater baralho, mao
        hand.add_card(deck.deal()) #adicionar
        hand.adjust_for_ace() #ajustar


    def hit_or_stand(deck, hand):   # bater ou ficar
        global playing

        while True:
            ask = input("\nVocê gostaria de continuar ou parar? Digite 'b' ou 'f':")

            if ask[0].lower() == 'b':
                hit(deck, hand) #continuar
            elif ask[0].lower() == 'f': #parar
                print("Jogador fica de pé, Dealer está jogando.")
                playing = False
            else:
                print("Desculpe! Eu não entendi isso! Por favor, tente novamente!")
                continue
            break


    def show_some(player, dealer): # mostrar algumas
        print("\nMão do dealer: ")
        print(" <carta escondida>")
        print("", dealer.cards[1])
        print("\nMão do jogador:", *player.cards, sep='\n ')


    def show_all(player, dealer): # mostrar tudo
        print("\nMão do dealer: ", *dealer.cards, sep='\n ')
        print("Mão do dealer =", dealer.value)
        print("\nMão do jogador: ", *player.cards, sep='\n ')
        print("Mão do jogador =", player.value)

    def player_busts(player, dealer, chips):
        print("O jogador estourou!")
        chips.lose_bet()# fichas perder aposta


    def player_wins(player, dealer, chips):
        print("O Jgador ganha!")
        chips.win_bet()# fichas ganhar aposta


    def dealer_busts(player, dealer, chips):
        print("O dealer estourou")
        chips.win_bet()


    def dealer_wins(player, dealer, chips):
        print("O dealer ganha!")
        chips.lose_bet()


    def push(player, dealer):#empate
        print("É um empate! do jogador e do dealer")


    # Gameplay!

    while True:
        print("Bem vindo ao BlackJack!")
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # configurar as fichas do jogador
        player_chips = Chips()

        # pedir ao jogador para fazer uma aposta
        take_bet(player_chips)

        # mostrar cartas
        show_some(player_hand, dealer_hand)

        while playing:

            hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        if player_hand.value <= 21: #mao do jogador

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
        if new_game[0].lower() == 's': #novo jogo
            playing = True
            continue
        else:
            print("\nObrigado por jogar!")
            break

if(__name__ == "__main__"):
    jogar()