class Pessoa():
    def __init__(self,nome,idade,peso):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.dormindo=False
        self.falando=False
    def apresentar(self):
        print(f"Olá meu nome é {self.nome}"
        f" eu tenho{self.idade} anos e peso {self.peso}")

    def comer(self, comida):
        if self.comendo == True:
            print(f"{self.nome} já está comendo!")
        elif self.falando == True:
            print(f"{self.nome} não pode comer pq está falando!")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer pq está dormindo!")
        else:
            print(f"{self.nome} foi comer! {comida}")
            self.comendo = True

    def parar_de_comer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer!")
        else:
            print(f"{self.nome} não está comendo!")

    def falar(self):
        if self.comendo == True:
            print(f"{self.nome} não pode comer pq está falando!")
        elif self.falando == True:
            print(f"{self.nome} já esta falando!")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar pq está dormindo!")
        else:
            print(f"{self.nome} foi falar!")
            self.falar = True

    def parar_de_falar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar!")
        else:
            print(f"{self.nome} não está falando!")

    def dormir(self):
        if self.comendo == True:
            print(f"{self.nome} não pode comer pq está dormindo!")
        elif self.falando == True:
            print(f"{self.nome} não pode falar pq está dormindo!")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo!")
        else:
            print(f"{self.nome} foi comer!")
            self.dormir = True

    def parar_de_dormir(self):
        if self.dormir == True:
            print(f"{self.nome} acordou!")
        else:
            print(f"{self.nome} não está dormindo!")