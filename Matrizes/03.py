from os.path import split

import numpy as np

# matriz = np.array([[1, 2, 3],
#                    [2, 4, 6]])

matriz = np.array([list(map(int, input("Digite a primeira linha com os numeros separados por ';' : ").split(';'))),
                   list(map(int, input("Digite a segunda linha separada por ';' : ").split(';')))])


soma_linha1 = np.sum(matriz[0])

print(f"Soma da linha 1: {soma_linha1}")