maior = float(input("Digite o preço do produto 1: "))
soma = maior

for i in range(2, 15):
    valor = float(input(f"Digite o preço do produto {i + 1}: "))

    if valor > maior:
        maior = valor
    soma += valor

media = soma/15

print(f"Maior preço: R${maior:.2f} \nMédia: R${media:.2f}")