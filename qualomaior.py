def iniciar():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))

    if(num1 > num2):
        print("numero {} é maior".format(num1))

    else:
        print("numero {} é maior".format(num2))


if(__name__ == "__main__"):
    iniciar()