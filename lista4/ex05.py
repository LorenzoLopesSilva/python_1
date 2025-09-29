
combustivel = input("Digite o combustivel: Gasolina(g) ou Alcool(a): ").lower()
litros = float(input("Digite a quantidade em litros: "))

#gasolina
if combustivel == "g":
    valor_inicial = litros * 5.89
    if litros < 20:
        valor_total = valor_inicial - valor_inicial * 0.04
    else:
        valor_total = valor_inicial - valor_inicial * 0.06
    print(f"Valor total: R${valor_total:.2f}")

#alcool
elif combustivel == "a":
    valor_inicial = litros * 3.97
    if litros < 20:
        valor_total = valor_inicial - valor_inicial * 0.03
    else:
        valor_total = valor_inicial - valor_inicial * 0.05
    print(f"Valor total: R${valor_total:.2f}")

else:
    print("Valor invalido")

