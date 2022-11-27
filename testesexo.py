from ast import Break
from tkinter import E


while(True):
    sexo = str(input("Digite o sexo do paciente"))
    if(sexo == "M"):
        print("Masculino")
        break
    if(sexo == "F"):
        print("Feminino")
        break
    else:
        print("Sexo invalido, digite novamente")
        