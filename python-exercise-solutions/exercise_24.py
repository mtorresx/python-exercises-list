#Este código pede um ano inteiro para o usuário
#Depois verifica se ele é divisível por 400, ou por 4 e não por 100
#E mostra se o ano é bissexto ou não na tela

ano = int(input("Ano: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    resultado = "ANO BISSEXTO"
else:
    resultado = "NÃO BISSEXTO"

print("Resultado:", resultado)
