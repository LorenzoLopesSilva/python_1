idade = int(input("Digite sua idade: "))

if idade < 2:
    print("BEBE")
elif 2 <= idade < 13:
    print("CRIANÇA")
elif 13 <= idade < 18:
    print("ADOLESCENTE")
elif 18 <= idade < 60:
    print("ADULTO")
else:
    print("IDOSO")