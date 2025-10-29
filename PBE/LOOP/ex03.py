import random

senha = random.randint(0000, 9999)


if senha < 1000:
    senha = "0" + f"{senha}"
else:
    senha = str(senha)

acertou = 0

while acertou == 0:
    tentativa = input("Tente acertar a senha: ")

    if tentativa == senha:
        print("ACERTOU!")
        acertou += 1
    else:
        caracteres = 0

        for i in tentativa:
            if i in senha:
                caracteres += 1
        print(f"Você acertou {caracteres} digitos.")


