#Este código pede um número real para o usuário
#Depois verifica se ele está dentro do intervalo fechado de 10 até 20
#E mostra se o número está dentro ou fora do intervalo

numero = float(input("Digite um número: "))

if numero >= 10 and numero <= 20:
    print("DENTRO")
else:
    print("FORA")
