user_1 = input("Usuario 1: pedra, papel ou tesoura? ")
user_2 = input("Usuario 2: pedra, papel ou tesoura? ")

if user_1 == user_2:
    print("Empate!")

elif user_1 == "pedra" and user_2 == "tesoura":
    print("Usuario 1 venceu!")

elif user_1 == "tesoura" and user_2 == "pedra":
    print("Usuario 2 venceu!")

elif user_1 == "tesoura" and user_2 == "papel":
    print("Usuario 1 venceu!")

elif user_1 == "papel" and user_2 == "tesoura":
    print("Usuario 2 venceu!")

elif user_1 == "papel" and user_2 == "pedra":
    print("Usuario 1 venceu!")

elif user_1 == "pedra" and user_2 == "papel":
    print("Usuario 2 venceu!")

else:
    print("Escolha invalida")