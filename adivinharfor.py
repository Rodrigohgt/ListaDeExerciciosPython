import random
print("Jogo de adivinhacao")

tentativa = 0
num_secreto = random.randrange(1,51)
rodada = 1

dificuldade = int(input("Selecione o nivel de dificuldade, Facil: 1 / Médio: 2 / Dificil: 3"))

if(dificuldade == 1):
    tentativa = 30
elif(dificuldade == 2):
    tentativa = 20
else:
    tentativa = 10

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
        print("PARABÉNS!! Você acertou na tentativa: ", rodada)
        break

    else:
        if(maior):
            print("Você chutou muito alto")
        elif(menor):
            print("Você chutou muito abaixo") 