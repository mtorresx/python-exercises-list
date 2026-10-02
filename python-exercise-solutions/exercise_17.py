#Este código pede um número inteiro para o usuário
#Depois verifica se o resto da divisão por 2 é igual a zero
#E mostra se o número é par ou ímpar na tela

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

print("Resultado:", resultado)
