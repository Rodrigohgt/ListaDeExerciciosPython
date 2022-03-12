print("sistema de cadastro")
usuario = str(input("Digite seu usuario para cadastro: "))
senha = int(input("Digite seu PIN para cadastro *APENAS NUMEROS*: "))
print("cadastro efetuado")

tentativas_de_login = 5

for i in range(1, tentativas_de_login + 1):
    login = str(input("digite seu usuario: "))
    senhalogin = int(input("digite sua senha: "))


    if((login == usuario)) and  ((senhalogin == senha)):
        print("Login efetuado com sucesso: ")
        break
    else:
        print("erro no login: ")
        
print("quantidade de tentativas acabou! acesso bloqueado")