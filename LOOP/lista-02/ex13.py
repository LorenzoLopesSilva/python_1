padrao1 = float(input("Tempo padrão da etapa 1: "))
padrao2 = float(input("Tempo padrão da etapa 2: "))
padrao3 = float(input("Tempo padrão da etapa 3: "))

maior_total = 0
equipe_vencedora = 0
empate = False

numero = int(input("Número da equipe (0 para encerrar): "))

while numero != 0:

    t1 = float(input("Tempo da equipe na etapa 1: "))
    t2 = float(input("Tempo da equipe na etapa 2: "))
    t3 = float(input("Tempo da equipe na etapa 3: "))


    d1 = padrao1 - t1
    if d1 < 0:
        d1 = -d1
    if d1 < 3:
        p1 = 100
    elif d1 <= 5:
        p1 = 80
    else:
        p1 = 80 - (d1 - 5) / 5

    d2 = padrao2 - t2
    if d2 < 0:
        d2 = -d2
    if d2 < 3:
        p2 = 100
    elif d2 <= 5:
        p2 = 80
    else:
        p2 = 80 - (d2 - 5) / 5

    d3 = padrao3 - t3
    if d3 < 0:
        d3 = -d3
    if d3 < 3:
        p3 = 100
    elif d3 <= 5:
        p3 = 80
    else:
        p3 = 80 - (d3 - 5) / 5

    total_pontos = p1 + p2 + p3

    print("\nEquipe:", numero)
    print("Pontos por etapa:", p1, p2, p3)
    print("Total de pontos:", total_pontos)
    print("--------------------------------")

    if total_pontos > maior_total:
        maior_total = total_pontos
        equipe_vencedora = numero
        empate = False
    elif total_pontos == maior_total:
        empate = True

    numero = int(input("Número da próxima equipe (0 para encerrar): "))

if empate == True:
    print("\nHouve empate! Maior pontuação obtida:", maior_total)
else:
    print("\nEquipe vencedora:", equipe_vencedora, "com", maior_total, "pontos.")
