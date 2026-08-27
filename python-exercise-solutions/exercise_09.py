#Este código pede o salário atual para o usuário
#Depois calcula um aumento de 15% sobre esse valor
#E mostra o valor do aumento e o novo salário na tela

salario = float(input("Digite o salário atual: R$ "))

aumento = salario * 0.15
novo_salario = salario + aumento

print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")