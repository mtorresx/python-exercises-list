#Este código pede três números reais para o usuário
#Depois compara os valores para descobrir o maior e o menor
#E mostra os dois resultados na tela (funciona com valores repetidos)

n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
n3 = float(input("Terceiro valor: "))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print("Maior:", maior)
print("Menor:", menor)
