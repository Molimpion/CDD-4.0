Hora1=int(input(f"Me diga um horario no formato 24horas?\n"))
minutos1=int(input(f"me diga os minutos que acompanham essas horas:\n"))
Hora2=int(input(f"a seguir me de um horario no formato 24horas:\n"))
minutos2=int(input(f"me diga os minutos que acompanham essas horas:\n"))
horastotais=Hora1+Hora2
minutostotais=minutos1+minutos2
if horastotais >12:
   horastotais=horastotais-12
if horastotais > 24:
       horastotais = horastotais - 24
if minutostotais >=60:
    minutostotais=minutostotais-60
    horastotais=horastotais+1
print(f"{horastotais}:{minutostotais}")