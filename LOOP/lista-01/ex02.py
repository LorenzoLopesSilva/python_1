n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

while n2 == 0:
    print("Segundo valor invalido")
    n2 = float(input("Digite um segundo numero diferente de 0: "))

div = n1/n2

print(div)