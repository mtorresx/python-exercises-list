#Este código pede três números inteiros para o usuário
#Depois coloca os valores em ordem crescente usando comparações e trocas
#E mostra os valores ordenados na tela (aceita valores repetidos)

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a > b:
    auxiliar = a
    a = b
    b = auxiliar

if b > c:
    auxiliar = b
    b = c
    c = auxiliar

if a > b:
    auxiliar = a
    a = b
    b = auxiliar

print(f"Ordem crescente: {a}, {b}, {c}")
