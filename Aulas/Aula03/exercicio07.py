Litros=float(input("E quantos litros você abasteceu?\n"))
Tipodecombustivel=input("Qual foi o combustivel que você solicitou?\n"
                        "G ou g para Gasolina\n"
                        "E ou e para Etanol\n")
vGas=5.80
vEta=4.90
if Tipodecombustivel=="G" or Tipodecombustivel=="g":
    ValorG = Litros*vGas
    print(f"Você abasteceu {Litros} litros e gastou R${ValorG:.2f}")
elif Tipodecombustivel=="E" or Tipodecombustivel=="e":
    ValorE = Litros*vEta
    print(f"Você abasteceu {Litros} litros e gastou R${ValorE:.2f}!")
else:
    print(f"Tipo de combusstivel não cadastrado!")