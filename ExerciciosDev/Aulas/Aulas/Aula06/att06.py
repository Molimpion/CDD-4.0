Resposta="S"
while Resposta=="S":
N1=int(input(f"Digite a sua primeira nota:\n"))
while N1<0 or N1>10:
    N1 = int(input(f"Digite a sua primeira nota novamente:\n"))
N2=int(input(f"Digite a sua segunda nota:\n"))
while N2<0 or N2>10:
    N2 = int(input(f"Digite a sua segunda nota novamente :\n"))
media=(N1+N2)/2
print(f"Sua Media é:{media}\n")
Resposta=input(f"Deseja fazer outro calculo?\n")