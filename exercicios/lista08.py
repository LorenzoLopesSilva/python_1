custo_fabrica = float(input("Digite o custo de fabrica do carro: "))

percentual_distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45

custo_final = custo_fabrica + percentual_distribuidor + impostos

print("O custo total do carro é:", custo_final)