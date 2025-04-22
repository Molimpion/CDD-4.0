n=int(input(f"Digite um numero:\n"))
if n%2==0 and n<0:
    print(f"{n} é um numero par e negativo!")
elif n%2==0 and n>0:
    print(f"{n} é um numero par e positivo!")
elif n%2!=0 and n<0:
    print(f"{n} é um numero impar e negativo!")
else:
    print(f"{n} é um numero impar e positivo!")