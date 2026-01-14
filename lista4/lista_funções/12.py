# função para calcular pontos de uma etapa
def calcular_pontos(padrao, tempo):
    # diferença absoluta
    d = padrao - tempo
    if d < 0:
        d = -d
    
    # regras dos pontos
    if d < 3:
        return 100
    elif d <= 5:
        return 80
    else:
        return 80 - (d - 5) / 5


# valores padrões
padrao1 = float(input("Tempo padrão da etapa 1: "))
padrao2 = float(input("Tempo padrão da etapa 2: "))
padrao3 = float(input("Tempo padrão da etapa 3: "))

numero = int(input("Número da equipe (0 para encerrar): "))

while numero != 0:
    t1 = float(input("Tempo da equipe na etapa 1: "))
    t2 = float(input("Tempo da equipe na etapa 2: "))
    t3 = float(input("Tempo da equipe na etapa 3: "))

    # calcula pontos usando a função
    p1 = calcular_pontos(padrao1, t1)
    p2 = calcular_pontos(padrao2, t2)
    p3 = calcular_pontos(padrao3, t3)

    total_pontos = p1 + p2 + p3

    print("Equipe:", numero)
    print("Pontos por etapa:", p1, p2, p3)
    print("Total de pontos:", total_pontos)
    print("--------------------------------")

    numero = int(input("Número da próxima equipe (0 para encerrar): "))
