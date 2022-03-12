def iniciar():
    print("Calculo de horas trabalhadas")

    horas_trabalhadas = float(input("Quantas horas você trabalha por dia ?"))
    salario_hora = float(input("E qual é o seu salario por hora ?"))
    dias_mes = int(input("Quantos dias tem o mês de referencia ?"))

    salario = dias_mes * (salario_hora * horas_trabalhadas)

    print("$",salario)


if(__name__ == "__main__"):
    iniciar()