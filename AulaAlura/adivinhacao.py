import random

def jogar():
    print("***************************************")
    print("***Bem vindo no jogo de adivinhação!***")
    print("***************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    # rodada = 1   metodo while


    print("Qual nível de dificuldade? ", numero_secreto)
    print("(1) Facil (2) Médio (3) Difícil")

    nivel = int(input("Selecione o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #while(total_de_tentativas >= rodada):
    for rodada in range(total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = float(input("Digite um número de 1 a 100\n"))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        menor =  chute < numero_secreto
        maior = chute > numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            #    rodada = rodada + 1 metodo while
            if(menor):
                print("Você errou! O número que você digitou é menor que o número secreto.")
            elif(maior):
                print("Você errou! O número que você digitou é maior que o número secreto.")
            pontos_perdidos = abs (numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    #    rodada = rodada + 1 metodo while
    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()