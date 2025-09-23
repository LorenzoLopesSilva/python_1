salario_fixo = float(input("Digite o salário fixo: "))
valor_vendas = float(input("Digite o valor das vendas: "))

if valor_vendas <= 1500:
    comissao = valor_vendas * 0.03
else:
    extra = (valor_vendas - 1500) * 0.05
    comissao = valor_vendas * 0.03 + extra

salario_total = salario_fixo + comissao
print(f"Seu salario total é de: R${salario_total:.2f}")