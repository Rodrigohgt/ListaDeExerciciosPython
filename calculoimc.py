print("Calcular o seu IMC")

kg = float(input("Quantos kilos você tem?"))
altura = float(input("Qual é a sua altura?"))

imc = kg / (altura * altura)

print("O seu imc está em: ", imc)

if(imc <= 20):
    print("Você está abaixo da média para seu peso")
if(imc >= 35):
    print("Você está acima da média para seu peso")
else:
    print("Você está na média de pesso")