import random
import time

while True:
    escolhaMenu = input("Escolha um jogo: "
                            "\n1- Adivinhe o tesouro"
                            "\n2- Combate Épico"
                            "\n3- Senha Hacker"
                            "\n4- Corrida de Robôs"
                            "\n5- Zumbi na noite"
                            "\n6- Sair"
                        "\nOpção: ")
    if escolhaMenu == "1":
        coordenada = random.randint(1, 10)
        acertou = 0

        while acertou == 0:
            escolha = int(input("Adivinhe a coordenada: "))

            if escolha == coordenada:
                print("ACERTOU!")
                acertou += 1
            elif escolha < coordenada:
                print("À direita")
            else:
                print("À esquerda")

        input("Enter para continuar")

    elif escolhaMenu == "2":
        def dano_jogador():
            dano = random.randint(10, 30)
            print(f"\nO dano do jogador foi: {dano}")
            return dano


        def dano_monstro():
            dano = random.randint(5, 25)
            print(f"O dano do monstro foi: {dano}")
            return dano


        jogador = 100
        monstro = 100
        rodadas = 1


        for i in range(100):
            monstro = monstro - dano_jogador()
            print(f"Vida do monstro: {monstro}")
            if monstro <= 0:
                print("Jogador venceu!")
                break

            jogador = jogador - dano_monstro()
            print(f"Vida do jogador: {jogador}")
            if jogador <= 0:
                print("Monstro venceu.")
                break

            time.sleep(2)

            rodadas += 1

        print(f"O jogo durou {rodadas} rodadas")

        input("Enter para continuar")

    elif escolhaMenu == "3":
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

        input("Enter para continuar")

    elif escolhaMenu == "4":
        r1 = 0
        r2 = 0


        def andar(nome):
            passos = random.randint(1, 3)
            print(f"\n{nome} andou {passos} passos.")
            return passos


        i = 1
        while r1 < 20 and r2 < 20:
            print(f"\nTurno {i}")

            r1 += andar("Robô 1")
            print(f"Posição: {r1}")
            for i in range(r1):
                print("#", end='')

            r2 += andar("Robô 2")
            print(f"Posição: {r2}")
            for i in range(r2):
                print("#", end='')

            time.sleep(2)
            i += 1
        if r1 > r2:
            print("\nRobô 1 ganhou")
        elif r1 < r2:
            print("\nRobô 2 ganhou")
        else:
            print("\nEmpate")

        input("Enter para continuar")

    elif escolhaMenu == "5":
        municoes = 5
        zumbis = 10

        for i in range(municoes):
            print(f"\nZumbis restantes: {zumbis}")
            print(f"Munições: {municoes}\nTiro {i + 1}: ")
            time.sleep(1)

            acerto = random.randint(0, 3)

            print(f"\nVocê acertou {acerto} zumbis")

            zumbis -= acerto
            municoes -= 1

            if zumbis <= 0:
                print("\nTodos os zumbis morreram. \nVocê sobreviveu!")
                break

            time.sleep(3)

        if zumbis > 0:
            print("\nMorreu!")

        input("Enter para continuar")

    elif escolhaMenu == "6":
        print("Obrigado por jogar!")
        break

    else:
        print("Escolha inválida")
        continue