km = float(input("Digite a distancia em km: "))
litro = float(input("Digite a quantidade de gasolina em litros: "))

consumo = km/litro

if consumo < 8:
    print("Venda o carro!")
elif 8 <= consumo <= 12:
    print("Economico!")
else:
    print("Super econômico!")

