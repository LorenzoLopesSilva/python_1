operacao = input("Deseja converter para Celsius(C) ou Fahrenheit(F)? ")
temperatura = float(input("Digite a temperatura que será convertida: "))

if operacao == "C":
    temperaturaConvertida = 5/9 * (temperatura - 32)
    print(f"A temperatura em Celsius é: {temperaturaConvertida:.2f}")
elif operacao == "F":
    temperaturaConvertida = 32 + (temperatura * 9/5)
    print(f"A temperatura em Fahrenheit é: {temperaturaConvertida:.2f}")
else:
    print("Operação invalida.")