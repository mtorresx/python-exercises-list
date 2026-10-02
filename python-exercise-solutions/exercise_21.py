#Este código pede duas notas para o usuário
#Depois calcula a média e compara com 7,0
#E mostra a média e se o aluno foi aprovado ou reprovado

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 7.0:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print(f"Média: {media:.1f}")
print("Situação:", situacao)
