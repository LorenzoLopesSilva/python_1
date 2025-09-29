numero = input("Digite um numero inteiro menor que 1000: ")
if int(numero) < 1000:
    quantidades = list(numero)



    if len(quantidades) == 3:
        if int(quantidades[0]) > 1:
            centenas = f"{quantidades[0]} centenas"
        else:
            centenas = f"{quantidades[0]} centena"

        if int(quantidades[1]) > 1:
            dezenas = f"{quantidades[1]} dezenas"
        else:
            dezenas = f"{quantidades[1]} dezena"

        if int(quantidades[2]) > 1:
            unidades = f"{quantidades[2]} unidades"
        else:
            unidades = f"{quantidades[2]} unidade"
        print(f"{numero}: {centenas}, {dezenas}, {unidades}")


    elif len(quantidades) == 2:

        if int(quantidades[0]) > 1:
            dezenas = f"{quantidades[0]} dezenas"
        else:
            dezenas = f"{quantidades[0]} dezena"

        if int(quantidades[1]) > 1:
            unidades = f"{quantidades[1]} unidades"
        else:
            unidades = f"{quantidades[1]} unidade"
        print(f"{numero}: {dezenas}, {unidades}")

    else:
        if int(quantidades[0]) > 1:
            unidades = f"{quantidades[0]} unidades"
        else:
            unidades = f"{quantidades[0]} unidade"
        print(f"{numero}: {unidades}")



