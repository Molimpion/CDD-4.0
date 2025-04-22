Alunos=int(input(f"Quantos alunos tem na sala:\n"))
soma=0
x=1
while x<=Alunos:
    notas=float(input(f"Digite as notas:\n"))
    soma += notas
    x+=1
media=soma/Alunos
print(f"A media da sala é:{media}!")