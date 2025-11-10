def fatorial(n):
    f = 1
    for i in range(n):
        f *= n - i
    return f

n = int(input("Digite um numero inteiro: "))

print(f"Fatorial de {n} é: {fatorial(n)}")