n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
for i in range(100):
    if(n2 == 0):
        n2 = float(input("Digite um segundo valor diferente de 0: "))

divisao = n1/n2
print(divisao)