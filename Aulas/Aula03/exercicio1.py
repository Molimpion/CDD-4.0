# Mostrar nome, idade e salario
nome=input("Qual é o seu nome?\n")
idade=int(input("Quantos anos você tem?\n"))
salario=float(input("quanto você recebe por mês?\n"))
aumento=float(input("quantos % seu salario aumentou por mês?"))
valorp=salario*aumento/100
salariof=salario+valorp
print(f"Prazer em conhecer você {nome},",
      f"então você tem {idade}?",
      f"e já recebe {salario:.2f} por mês?\n",
      f" você agora vai receber R$:{valorp:.2f} há mais por mês?\n",
      f" no total voce vai receber R${salariof:.2f} no total!")