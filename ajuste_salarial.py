print("********************************")
print("Ajuste salarial de funcionarios")
print("********************************")

sim_nao = int(input("Gostaria de calcular um salario? Digite 1 para continuar ou 2 para encerrar"))

if(sim_nao == 1):
    while(sim_nao == 1):
        salario_atual = float(input("Digite o salario do funcionario: "))
        ajuste_anual = float(input("Digite o ajuste salarial do funcionario: "))

        novo_salario = salario_atual + (salario_atual * ajuste_anual) / 100

        print("O novo salario do funcionario é de: {} ".format(novo_salario))
        
        sim_nao = int(input("Gostaria de calcular outro salario? Digite 1 para continuar ou 2 para encerrar:"))
        continue
else:

    print("Encerrando calculo")
    