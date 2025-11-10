import numpy as np

matriz = np.array([list(map(int, input("Digite os 2 numeros da primeira linha separados por ',' : ").split(','))),
           list(map(int, input("Digite os 2 numeros da segunda linha separados por ',' : ").split(',')))])

# soma = np.sum(matriz)

# media = soma/ np.size(matriz)

media = np.mean(matriz)
print(f"A média é: {media:.2f}")
