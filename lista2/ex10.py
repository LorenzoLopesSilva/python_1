hora_inicial = int(input("Digite a hora inicial do jogo: "))
hora_final = int(input("Digite a hora final do jogo: "))

sub_horas = hora_inicial - hora_final

if sub_horas < 0:
    horas = sub_horas * -1
    print(f"O jogo durou {horas} horas")
else:
    horas = 24 - sub_horas
    print(f"O jogo durou {horas} horas")