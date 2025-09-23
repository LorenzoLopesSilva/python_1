ano = int(input("Digite seu ano de nascimento: "))

idade = 2025 - ano

if idade >= 18:
    print("Pode votar!")
else:
    print("Não pode votar.")