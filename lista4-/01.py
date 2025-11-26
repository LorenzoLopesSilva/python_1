a1 = float(input("Digite a primeira aresta: "))
a2 = float(input("Digite a segunda aresta: "))
a3 = float(input("Digite a terceira aresta: "))

def calcula_e_imprime(a1, a2, a3):
    area = 2 * (a1 * a2 + a1 * a3 + a2 * a3)
    tinta = area * 3
    rolos = int(area / 10)
    if area % 10 != 0:
        rolos = rolos + 1
    valor_rolos = rolos * 5
    latas = int(tinta / 5)
    if tinta % 5 != 0:
        latas = latas + 1
    valor_latas = latas * 45
    materiais = valor_rolos + valor_latas
    mao = area * 20
    print(f"Mão de obra: R${mao:.2f} \nMateriais: R${materiais:.2f} \nValor total: R${(mao + materiais):.2f}")

calcula_e_imprime(a1, a2, a3)