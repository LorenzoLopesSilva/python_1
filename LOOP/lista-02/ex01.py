from random import randint

lista = []
maior_que_5 = 0
divisiveis_por_3= 0

for i in range(20):
    lista.append(randint(0, 10))

for i in lista:
    if i > 5:
        maior_que_5 += 1
    if i % 3 == 0:
        divisiveis_por_3 += 1

print(f"Numeros: {lista}"
      f"\nMaiores que 5: {maior_que_5}"
      f"\nDivisiveis por 3: {divisiveis_por_3}")