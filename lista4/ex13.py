preco = float(input("Digite o preço: "))

if preco < 50:
    preco_novo = preco + preco * 0.05
elif 50 <= preco < 100:
    preco_novo = preco + preco * 0.10
else:
    preco_novo = preco + preco * 0.15

print(f"Novo preço: R${preco_novo:.2f}")

if preco_novo < 80:
    print("Barato")
elif 80 <= preco_novo <= 120:
    print("Normal")
elif 120 < preco_novo <= 200:
    print("Caro")
else:
    print("Muito caro")