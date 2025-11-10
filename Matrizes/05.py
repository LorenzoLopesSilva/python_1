import numpy as np

matriz = np.array([list(map(int, input("Digite os 3 numeros da primeira linha separados por ',' : ").split(','))),
           list(map(int, input("Digite os 3 numeros da segunda linha separados por ',' : ").split(',')))])

maior_linha2 = np.max(matriz[1])

print(f"Maior numero da linha 2: {maior_linha2}")