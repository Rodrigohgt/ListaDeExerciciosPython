print("Dia da semana")

sim_nao = 1

while(sim_nao == 1):
    dia = int(input("Digite o dia da semana de acordo com o numero, Segunda (1) Terça (2) Quarta (3) quinta (4) Sexta (5) Sabado (6) Domingo (7)"))

    if(dia == 1):
            print("Hoje é Segunda-feira")
            break
    elif(dia == 2):
            print("Hoje é Terça-feira")
            break
    elif(dia == 3):
            print("Hoje é quarta-feira")
            break
    elif(dia == 4):
            print("Hoje é quinta-feira")
            break
    elif(dia == 5):
            print("Hoje é sexta-feira")
            break
    elif(dia == 6):
            print("Hoje é Sabado")
            break
    elif(dia == 7):
            print("Hoje é Domingo")
            break
                   
    else:
        tentarnovamente = int(input("numero invalido, digite 1 para tentar novamente ou 2 cancelar a aplicação: "))
        
        if(tentarnovamente == 1):
            if(sim_nao):
                print("Tente novamente")
                continue
        else:
            print("Aplicação encerrada")
            break