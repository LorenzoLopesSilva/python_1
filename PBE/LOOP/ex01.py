import random

coordenada = random.randint(1, 10)
acertou = 0

while acertou == 0:
    escolha = int(input("Adivinhe a coordenada: "))

    if escolha == coordenada:
        print("ACERTOU!")
        acertou += 1
    elif escolha < coordenada:
        print("À direita")
    else:
        print("À esquerda")