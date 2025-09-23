numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é ímpar")

if numero % 3 == 0 and numero % 5 == 0:
    print("Multiplo de 3 e 5")
elif numero % 3 == 0:
    print("Multiplo de 3")
elif numero % 5 == 0:
    print("Multiplo de 5")
else:
    print("Não é multiplo de 3 nem de 5")