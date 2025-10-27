tamanho = int(input("Qual o tamanho da lista? "))
soma = 0
for i in range(0, tamanho):
    n = float(input("Digite um numero: "))

    soma += n

media = soma/tamanho

print(f"Media: {media}")



