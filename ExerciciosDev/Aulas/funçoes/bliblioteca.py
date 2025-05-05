def imprimirNome(nome):
    print(f"Olá {nome}")

def piramide(t):
    for x in range(1, t+1, 1):
        for y in range(0, x):
             print(x, end=" ")
        print()

def Vogal(texto):
    cont=0
    for x in range(len(texto)):
        if texto[x]== "a" or texto[x]== "e" or texto[x]== "i" or texto[x]== "o" or texto[x]== "u":
            cont+=1
    print(cont)

def valorEstoque(produto, quantidade, valorUnitario):
    calculo=quantidade*valorUnitario
    return produto, calculo

def tipoNumero(n):
    if n>0:
        return"P"
    elif n<0:
        return "N"
    else:
      return "Z"

def somasNumericas(numero1, numero2):
    soma=numero1+numero2
    print(soma)

def somasNumericas2(*numero):
    soma=0
    for x in range(len(numero)):
        soma+=numero[x]
    print(soma)

def Leitura(texto):
    cont=0
    for x in range(len(texto)-1, -1, -1):
        print(texto[x], end=" ")
        if texto[x] not in " ":
            cont+=1
    print(f"\n {cont}")

def endoidar(l):
    novaLista=[]
    for x in l:
        if x not in novaLista:
            novaLista.append(x)
    print(novaLista)


