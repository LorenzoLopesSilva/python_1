import numpy as np

array = np.zeros(5, dtype= int)
for i in range(5):
    n = int(input("Digite um numero inteiro: "))
    array[i] = n
maior = np.max(array)

print(f"Maior numero: {maior}")