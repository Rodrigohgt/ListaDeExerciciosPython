import random

def iniciar():

    print("Jogo de adivinhacao")

    tentativa = 0
    num_secreto = random.randrange(1,51)
    rodada = 1
    pontos = 500

    dificuldade = int(input("Selecione o nivel de dificuldade, Facil: 1 / Médio: 2 / Dificil: 3 {}".format(num_secreto)))

    if(dificuldade == 1):
        tentativa = 15
    elif(dificuldade == 2):
        tentativa = 10
    else:
        tentativa = 5

    for rodada in range(1, tentativa + 1):
        print("Tentativas {} de {} ".format(rodada, tentativa))
        chute = int(input("Digite o seu numero: "))
        print("Você digitou: ", chute)


        if(chute < 1 or chute > 100):
            print("Chute um numero entre 1 e 100")
            

        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto


        if(acertou):
            print("PARABÉNS!! Você acertou na tentativa: {} e fez o total de: {} pontos".format(rodada,pontos))
            break

        else:
            if(maior):
                print("Você chutou muito alto")
            elif(menor):
                print("Você chutou muito abaixo") 
            pontos_perdidos = abs(num_secreto - 20)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")

if(__name__ == "__main__"):
    iniciar()