nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + (nota2 * 2) + (nota3 * 3) + ((nota1 + nota2 + nota3) /3)) / 7

if media >= 9:
    conceito = "A"
elif 9 > media >= 7.5:
    conceito = "B"
elif 7.5 > media >= 6:
    conceito = "C"
else:
    conceito = "D"

print(f"Media de aproveitamento: {media:.2f} \nConceito: {conceito}")