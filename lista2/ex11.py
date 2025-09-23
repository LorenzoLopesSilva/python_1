horas_mensais = int(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_hora = float(input("Digite o salario por hora: "))

if horas_mensais > 160:
    salario = 160 * salario_hora
    extra = (horas_mensais - 160) * (salario_hora + salario_hora * 0.5)
    salario_total = salario + extra
    print(f"O salario total é de R${salario_total:.2f}")
else:
    print(f"O salario total é de: R${horas_mensais * salario_hora}")