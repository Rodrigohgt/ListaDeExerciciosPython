
def iniciar():
    print("Jogo de adivinhacao")

    tentativa = 5 
    num_secreto = 42
    rodada = 0

    while(rodada < tentativa):
        print("Tentativas {} de {} ".format(rodada, tentativa))
        chute = int(input("Digite o seu numero: "))
        print("Você digitou: ", chute)

        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        
        if(acertou):
            print("Você acertou!!!")

        else:
            if(maior):
                print("Você chutou muito alto")
            elif(menor):
                print("Você chutou muito abaixo")

        rodada = rodada + 1        
        

if(__name__ == "__main__"):
    iniciar()
