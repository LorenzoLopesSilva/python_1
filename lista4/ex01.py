aresta1 = float(input("Digite o valor da primeira aresta: ")) #altura
aresta2 = float(input("Digite o valor da segunda aresta: ")) #largura
aresta3 = float(input("Digite o valor da terceira aresta: ")) #profundidade

face1 = aresta1 * aresta2
face2 = aresta1 * aresta3
base = aresta2 * aresta3

area_total = face1 * 2 + face2 * 2 + base * 2

tinta_total = area_total * 3


if area_total % 10 == 0:
    rolo_valor = (area_total / 10) * 5

else:
    rolo_valor = ((area_total // 10) + 1) * 5

mao_de_obra = area_total * 20

if tinta_total % 5 == 0:
    lata_valor = (tinta_total / 5) * 45
else:
    lata_valor = ((tinta_total // 5) + 1) * 45

materiais = rolo_valor + lata_valor

print(f"Mão de obra: R${mao_de_obra:.2f} \nMateriais: R${materiais:.2f} \nValor total: R${(mao_de_obra + materiais):.2f}")