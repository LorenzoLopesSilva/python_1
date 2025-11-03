homens = 0
mulheres = 0
soma_idade_homens = 0
soma_idades = 0
mulheres_maiores_que_20 = 0

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    sexo = input(f"Digite o sexo da pessoa {i+1}. (f/m): ").lower()

    if sexo == "m":
        homens += 1
        soma_idade_homens += idade
        soma_idades += idade
    elif sexo == "f":
        mulheres += 1
        if idade > 20:
            mulheres_maiores_que_20 += 1
        soma_idades += idade
    else:
        print("Valor incorreto. Pessoa não contabilizada.")

media_idades = soma_idades/(mulheres + homens)
media_idade_homens = soma_idade_homens/homens

print(f"\nHomens cadastrados: {homens}"
      f"\nMulheres cadastradas: {mulheres}"
      f"\nMédia das idades: {media_idades}"
      f"\nMédia das idades dos homens: {media_idade_homens}"
      f"\nMulheres com mais de 20 anos: {mulheres_maiores_que_20}")