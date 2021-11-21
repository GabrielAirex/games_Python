import adivinhacao
import forca


print("          ----------------------------")
print("          |||||Escolha o seu jogo|||||")
print("          ----------------------------")
print ("Digite (1) para jogar forca, Digite (2) para jogar Adivinhação")

jogo = int(input("O jogo será: "))

if jogo ==1:
    print("O jogo escolhido foi Forca")
    forca.jogar()
elif jogo == 2:
    print("O jogo escolhido foi Adivinhação")
    adivinhacao.jogar()
else:
    print("O codigo foi invalido, você deve escolher entre 1 e 2")
