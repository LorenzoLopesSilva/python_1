numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 > numero2 > numero3:
    print(f"{numero1} é o maior")
elif numero2 > numero1 > numero3:
    print(f"{numero2} é o maior")
else:
    print(f"{numero3} é o maior")