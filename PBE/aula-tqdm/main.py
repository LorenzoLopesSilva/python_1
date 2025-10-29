from tqdm import tqdm
import time

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

def tempo():
    for i in tqdm(range(100)):
        time.sleep(0.05)

if a > b:
    tempo()
    print(f"{a} maior que {b}")

else:
    tempo()
    print(f"{b} maior que {a}")
