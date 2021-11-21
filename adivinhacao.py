import numpy
import random

def jogar():
    print("          ---------------------------")
    print("          Bem vindo ao jogo da sorte!")
    print("          ---------------------------")

    numero_random = random.randrange(1,101)
    tentativas = 3
    print ("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")


    nivel= int(input("O nivel será:"))

    if (nivel == 1):
        tentativas = 20
        print("Você escolheu o nivel fácil, terá {}".format(tentativas))
    elif (nivel == 2):
        tentativas = 10
        print("Você escolheu o nivel Médio, terá {}".format(tentativas))
    else:
        tentativas=5
        print("Você escolheu o nivel Dificil, terá {}".format(tentativas))

    for rodada in range(1,tentativas+1):

        print("Tentativa {} de {}".format(rodada,tentativas))
        palpite = int(input("Digite o seu palpite, o numero deve ser entre 1 e 100: "))
        print( "Você digitou:" , palpite )

        if (palpite < 1 or palpite > 100):
            print("Você digitou um valor invalido")
            continue

        if ( numero_random == palpite ):
            print("Você está com sorte, acertou!!,o numero secreto de fato era:", numero_random)
            break

        elif ( palpite > numero_random ):
            print("Você chutou um valor maior que o numero secreto")
        elif( palpite < numero_random ):
            print("Você chutou um valor menor que o numero secreto")

    print("Fim de jogo, o valor era:{}".format(numero_random))

if(__name__=="__main__"):
    jogar()