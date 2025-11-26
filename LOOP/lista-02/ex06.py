maior_idade = 0
qtd_homens = 0
soma_idade_homens = 0
qtd_mulheres = 0
mulher_mais_jovem = 9999

continuar = "s"

while continuar == "s":
    sexo = input("Sexo (M/F): ").lower()
    idade = int(input("Idade: "))

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "m":
        qtd_homens += 1
        soma_idade_homens += idade
    else:
        qtd_mulheres += 1
        if idade < mulher_mais_jovem:
            mulher_mais_jovem = idade

    continuar = input("Quer continuar? (s/n): ").lower()

if qtd_homens > 0:
    media_homens = soma_idade_homens / qtd_homens
else:
    media_homens = 0

print("Maior idade:", maior_idade)
print("Quantidade de homens:", qtd_homens)
print("Mulher mais jovem:", mulher_mais_jovem)
print("Média de idade entre os homens:", media_homens)
