import random

def jogar():
    print("          ---------------------------")
    print("          Bem vindo ao jogo da forca!")
    print("          ---------------------------")


    arquivo=open("palavras.txt","r")
    palavras=[]
    for linha in arquivo:
        palavras.append(linha.strip())
    numero=random.randrange(0,len(palavras))

    palavra_secreta=palavras[numero].upper()

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
            print("Você cometeu um erro {}/6".format(erro,))

        enforcou = erro ==6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns, você ganhou a palavra era: {}".format(palavra_secreta))
    else:
        print("você perdeu a palavra era: {}".format(palavra_secreta))
if(__name__=="__main__"):
    jogar()