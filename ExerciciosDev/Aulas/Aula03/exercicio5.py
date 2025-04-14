nota1=float(input(f"Me diga a sua nota do primeiro trimestre!\n"))
nota2=float(input(f"Agora a do segundo trimestre!\n"))
nota3=float(input(f"Por ultimo a do terceiro!\n"))
media=(nota1+nota2+nota3)/3
if media>7:
    print(f"Aluno Aprovado, media:{media:.2f}!")
elif media >=4:
    print(f"Aluno pode fazer recuperação, media:{media:.2f}!")
else:
    print(f"Aluno reprovado sem chance de recuperação, media:{media:.2f}!")