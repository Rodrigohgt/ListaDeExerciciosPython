print("Negociação de fatura")


erro = True

while(erro):
    fatura = float(input("Qual o valor da fatura ?")) 
    divisao = int(input("parcelar divida em até 10X. Qual o valor da parcela:  "))
    
    if(divisao == 1):
        print("Valor sera pago avista no total original da fatura R${}" .format(fatura))
        break
    elif(divisao == 2):
        novovalor = fatura / divisao * 10
        valorparcela = novovalor / divisao 
        print("O valor da sua fatura agora é R${:.2f} e valor da parcelar é {} de R${:.2f}".format(novovalor, divisao, valorparcela))
        break
    elif(divisao == 3):
        novovalor = fatura / divisao * 10.2
        valorparcela = novovalor / divisao 
        print("O valor da sua fatura agora é R${:.2f} e valor da parcelar é {} de R${:.2f}".format(novovalor, divisao, valorparcela))
        break
    elif(divisao == 4):
        novovalor = fatura / divisao * 10.5
        valorparcela = novovalor / divisao 
        print("O valor da sua fatura agora é R${:.2f} e valor da parcelar é {} de R${:.2f}".format(novovalor, divisao, valorparcela))
        break
    elif(divisao == 5):
        novovalor = fatura / divisao * 10.8
        valorparcela = novovalor / divisao 
        print("O valor da sua fatura agora é R${:.2f} e valor da parcelar é {} de R${:.2f}".format(novovalor, divisao, valorparcela))
        break
    elif(divisao == 6):
        novovalor = fatura / divisao * 11
        valorparcela = novovalor / divisao 
        print("O valor da sua fatura agora é R${:.2f} e valor da parcelar é {} de R${:.2f}".format(novovalor, divisao, valorparcela))
        break
    elif(divisao == 7):
        novovalor = fatura / divisao * 11.2
        valorparcela = novovalor / divisao 
        print("O valor da sua fatura agora é R${:.2f} e valor da parcelar é {} de R${:.2f}".format(novovalor, divisao, valorparcela))
        break
    elif(divisao == 8):
        novovalor = fatura / divisao * 12
        valorparcela = novovalor / divisao 
        print("O valor da sua fatura agora é R${:.2f} e valor da parcelar é {} de R${:.2f}".format(novovalor, divisao, valorparcela))
        break
    elif(divisao == 9):
        novovalor = fatura / divisao * 12.8
        valorparcela = novovalor / divisao 
        print("O valor da sua fatura agora é R${:.2f} e valor da parcelar é {} de R${:.2f}".format(novovalor, divisao, valorparcela))
        break
    elif(divisao == 10):
        novovalor = fatura / divisao * 13.7
        print("O valor da sua fatura agora é {:.2f}".format(novovalor))
        break
    else:
        print("Erro, tente novamente")
        continue