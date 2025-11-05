
padrao1 = float(input("Tempo padrão da etapa 1: "))
padrao2 = float(input("Tempo padrão da etapa 2: "))
padrao3 = float(input("Tempo padrão da etapa 3: "))

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

    print("Equipe:", numero)
    print("Pontos por etapa:", p1, p2, p3)
    print("Total de pontos:", total_pontos)
    print("--------------------------------")

    numero = int(input("Número da próxima equipe (9999 para encerrar): "))
