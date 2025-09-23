valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salario do comprador: "))
anos = int(input("Digite em quantos anos será pago: "))

prestacao = valor_casa / (anos * 12)

if prestacao <= salario * 0.3:
    print(f"Prestação mensal: R${prestacao:.2f}.")
else:
    print(f"Emprestimo negado")