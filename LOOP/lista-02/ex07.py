pessoa_mais_velha = ""
maior_idade = 0

mulher_mais_jovem_nome = ""
mulher_mais_jovem_idade = 9999

soma_idades = 0
total = 0

homens_mais_30 = 0
mulheres_menos_18 = 0

continuar = "s"

while continuar == "s":
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").lower()

    total += 1
    soma_idades += idade

    if idade > maior_idade:
        maior_idade = idade
        pessoa_mais_velha = nome

    if sexo == "m" and idade > 30:
        homens_mais_30 += 1

    if sexo == "f":
        if idade < mulher_mais_jovem_idade:
            mulher_mais_jovem_idade = idade
            mulher_mais_jovem_nome = nome
        if idade < 18:
            mulheres_menos_18 += 1

    continuar = input("Quer continuar? (s/n): ").lower()

media_idades = soma_idades / total

print("Pessoa mais velha:", pessoa_mais_velha)
print("Mulher mais jovem:", mulher_mais_jovem_nome)
print("Média de idade:", media_idades)
print("Homens com mais de 30 anos:", homens_mais_30)
print("Mulheres com menos de 18 anos:", mulheres_menos_18)
