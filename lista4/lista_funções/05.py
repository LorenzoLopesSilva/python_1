def somar_salario(sexo, sal_homem, sal_mulher):
    # soma no grupo certo
    if sexo == "f":
        sal_mulher += salario
    elif sexo == "m":
        sal_homem += salario

    return sal_homem, sal_mulher


salario_homens = 0   # total homens
salario_mulheres = 0 # total mulheres

continuar = True

while continuar:
    sexo = input("\nSexo (f/m): ").lower()  # pega sexo
    salario = float(input("Salário: "))     # pega salário

    # atualiza os totais
    salario_homens, salario_mulheres = somar_salario(
        sexo, salario_homens, salario_mulheres
    )

    # Enter continua, outra tecla para
    if input("Enter p/ continuar, outra tecla p/ parar: ") != "":
        continuar = False

# mostra os totais
print("\nTotal homens: R$", salario_homens)
print("Total mulheres: R$", salario_mulheres)
