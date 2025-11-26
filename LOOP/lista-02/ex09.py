num = int(input("Digite um número: "))
divisoes = 0

for i in range(1, num+1):
    if num % i == 0:
        divisoes += 1

if divisoes == 2:
    print("Número primo")
else:
    print("Não é primo")
