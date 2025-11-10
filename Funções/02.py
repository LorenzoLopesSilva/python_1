def maior (n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print(f"O maior numero é: {maior(n1, n2)}")