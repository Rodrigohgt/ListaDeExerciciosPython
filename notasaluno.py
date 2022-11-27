def iniciar():
    nota1 = float(input("primeira nota "))
    nota2 = float(input("Segunda nota "))

    media = nota1 + nota2
    media = media / 2

    print("a média de nota foi: {}".format(media))

    if(media == 10):
        print("Aprovado com distição")
    elif(media >= 7):
        print("Aprovado")
    else:
        print("Reprovado")
        
if(__name__ == "__main__"):
    iniciar()
