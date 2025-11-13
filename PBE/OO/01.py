class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        print("O personagem atacou")

    def receber_dano(self, valor):
        self.vida -= valor

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self):
        super().atacar()
        print(f"{self.nome} atacou com uma espada!")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self):
        super().atacar()
        print(f"{self.nome} lançou uma magia!")

guerreiro1 = Guerreiro("Ragnar", 200)
mago1 = Mago("Gandalf", 200)

guerreiro1.atacar()
mago1.atacar()
guerreiro1.atacar()
mago1.atacar()

guerreiro1.receber_dano(150)
mago1.receber_dano(100)

print(f"\nVida do Guerreiro: {guerreiro1.vida}"
      f"\nVida do Mago: {mago1.vida}")
