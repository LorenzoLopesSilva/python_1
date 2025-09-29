numero = input("Digite um numero de 4 digitos: ")

numero = list(numero)

if numero[3] == "0":
    print("O numero não pode terminar com o digito 0.")
else:
    novo_numero = [numero[3], numero[2], numero[1], numero[0]]
    print(int("".join(novo_numero)))

