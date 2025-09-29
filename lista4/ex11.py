valor = int(input("Valor do saque: "))

n200 = 0
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0

if 5 <= valor <= 9998:
    if valor >= 200:
        n200 = int(input("Quantas notas de 200? "))
        valor -= n200 * 200
        print(f"Valor restante: {valor}")
    if valor < 0:
        print("A quantidade de notas excedeu o valor")
        exit()

    if valor >= 100:
        n100 = int(input("Quantas notas de 100? "))
        valor -= n100 * 100
        print(f"Valor restante: {valor}")
    if valor < 0:
        print("A quantidade de notas excedeu o valor")
        exit()

    if valor >= 50:
        n50 = int(input("Quantas notas de 50? "))
        valor -= n50 * 50
        print(f"Valor restante: {valor}")
    if valor < 0:
        print("A quantidade de notas excedeu o valor")
        exit()

    if valor >= 20:
        n20 = int(input("Quantas notas de 20? "))
        valor -= n20 * 20
        print(f"Valor restante: {valor}")
    if valor < 0:
        print("A quantidade de notas excedeu o valor")
        exit()

    if valor >= 10:
        n10 = int(input("Quantas notas de 10? "))
        valor -= n10 * 10
        print(f"Valor restante: {valor}")
    if valor < 0:
        print("A quantidade de notas excedeu o valor")
        exit()

    if valor >= 5:
        n5 = int(input("Quantas notas de 5? "))
        valor -= n5 * 5
        print(f"Valor restante: {valor}")
    if valor < 0:
        print("A quantidade de notas excedeu o valor")
        exit()

    if valor >= 2:
        n2 = int(input("Quantas notas de 2? "))
        valor -= n2 * 2
        print(f"Valor restante: {valor}")
    if valor < 0:
        print("A quantidade de notas excedeu o valor")
        exit()



print(f"Notas de 200: {n200}"
      f"\nNotas de 100: {n100}"
      f"\nNotas de 50: {n50}"
      f"\nNotas de 20: {n20}"
      f"\nNotas de 10: {n10}"
      f"\nNotas de 5: {n5}"
      f"\nNotas de 2: {n2}")

