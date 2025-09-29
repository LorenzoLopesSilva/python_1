operacao = int(input("Escolha a opção: \n1- Soma de 2 numeros"
                     "\n2- Diferença entre 2 numeros (maior pelo menor)"
                     "\n3- Produto entre 2 numeros"
                     "\n4- Divisão entre 2 numeros (o denominador não pode ser zero)"
                     "\nOpção: "))

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

if operacao == 1:
    resultado = n1 + n2

elif operacao == 2:
    if n1 > n2:
        resultado = n1 - n2
    else:
        resultado = n2 - n1
elif operacao == 3:
    resultado = n1 * n2
elif operacao == 4:
    if n2 == 0:
        print("Denominador não pode ser 0")
    else:
        resultado = n1 / n2
else:
    print("Operação invalida!")
    exit()

print(f"Resultado da operação: {resultado} ")