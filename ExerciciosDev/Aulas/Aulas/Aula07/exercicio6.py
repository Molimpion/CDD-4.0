peso=float(input(f"Me diga seu peso:\n"))
altura=float(input(f"a sua altura tambem:\n"))
imc=peso/(altura*altura)
if imc<18.6:
    print(f"Voce esta abaixo do peso!")
elif imc>=18.6 or imc<=24.9:
    print(f"Peso ideal!(parabens)")
elif imc >= 25.0 or imc <= 29.9:
    print(f"Levemente acima do peso")
elif imc >= 30.0 or imc <= 34.9:
    print(f"Obesidade grau I")
elif imc >= 35.0 or imc <= 39.9:
    print(f"Obesidade grau II(severa)")
else:
    print(f"Obesidade grau III(morbida)")