import forca
import adivinhacao
import blackjack

def escolhe_jogo():
    print("*************************")
    print("***Escolha o seu jogo!***")
    print("*************************")

    print("(1) Adivinhação (2) Forca (3) BlackJack")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 3):
        print("Jogando Blackjack")
        blackjack.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()