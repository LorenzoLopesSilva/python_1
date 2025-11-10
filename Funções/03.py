import numpy as np
def media(lista):
    media = np.mean(lista)
    return media

lista = np.array(list(map(int, input("Digite uma lista de numeros separados por virgula: ").split(','))))

print(f"Media dos numeros: {media(lista):.2f}")

