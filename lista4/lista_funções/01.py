from random import randint

# cria a lista com números aleatórios
def gerar_lista():
    lista = []
    for i in range(20):
        lista.append(randint(0, 10))
    return lista

# conta quantos são maiores que 5
def contar_maiores_que_5(lista):
    maior_que_5 = 0
    for i in lista:
        if i > 5:
            maior_que_5 += 1
    return maior_que_5

# conta quantos são divisíveis por 3
def contar_divisiveis_por_3(lista):
    divisiveis_por_3 = 0
    for i in lista:
        if i % 3 == 0:
            divisiveis_por_3 += 1
    return divisiveis_por_3


# Execução
lista = gerar_lista()
maior_que_5 = contar_maiores_que_5(lista)
divisiveis_por_3 = contar_divisiveis_por_3(lista)

print(f"Numeros: {lista}"
      f"\nMaiores que 5: {maior_que_5}"
      f"\nDivisiveis por 3: {divisiveis_por_3}")
