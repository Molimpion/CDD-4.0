pin=123456
tentativas=1
mensagem="senha Bloqueada"
while tentativas <=3:
    senha=int(input(f"Digite a senha:\n"))
    if senha==pin:
       mensagem="Liberado"
       break
    tentativas+=1
print(mensagem)