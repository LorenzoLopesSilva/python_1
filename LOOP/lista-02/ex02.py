soma_idade = 0
maior_que_18 = 0
menor_que_5 = 0
maior_idade = 0

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    if idade >= 18:
        maior_que_18 += 1
    elif idade < 5:
        menor_que_5 += 1

    if idade > maior_idade:
        maior_idade = idade

    soma_idade += idade

media_idade = soma_idade / 10

print(f"\nMédia das idades: {media_idade} anos"
      f"\nMaiores de 18 anos: {maior_que_18}"
      f"\nMenores que 5 anos: {menor_que_5}"
      f"\nMaior idade: {maior_idade} anos")