class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
    
    def exibir_info(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}")

produto1 = Produto("Boné", 50.0)
produto1.aplicar_desconto(10)
produto1.exibir_info()