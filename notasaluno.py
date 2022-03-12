def iniciar():
    print("Calculo de nota de alunos")

    nota1 = float(input("Qual a nota 1 do aluno?"))
    nota2 = float(input("Qual a nota 2 do aluno?"))

    media = (nota1 + nota2) / 2
    media = media >= 6

    print("A media do aluno é: {} ".format(media))

    if(media):
        print("aluno passou de materia")

    else:
        print("O aluno reprovou na materia")
