#Este código pede três medidas para o usuário
#Depois verifica se cada lado é menor que a soma dos outros dois
#E mostra se as medidas formam ou não um triângulo

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Resultado: FORMAM UM TRIÂNGULO")
else:
    print("Resultado: NÃO FORMAM UM TRIÂNGULO")
