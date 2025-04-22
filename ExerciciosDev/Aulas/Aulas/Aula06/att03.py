n1=int(input(f"Digite um numero:\n"))
n2=int(input(f"Digite um segundo numero:\n"))
while n2==0:
 n2=int(input(f"Numero invalido, recebemos apenas valores diferentes de zero, digite o segundo numero novamente:\n"))
div=n1/n2
print(f"{div}")

