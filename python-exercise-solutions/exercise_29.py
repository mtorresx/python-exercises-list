#Este código pede três medidas para o usuário
#Primeiro verifica se formam um triângulo e, se formarem, classifica o tipo
#E mostra se é equilátero, isósceles ou escaleno

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 and lado2 == lado3:
        print("Resultado: EQUILÁTERO")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Resultado: ISÓSCELES")
    else:
        print("Resultado: ESCALENO")
else:
    print("Resultado: NÃO FORMA TRIÂNGULO")
