soma = float(input("Digite o valor da mercadoria 1: "))
qtde = 1

indice = 1

while indice > 0:
    mais_produtos = input("MAIS MERCADORIAS? (S/N): ").lower()

    if mais_produtos == "s":
        qtde += 1
        valor = float(input(f"Digite o valor da mercadoria {qtde}: "))
        soma += valor
        indice += 1
    elif mais_produtos != "n":
        print("VALOR INVALIDO")
        indice += 1

    indice -= 1

media = soma/qtde

print(f"O valor total em estoque é: R${soma:.2f} \nA média dos valores é: R${media:.2f}")