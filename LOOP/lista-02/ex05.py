

salario_homens = 0
salario_mulheres = 0

continuar = True

while continuar:
    sexo = input("\nDigite o sexo do funcionario (f/m):  ").lower()
    salario = float(input("Digite o salário do funcionario: "))

    if sexo == "f":
        salario_mulheres += salario
    elif sexo == "m":
        salario_homens += salario

    escolha = input("Aperte Enter para continuar: ")
    if escolha != "":
        continuar = False

print(f"\nSalário total dos homens: R${salario_homens:.2f}"
      f"\nSalário total das mulheres: R${salario_mulheres:.2f}")
