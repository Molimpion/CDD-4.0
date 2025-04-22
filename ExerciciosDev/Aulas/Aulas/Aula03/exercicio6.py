time1=input("Qual o nome do seu time?\n")
time2=input("Qual o nome do adiversario?\n")
golstime1=int(input("digite o numero de gols: \n"))
golstime2=int(input("digite o numero de gols: \n"))
if golstime1>golstime2:
    print(f"{time1} vencedor")
else:
    if golstime2>golstime1:
        print(f"{time2} vencedor")
    else:print("Empate")
