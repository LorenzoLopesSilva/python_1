n = int(input("Digite um numero maior que 0: "))

while n <= 0:
    print("Valor invalido")
    n = int(input("Digite um valor maior que 0: "))
for i in range(1, n + 1):
    print(i)