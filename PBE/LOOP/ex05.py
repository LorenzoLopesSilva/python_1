import random
import time

municoes = 5
zumbis = 10

for i in range(municoes):
    print(f"\nZumbis restantes: {zumbis}")
    print(f"Munições: {municoes}\nTiro {i + 1}: ")
    time.sleep(1)

    acerto = random.randint(0, 3)

    print(f"\nVocê acertou {acerto} zumbis")

    zumbis -= acerto
    municoes -= 1

    if zumbis <= 0:
        print("\nTodos os zumbis morreram. \nVocê sobreviveu!")
        break

    time.sleep(3)

if zumbis > 0:
    print("\nMorreu!")

