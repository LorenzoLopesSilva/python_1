qtde_atual = int(input("Digite a quantidade atual em estoque: "))
qtde_maxima = int(input("Digite a quantidade maxima: "))
qtde_minima = int(input("Digite a quantidade minima: "))

media = (qtde_maxima + qtde_minima) / 2

if qtde_atual >= media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")