ano = int(input("Digite seuano de nascimento: "))

idade = 2025 - ano

if idade > 18:
    print(f"Já se passaram {idade - 18} anos do seu alistamento.")
elif idade < 18:
    print(f"Faltam {18 - idade} anos para seu alistamento.")
else:
    print("Você está no ano de alistamento.")