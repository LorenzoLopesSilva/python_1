import random

def dano_jogador():
    dano = random.randint(10, 30)
    print(f"O dano do jogador foi: {dano}")
    return dano

def dano_monstro():
    dano = random.randint(5, 25)
    print(f"O dano do monstro foi: {dano}")
    return dano

jogador = 100
monstro = 100
rodadas = 1

for i in range(100):
    monstro = monstro - dano_jogador()
    print(f"Vida do monstro: {monstro}")
    if monstro <= 0:
        print("Jogador venceu!")
        break

    jogador = jogador - dano_monstro()
    print(f"Vida do jogador: {jogador}")
    if jogador <=0:
        print("Monstro venceu.")
        break

    rodadas += 1

print(f"O jogo durou {rodadas} rodadas")
