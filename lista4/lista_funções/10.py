def soma_impares(n):
    soma = 0
    impar = 1

    for i in range(n):
        soma += impar
        impar += 2

    print("Resultado:", soma)


n = int(input("Digite um número: "))
soma_impares(n)
