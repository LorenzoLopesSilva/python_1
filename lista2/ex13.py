n_conta = int(input("Digite o numero da conta: "))
saldo = float(input("Digite o saldo: "))
debito = float(input("Digite o débito: "))
credito = float(input("Digite o crédito: "))

saldo_atual = saldo - debito + credito
print(f"O salario da conta {n_conta} é: R${saldo_atual:.2f}")

if saldo_atual >= 0:
    print("Saldo positivo!")
else:
    print("Saldo negativo")