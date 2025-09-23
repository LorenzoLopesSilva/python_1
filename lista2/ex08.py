ano = int(input("Digite o ano desejado: "))

if ano % 4 == 0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")