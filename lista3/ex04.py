carro = input("O carro é popular(p) ou de luxo(l)? ")
dias = int(input("Digite quantos dias de uso: "))
km = int(input("Digite a quantidade de km percorrido: "))

if carro == "p":
    if km <= 100:
        valor = dias * 90 + km * 0.20
        print(f"O valor do serviço é: R${valor:.2f}")
    else:
        valor = dias * 90 + km * 0.10
        print(f"O valor do serviço é: R${valor:.2f}")

if carro == "l":
    if km <= 200:
        valor = dias * 150 + km * 0.30
        print(f"O valor do serviço é: R${valor:.2f}")
    else:
        valor = dias * 150 + km * 0.25
        print(f"O valor do serviço é: R${valor:.2f}")
else:
    print("Tipo do carro invalido")


