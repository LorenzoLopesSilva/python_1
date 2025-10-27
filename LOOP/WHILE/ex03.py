tamanho = int(input("Digite o tamanho da lista: "))
soma = 0
i = tamanho
while i > 0:
    n = float(input("Digite um numero: "))
    soma += n
    i -= 1

media = soma/tamanho
print(f"Media: {media}")