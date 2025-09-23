nome = input("Digite o nome do funcionario: ")
salario_atual = float(input("Digite o salário atual: "))
anos = int(input("Quantos anos trabalhados na empresa: "))

if anos < 3:
    extra = salario_atual * 0.03
elif 3 <= anos < 10:
    extra = salario_atual * 0.125
else:
    extra = salario_atual * 0.20

salario = salario_atual + extra

print(f"O novo salario de {nome} é: R${salario:.2f}")