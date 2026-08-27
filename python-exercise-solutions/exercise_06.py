#Este código pede a largura e a altura para o usuário
#Depois calcula a área e o perímetro usando esses valores
#E mostra os resultados na tela

base = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"A área é: {area}")
print(f"O perímetro é: {perimetro}")