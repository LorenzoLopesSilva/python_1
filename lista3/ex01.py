comprimento = float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
area = comprimento * largura
print(f"A área do terreno é de {area}m²")
if area < 100:
    print("Terreno popular")
elif 100 <= area <= 500:
    print("Terreno master")
else:
    print("Terreno VIP")