#Este código pede um número inteiro para o usuário
#Depois verifica se ele é divisível por 3, por 5, por ambos ou por nenhum
#E mostra a situação na tela

numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("DIVISÍVEL POR 3 E 5")
elif numero % 3 == 0:
    print("DIVISÍVEL APENAS POR 3")
elif numero % 5 == 0:
    print("DIVISÍVEL APENAS POR 5")
else:
    print("NÃO DIVISÍVEL POR 3 NEM 5")
