#soma=0
#for x in range(1,6):
#    numeros=int(input(f"Digite um numero:\n"))
#   soma+=numeros
#   media=soma/5
#    print(f"media")
soma=0
x=1
while x<=5:
    numeros = int(input(f"Digite um numero:\n"))
    soma += numeros
    x+=1
media=soma/5
print(f"{media}")