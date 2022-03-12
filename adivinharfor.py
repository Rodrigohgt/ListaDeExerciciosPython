import random
print("Jogo de adivinhacao")

tentativa = 5 
num_secreto = random.randrange(1,51)
rodada = 1

for rodada in range(1, tentativa + 1):
    print("Tentativas {} de {} ".format(rodada, tentativa))
    chute = int(input("Digite o seu numero: "))
    print("Você digitou: ", chute)


    if(chute < 1 or chute > 100):
        print("Chute um numero entre 1 e 100")
        continue

    acertou = chute == num_secreto
    maior = chute > num_secreto
    menor = chute < num_secreto


    if(acertou):
        print("Você acertou!!! na tentativa: ", rodada)
        break

    else:
        if(maior):
            print("Você chutou muito alto")
        elif(menor):
            print("Você chutou muito abaixo") 