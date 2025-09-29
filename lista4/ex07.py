lado1 = float(input("Digite o primeiro lado do triangulo: "))
lado2 = float(input("Digite o segundo lado do triangulo: "))
lado3 = float(input("Digite o terceiro lado do triangulo: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:

    if lado1 == lado2 == lado3:
        print("Triangulo equilátero!")
    elif lado1 != lado2 != lado3 != lado1:
        print("Triangulo escaleno!")
    else:
        print("Triangulo isosceles!")
else:
    print("Não forma um triangulo: ")