i = 0
soma_salario = 0
soma_filhos = 0
maior_salario = 0
contador_salario = 0
habitantes = True

while habitantes:
    salario = float(input(f"Digite o salário da pessoa {i + 1}: "))

    if salario < 0:
        habitantes = False
    else:
        filhos = int(input(f"Digite a quantidade de filhos da pessoa {i + 1}: "))
        print("aaaaaaaaaa")

        if salario > maior_salario:
            maior_salario = salario

        if salario < 150:
            contador_salario += 1

        soma_salario += salario
        soma_filhos += filhos

        i += 1

media_salario = soma_salario/i
media_filhos = soma_filhos/i

percentual = (100/(i) * contador_salario)

print(f"Média salarial: R${media_salario:.2f}"
      f"\nMédia dos filhos: {media_filhos}"
      f"\nMaior salário: {maior_salario}"
      f"\nPessoas com salario menor que R$150,00: {percentual:.2f}%")