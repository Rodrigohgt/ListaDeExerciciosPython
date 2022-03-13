print("Sistema de urna eletronica")

def iniciar():
    
    votenovamente = "votenovamente"

    while(votenovamente):
        voto = int(input("Digite o numero do candidato que você queira votar"))

        if(voto == 13):
            print("Você votou no Lula")
            confirmar = int(input("Digite 1 para confirmar ou 2 Para tentar novamente"))
            if(confirmar == 1):
                print("Confirmado voto no lula")
                break
            else:
                if(votenovamente):
                    print("voto cancelado")
                    continue

        elif(voto == 17):
            print("Você votou no Bolsonaro")
            confirmar = int(input("Digite 1 para confirmar ou 2 Para tentar novamente"))
            if(confirmar == 1):
                print("Confirmado voto no Bolsonaro")
                break
            else:
                if(votenovamente):
                    print("voto cancelado")
                    continue

        elif(voto == 31):
            print("Você votou no Daciolo")
            confirmar = int(input("Digite 1 para confirmar ou 2 Para tentar novamente"))
            if(confirmar == 1):
                print("Confirmado voto no Daciolo")
                break
            else:
                if(votenovamente):
                    print("voto cancelado")
                    continue

        elif(voto == 0):
            print("Você votou Branco")
            confirmar = int(input("Digite 1 para confirmar ou 2 Para tentar novamente"))
            if(confirmar == 1):
                print("Confirmado voto no Branco")
                break
            else:
                if(votenovamente):
                    print("voto cancelado")
                    continue

        else:
            if(votenovamente):
                print("Erro, candidato invalido, tente novamente")
                continue


if(__name__ == "__main__"):
    iniciar()