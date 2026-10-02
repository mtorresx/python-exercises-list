#Este código pede dois números reais para o usuário
#Depois compara os valores para descobrir qual deles é o maior
#E mostra o maior valor, ou informa que os valores são iguais

valor1 = float(input("Primeiro valor: "))
valor2 = float(input("Segundo valor: "))

if valor1 > valor2:
    print("Maior valor:", valor1)
elif valor2 > valor1:
    print("Maior valor:", valor2)
else:
    print("VALORES IGUAIS")
