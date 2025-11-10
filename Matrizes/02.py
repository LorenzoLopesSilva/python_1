import numpy as np
numeros = np.array(list(map(int, input("Digite 3 numeros separados por espaço: ").split())))

soma = np.sum(numeros)

print(f"Soma dos numeros: {soma}")