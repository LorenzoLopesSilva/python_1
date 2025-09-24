import os

palavra = input("Digite a palavra secreta: ")
numero = int(input("Digite o numero secreto: "))

os.system('cls')

tentativaPalavra = input("Tente acertar a palavra: ")
tentativaNumero = int(input("Tente acertar o numero: "))

if tentativaPalavra == palavra and tentativaNumero == numero:
    print("Cofre Aberto!")
else:
    print("Cofre Fechado.")