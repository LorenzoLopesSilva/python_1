contador = 0
for i in range(10):
    n = float(input("Digite um numero: "))

    if 10 <= n <= 20:
        contador += 1

print(f"Numeros entre 10 e 20: {contador}")