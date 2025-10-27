i = 5
maior = 0

while i > 0:
    n = int(input("Digite um numero: "))

    if(n > maior):
        maior = n
    i -= 1

print(f"Maior: {maior}")