print("Sistema de urna eletronica")

def iniciar():
    
    votenovamente = "votenovamente"

    while(votenovamente):
        voto = int(input("Digite o numero do candidato que você queira votar"))

        lula = voto == 13
        bolsonaro = voto == 17
        daciolo = voto == 31
        branco = voto == 0

        if(lula):
            print("Você votou no Lula")
            confirmar = int(input("Digite 1 para confirmar ou 2 Para tentar novamente"))
            if(confirmar == 1):
                print("Confirmado voto no lula")
                break
            else:
                if(votenovamente):
                    print("voto cancelado")
                    continue

        elif(bolsonaro):
            print("Você votou no Bolsonaro")
            confirmar = int(input("Digite 1 para confirmar ou 2 Para tentar novamente"))
            if(confirmar == 1):
                print("Confirmado voto no Bolsonaro")
                break
            else:
                if(votenovamente):
                    print("voto cancelado")
                    continue

        elif(daciolo):
            print("Você votou no Daciolo")
            confirmar = int(input("Digite 1 para confirmar ou 2 Para tentar novamente"))
            if(confirmar == 1):
                print("Confirmado voto no Daciolo")
                break
            else:
                if(votenovamente):
                    print("voto cancelado")
                    continue

        elif(branco):
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