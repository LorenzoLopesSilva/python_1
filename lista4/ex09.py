valor = float(input("Digite o valor: "))
estado = input("Digite o estado (MG; SP; RJ; MS): ").lower()

if estado == "mg":
    valor_final = valor + valor * 0.07
elif estado == "sp":
    valor_final = valor + valor * 0.12
elif estado == "rj":
    valor_final = valor + valor * 0.15
elif estado == "ms":
    valor_final = valor + valor * 0.08
else:
    print("Valor do estado incorreto.")
    exit()
print(f"Valor total: R${valor_final:.2f}")



