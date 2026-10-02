#Este código pede duas notas para o usuário
#Depois calcula a média e verifica em qual faixa ela se encaixa
#E mostra a média e a situação: reprovado, recuperação ou aprovado

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    situacao = "REPROVADO"
elif media < 7.0:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print(f"Média: {media:.1f}")
print("Situação:", situacao)
