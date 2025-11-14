salario_minimo = 1804.00

total_folha = 0
total_pecas = 0

homens_A = homens_B = homens_C = 0
mulheres_A = mulheres_B = mulheres_C = 0

pecas_homens_A = pecas_homens_B = pecas_homens_C = 0
pecas_mulheres_A = pecas_mulheres_B = pecas_mulheres_C = 0

maior_salario = 0
operario_maior_salario = 0

numero = int(input("Número do operário (0 para encerrar): "))

while numero != 0:
    pecas = int(input("Quantidade de peças fabricadas: "))
    sexo = input("Sexo (m = masculino / f = feminino): ")

    total_pecas += pecas


    if pecas <= 30:
        salario = salario_minimo
        classe = "A"
    elif pecas <= 35:
        salario = salario_minimo + (pecas - 30) * (salario_minimo * 0.03)
        classe = "B"
    else:
        salario = salario_minimo + (pecas - 30) * (salario_minimo * 0.05)
        classe = "C"

    total_folha += salario


    if sexo == "m": 
        if classe == "A":
            homens_A += 1
            pecas_homens_A += pecas
        elif classe == "B":
            homens_B += 1
            pecas_homens_B += pecas
        else:
            homens_C += 1
            pecas_homens_C += pecas
    else:  
        if classe == "A":
            mulheres_A += 1
            pecas_mulheres_A += pecas
        elif classe == "B":
            mulheres_B += 1
            pecas_mulheres_B += pecas
        else:
            mulheres_C += 1
            pecas_mulheres_C += pecas


    if salario > maior_salario:
        maior_salario = salario
        operario_maior_salario = numero

    print("Salário do operário:", salario)
    print("----------------------------------")

    numero = int(input("Número do próximo operário (0 para encerrar): "))


if homens_A > 0:
    media_homens_A = pecas_homens_A / homens_A
else:
    media_homens_A = 0

if homens_B > 0:
    media_homens_B = pecas_homens_B / homens_B
else:
    media_homens_B = 0

if homens_C > 0:
    media_homens_C = pecas_homens_C / homens_C
else:
    media_homens_C = 0

if mulheres_A > 0:
    media_mulheres_A = pecas_mulheres_A / mulheres_A
else:
    media_mulheres_A = 0

if mulheres_B > 0:
    media_mulheres_B = pecas_mulheres_B / mulheres_B
else:
    media_mulheres_B = 0

if mulheres_C > 0:
    media_mulheres_C = pecas_mulheres_C / mulheres_C
else:
    media_mulheres_C = 0

print("Total da folha de pagamento: R$", total_folha)
print("Total de peças produzidas:", total_pecas)
print("Médias de peças dos homens: Classe A:", media_homens_A, " | Classe B:", media_homens_B, " | Classe C:", media_homens_C)
print("Médias de peças das mulheres: Classe A:", media_mulheres_A, " | Classe B:", media_mulheres_B, " | Classe C:", media_mulheres_C)
print("Operário com maior salário:", operario_maior_salario)
