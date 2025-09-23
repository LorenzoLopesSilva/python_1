distancia = float(input("Digite a distancia que será percorrida: "))

if distancia <= 200:
    valorPassagem = 0.50
else:
    valorPassagem = 0.45

valorTotal = distancia * valorPassagem

print(f"O preço da passagem é: R${valorTotal:.2f}")