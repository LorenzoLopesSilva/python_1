contador = 0
for i in range(10):
    n = float(input("Digite um numero: "))

    if n < 0:
        contador += 1

print(f"Numeros negativos: {contador}")


