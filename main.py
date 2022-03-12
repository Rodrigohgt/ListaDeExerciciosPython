import adivinhacaowhile
import adivinharfor
import ajuste_salarial
import cadastroeloginfor
import calculadora
import calculoimc
import horas_trabalhadas
import jogo_da_forca
import kmcarro
import notasaluno
import qualomaior

print("Escolha seu exercicios para testar")

x = int(input("Adivinhacaowhile(1) adivinharfor(2) ajuste_salarial(3) cadastroelogin(4) calculadora(5) calculoimc(6) horas_trabalhadas(7) jogo_da_forca(8) kmcarro(9) notasaluno(10) qualomaior(11)"))

if(x == 1):
    print("iniciando AdivinhacaoWhile")
    adivinhacaowhile.iniciar()
elif(x == 2):
    print("iniciando adivinharfor")
    adivinharfor.iniciar()
elif(x == 3):
    print("iniciando ajuste_salarial")
    ajuste_salarial.iniciar()
elif(x == 4):
    print("iniciando cadastroelogin")
    cadastroeloginfor.iniciar()
elif(x == 5):
    print("iniciando calculadora")
    calculadora.iniciar()
elif(x == 6):
    print("iniciando calculoimc")
    calculoimc.iniciar()
elif(x == 7):
    print("iniciando horas_trabalhadas")
    horas_trabalhadas.iniciar()
elif(x == 8):
    print("iniciando jogo_da_forca")
    jogo_da_forca.iniciar()
elif(x == 9):
    print("iniciando kmcarro")
    kmcarro.iniciar()
elif(x == 10):
    print("iniciando notasaluno")
    notasaluno.iniciar()
elif(x == 11):
    print("qualomaior")
    qualomaior.iniciar()
else:
    print("exercicio invalido")