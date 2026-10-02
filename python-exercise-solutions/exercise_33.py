#Este código pede um número de 1 a 7 para o usuário
#Depois verifica qual dia da semana corresponde a esse número
#E mostra o nome do dia, ou opção inválida para outros valores

numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    dia = "SEGUNDA-FEIRA"
elif numero == 2:
    dia = "TERÇA-FEIRA"
elif numero == 3:
    dia = "QUARTA-FEIRA"
elif numero == 4:
    dia = "QUINTA-FEIRA"
elif numero == 5:
    dia = "SEXTA-FEIRA"
elif numero == 6:
    dia = "SÁBADO"
elif numero == 7:
    dia = "DOMINGO"
else:
    dia = "OPÇÃO INVÁLIDA"

print(dia)
