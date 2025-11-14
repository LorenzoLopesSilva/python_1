# pega todas as alturas e pesos e faz as contagens
def coletar_dados():
    soma_alturas = 0
    mais_90 = 0
    menos_50kg_menos_160m = 0
    mais_190m_mais_100kg = 0

    for i in range(7):
        altura = float(input(f"\nDigite a altura da pessoa {i+1} em cm: "))
        peso = float(input(f"Digite o peso da pessoa {i+1} em kg: "))

        if peso > 90:
            mais_90 += 1
        elif peso < 50:
            if altura < 160:
                menos_50kg_menos_160m += 1

        if altura > 190:
            if peso > 100:
                mais_190m_mais_100kg += 1

        soma_alturas += altura

    return [soma_alturas, mais_90, menos_50kg_menos_160m, mais_190m_mais_100kg]


# calcula média das alturas
def calcular_media_alturas(soma_alturas):
    return soma_alturas / 7


# Execução
dados = coletar_dados()

soma_alturas = dados[0]
mais_90 = dados[1]
menos_50kg_menos_160m = dados[2]
mais_190m_mais_100kg = dados[3]

media_alturas = calcular_media_alturas(soma_alturas)

print(f"\nMédia das alturas: {media_alturas:.2f}cm"
      f"\nPessoas que pesam mais que 90kg: {mais_90}"
      f"\nPessoas com menos de 50kg e menos de 160cm: {menos_50kg_menos_160m}"
      f"\nPessoas com mais de 190cm e mais de 100kg: {mais_190m_mais_100kg}")
