velocidade = int(input("Digite a velocidade: "))

if velocidade > 80:
    print("Foi multado")
    multa = (velocidade - 80) * 5
    print(f"Multa no valor de R${multa:.2f}")
else:
    print("Está no limite de velocidade")