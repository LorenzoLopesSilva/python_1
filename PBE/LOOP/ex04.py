import random
import time

r1 = 0
r2 = 0

def andar(nome):
    passos = random.randint(1, 3)
    print(f"\n{nome} andou {passos} passos.")
    return passos

i = 1
while r1 < 20 and r2 < 20:
    print(f"\nTurno {i}")

    r1 += andar("Robô 1")
    print(f"Posição: {r1}")

    r2 += andar("Robô 2")
    print(f"Posição: {r2}")

    # time.sleep(2)
    i += 1
if r1 > r2:
    print("Robô 1 ganhou")
elif r1 < r2:
    print("Robô 2 ganhou")
else:
    print("Empate")