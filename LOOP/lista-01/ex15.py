qtde = int(input("Digite o numero total de mercadorias no estoque: "))
soma = 0
for i in range(qtde):
    valor = float(input(f"Digite o valor da mercadoria {i + 1}: "))

    soma += valor

media = soma/qtde

print(f"O valor total em estoque é: R${soma:.2f} \nA média dos valores é: R${media:.2f}")


