import random

def imprime_mensagem_abertura():
    print("          ---------------------------")
    print("          Bem vindo ao jogo da forca!")
    print("          ---------------------------")

def input_palavra_arq():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta=input_palavra_arq()


    letras_acertadas=["_" for letra in palavra_secreta]




    enforcou = False
    acertou = False
    erro=0
    print(letras_acertadas)
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ").strip().upper()
        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if(chute == letra):
                   letras_acertadas[index] =letra
                index+=1
        else:
            erro+=1
            print("Você cometeu um erro {}/7".format(erro,))
            print("  _______     ")
            print(" |/      |    ")
            if (erro == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if (erro == 2):
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")

            if (erro == 3):
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if (erro == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if (erro == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if (erro == 6):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if (erro == 7):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

        enforcou = erro ==7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns, você ganhou a palavra era: {}".format(palavra_secreta))
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("você perdeu a palavra era: {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
if(__name__=="__main__"):
    jogar()