morangos = float(input("Digite a quantidade de morangos (kg): "))
macas = float(input("Digite a quantidade de maçãs (kg): "))

kg_total = morangos + macas

if morangos <= 5:
    valor_morangos = morangos * 2.5
else:
    valor_morangos = morangos * 2.2

if macas <= 5:
    valor_macas = macas * 1.8
else:
    valor_macas = macas * 1.5

valor_total = valor_macas + valor_morangos

if valor_total > 25 or kg_total > 8:
    valor_total -= valor_total * 0.1

print(f"O valor total da compra é: R${valor_total:.2f}")