#Este código pede um número real para o usuário
#Depois verifica se ele é positivo, negativo ou igual a zero
#E mostra a classificação na tela

numero = float(input("Digite um número: "))

if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "ZERO"

print("Resultado:", resultado)
