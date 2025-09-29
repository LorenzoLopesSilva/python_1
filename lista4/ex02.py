data = input("Digite uma data no formato dd/mm/aaaa: ")

if len(data) > 10:
    print("Data inválida (caracteres extra)")
elif len(data) < 10:
    print("Data invalida (caracteres faltantes)")

else:
    valores_data = data.split("/")
    if int(valores_data[0]) > 31 or len(valores_data[0]) > 2:
        print("Data invalida")
    elif int(valores_data[1]) > 12 or len(valores_data[1]) > 2:
        print("Data invalida")
    elif len(valores_data) > 4:
        print("Data invalida")
    else:
        print("Data valida!")




