from ast import Not
from re import I


def iniciar():
    print("jogo da forca")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Chute uma letra")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        else:
            print("continue")
if(__name__ == "__main__"):
    iniciar()