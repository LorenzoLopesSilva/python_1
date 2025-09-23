genero = input("Genero masculino (m) ou feminino (f)? ")
salarioAtual = float(input("Digite o salario atual: "))
tempo = int(input("Digite o tempo de trabalho: "))

if genero == "f":
    if tempo < 15:
        salario = salarioAtual + salarioAtual * 0.05
    elif 15 <= tempo <= 20:
        salario = salarioAtual + salarioAtual * 0.12
    else:
        salario = salarioAtual + salarioAtual * 0.23
    print(f"O novo salário é: R${salario:.2f}")

elif genero == "m":
    if tempo < 20:
        salario = salarioAtual + salarioAtual * 0.03
    elif 15 <= tempo <= 30:
        salario = salarioAtual + salarioAtual * 0.13
    else:
        salario = salarioAtual + salarioAtual * 0.25
    print(f"O novo salário é: R${salario:.2f}")
else:
    print("Valores incorretos")
