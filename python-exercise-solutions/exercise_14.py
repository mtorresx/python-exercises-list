#Este código pede dois valores para o usuário
#Depois troca os valores entre as duas variáveis
#E mostra os novos valores de cada variável na tela

valor_a = input("Digite o valor de A: ")
valor_b = input("Digite o valor de B: ")

temporario = valor_a
valor_a = valor_b
valor_b = temporario

print("Novo valor de A:", valor_a)
print("Novo valor de B:", valor_b)