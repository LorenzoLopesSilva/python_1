maior = float(input("Digite um numero: "))
menor = maior

for i in range(2, 101):
    n = float(input(f"Digite o {i}° numero: "))

    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f"Menor numero: {menor} \nMaior numero: {maior}")

